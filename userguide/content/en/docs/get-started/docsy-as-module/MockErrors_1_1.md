---
weight: 2
date: '2025-06-12'
title: Mockerrors 1 1
aliases:
- /docs/MockErrors_1_1/
description: ''
linkTitle: Mockerrors 1 1
type: docs
---

# MockErrors

Undici exposes a variety of mock error objects that you can use to enhance your mock error handling.
You can find all the mock error objects inside the `mockErrors` key.

```js
import { mockErrors } from 'undici'
```

| Mock Error            | Mock Error Codes                | Description                                                |
| --------------------- | ------------------------------- | ---------------------------------------------------------- |
| `MockNotMatchedError` | `UND_MOCK_ERR_MOCK_NOT_MATCHED` | The request does not match any registered mock dispatches. |
