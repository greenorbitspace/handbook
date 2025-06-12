---
weight: 2
date: '2025-06-12'
title: 28 Crypto 1 1
aliases:
- /docs/28-crypto_1_1/
description: ''
linkTitle: 28 Crypto 1 1
type: docs
---

### crypto module
- provides cryptograph functionalities and use libuv threads pool for some of its method

```js
const crypto = require("node: crypto")
// password based key derivation function 2
// one of the popular ways to hash passwords bfore storing them
// it is a cpu consuming method and is offload to libuv
crypto.pbkdf2
```