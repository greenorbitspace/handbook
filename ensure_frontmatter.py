import os
import sys
import yaml
from datetime import datetime, timezone

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def parse_front_matter(content):
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            rest = parts[2].lstrip('\n')
            try:
                fm = yaml.safe_load(fm_text)
                if fm is None:
                    fm = {}
                return fm, rest
            except yaml.YAMLError:
                print(f"Warning: YAML parsing error in {path}")
                return None, content
    return None, content

def generate_front_matter_yaml(data):
    from yaml.representer import SafeRepresenter
    class LiteralStr(str): pass

    def literal_str_representer(dumper, data):
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')

    yaml.add_representer(LiteralStr, literal_str_representer)

    if 'description' in data and isinstance(data['description'], str) and '\n' in data['description']:
        data['description'] = LiteralStr(data['description'])

    return yaml.dump(data, sort_keys=False, allow_unicode=True)

def filename_to_title(filename):
    name = os.path.splitext(filename)[0]
    return name.replace('-', ' ').replace('_', ' ').title()

def filename_to_alias(filename):
    name = os.path.splitext(filename)[0]
    return f"/{type_cli}/{name}/"

def iso8601_today_with_offset():
    now = datetime.now(timezone.utc).astimezone()
    return now.isoformat(timespec='seconds')

def update_front_matter(fm, filename, content_type):
    updated = fm.copy() if fm else {}

    # Set type from CLI argument
    updated['type'] = content_type

    # Weight: integer, default 2
    if 'weight' not in updated or not isinstance(updated['weight'], int):
        updated['weight'] = 2

    # Date: valid ISO8601, else current
    try:
        datetime.fromisoformat(updated['date'])
    except (KeyError, ValueError, TypeError):
        updated['date'] = iso8601_today_with_offset()

    # Title: non-empty string
    if not updated.get('title') or not isinstance(updated['title'], str):
        updated['title'] = filename_to_title(filename)

    # linkTitle: mirror title if missing or invalid
    if not updated.get('linkTitle') or not isinstance(updated['linkTitle'], str):
        updated['linkTitle'] = updated['title']

    # Aliases: list of strings with at least one alias
    if not updated.get('aliases') or not isinstance(updated['aliases'], list) or not all(isinstance(a, str) for a in updated['aliases']):
        updated['aliases'] = [filename_to_alias(filename)]

    # Description: present string (empty if missing)
    if 'description' not in updated or not isinstance(updated['description'], str):
        updated['description'] = ""

    return updated

def process_file(path, content_type):
    content = read_file(path)
    fm, body = parse_front_matter(content)
    filename = os.path.basename(path)
    new_fm = update_front_matter(fm, filename, content_type)
    fm_yaml = generate_front_matter_yaml(new_fm)
    new_content = f"---\n{fm_yaml}---\n\n{body.lstrip()}"
    write_file(path, new_content)
    print(f"Processed: {path}")

def process_directory(dir_path, content_type):
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.md'):
                process_file(os.path.join(root, file), content_type)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python ensure_frontmatter.py <directory_or_file> <type>")
        sys.exit(1)
    path = sys.argv[1]
    type_cli = sys.argv[2].strip()
    if os.path.isdir(path):
        process_directory(path, type_cli)
    elif os.path.isfile(path):
        process_file(path, type_cli)
    else:
        print(f"Path not found: {path}")