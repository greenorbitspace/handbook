---
weight: 2
date: '2025-06-12'
title: Tech Stack 1
aliases:
- /docs/tech-stack_1/
description: ''
linkTitle: Tech Stack 1
type: docs
---

{{- /*Initialize.*/}}
{{- $title := "" }}

{{- /*Get params.*/}}
{{- with (.Get 0) }}
  {{- $title = . }}
{{- else }}
  {{- errorf "The %q shortcode requires a single positional argument."}}
{{- end }}

{{- with (index site.Data.public.teach_stack $title) }}

- **Description:** {{ .description }}
{{- with .provisioner }}
- **Provisioner:** {{ . }}
{{- end }}
{{- with .deprovisioner }}
- **Deprovisioner:** {{ . }}
{{- end }}
{{- with .need_move_to_okta }}
- **Okta Enabled:** {{ . }}
{{- end }}
{{- with .critical_systems_tier }}
- **Critical Systems Tier:** {{ . }}
{{- end }}
{{- end }}
