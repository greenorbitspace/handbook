---
weight: 2
date: '2025-06-12'
title: Kubeutil 1 1
aliases:
- /docs/kubeutil_1_1/
description: ''
linkTitle: Kubeutil 1 1
type: docs
---

# kubeutil

> **This module is intended for internal use and should never be imported directly.**
> Checks should use the methods exposed by the `AgentCheck` class instead, see
> [dedicated docs](https://datadoghq.dev/integrations-core/base/about/) for
> more details.

This modules provides specific functionalities to help collecting metrics on
kubernetes clusters.

## Implementation

* [kubeutil.c](/rtloader/common/builtins/kubeutil.c)
* [kubeutil.h](/rtloader/common/builtins/kubeutil.h)
* [kubeutil.go](/pkg/collector/python/kubeutil.go)

## Functions

```python

    def get_connection_info():
        """Get kubelet connection informations.

        Returns:
            A dictionary containing connection info, can be empty.
        """
```
