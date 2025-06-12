---
weight: 2
date: '2025-06-12'
title: Pricing Themes 1
aliases:
- /docs/pricing-themes_1/
description: ''
linkTitle: Pricing Themes 1
type: docs
---

{{ range .Params }}
{{ $tier := . }}

##### {{ . }}

    {{- range site.Data.public.pricing_themes }}
        {{- if eq .tier $tier }}

1. {{ .name }}
        {{- end }}
    {{- end }}
{{- end }}
