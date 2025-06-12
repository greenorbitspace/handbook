import re
import os
import sys
from pathlib import Path

def find_latest_log_file(search_dir='.'):
    """Find the newest .log file in given directory."""
    log_files = list(Path(search_dir).glob('*.log'))
    if not log_files:
        return None
    return max(log_files, key=lambda f: f.stat().st_mtime)

def extract_problematic_files(log_path):
    """Extract file paths from Hugo build errors about missing shortcode templates."""
    pattern = re.compile(
        r'failed to extract shortcode: template for shortcode "[^"]+" not found'
    )
    file_pattern = re.compile(
        r'process: readAndProcessContent: "([^"]+):\d+:\d+"'
    )
    problematic_files = set()

    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            if pattern.search(line):
                file_match = file_pattern.search(line)
                if file_match:
                    filepath = file_match.group(1)
                    problematic_files.add(filepath)
    return problematic_files

def delete_files_in_folder(file_paths, folder):
    folder_path = Path(folder).resolve()
    for filepath in file_paths:
        abs_path = Path(filepath).resolve()
        # Only delete if inside the specified folder
        if folder_path in abs_path.parents or abs_path == folder_path:
            if abs_path.is_file():
                try:
                    abs_path.unlink()
                    print(f"Deleted problematic file: {abs_path}")
                except Exception as e:
                    print(f"Failed to delete {abs_path}: {e}")
            else:
                print(f"File not found or not a file, skipping: {abs_path}")
        else:
            print(f"Skipped (outside folder): {abs_path}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python clean_hugo_shortcodes.py <folder-to-clean> [log-folder]")
        sys.exit(1)

    folder_to_clean = sys.argv[1]
    log_search_dir = sys.argv[2] if len(sys.argv) > 2 else '.'

    log_file = find_latest_log_file(log_search_dir)
    if not log_file:
        print(f"No .log files found in directory '{log_search_dir}'.")
        sys.exit(1)

    print(f"Using latest log file: {log_file}")

    problematic_files = extract_problematic_files(log_file)

    if not problematic_files:
        print("No problematic shortcode error files found in the log.")
        sys.exit(0)

    print(f"Found {len(problematic_files)} problematic files:")
    for f in problematic_files:
        print(f" - {f}")

    delete_files_in_folder(problematic_files, folder_to_clean)