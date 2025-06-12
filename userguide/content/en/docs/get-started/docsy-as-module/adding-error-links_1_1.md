---
weight: 2
date: '2025-06-12'
title: Adding Error Links 1 1
aliases:
- /docs/adding-error-links_1_1/
description: ''
linkTitle: Adding Error Links 1 1
type: docs
---

# Adding Warning and Error Descriptions

Next.js has a system to add helpful links to warnings and errors.

This allows the logged message to be short while giving a broader description and instructions on how to solve the warning/error on the documentation.

In general, all warnings and errors added should have these links attached.

Below are the steps to add a new link:

1. Run `pnpm new-error` which will create the error document and update the manifest automatically.
2. At the end of the command the URL for the error will be provided, add that to your error.
