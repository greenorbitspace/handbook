---
weight: 2
date: '2025-06-12'
title: 1 Express 1 1
aliases:
- /docs/1-express_1_1/
description: ''
linkTitle: 1 Express 1 1
type: docs
---

### install
```bash
cd myApp
npm init
npm install express
```

### createServer
```js
const express = require('express')
const app = express()
const port = 300

app.get('/', (req, res) => {
    res.send('Hello World')
})

app.listen(port, () => {
    console.log("listening...")
})
```
> [!NOTE]
> The req (request) and res (response) are the exact same objects that Node provides, so you can invoke req.pipe(), req.on('data', callback), and anything else you would do without Express involved.

### run app
```bash
node app.js
```