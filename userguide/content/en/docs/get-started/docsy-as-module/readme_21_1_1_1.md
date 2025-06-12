---
weight: 2
date: '2025-06-12'
title: Readme 21 1 1 1
aliases:
- /docs/readme_21_1_1_1/
description: ''
linkTitle: Readme 21 1 1 1
type: docs
---

# array-union

> Create an array of unique values, in order, from the input arrays

## Install

```
$ npm install array-union
```

## Usage

```js
import arrayUnion from 'array-union';

arrayUnion([1, 1, 2, 3], [2, 3]);
//=> [1, 2, 3]

arrayUnion(['foo', 'foo', 'bar']);
//=> ['foo', 'bar']

arrayUnion(['🐱', '🦄', '🐻'], ['🦄', '🌈']);
//=> ['🐱', '🦄', '🐻', '🌈']

arrayUnion(['🐱', '🦄'], ['🐻', '🦄'], ['🐶', '🌈', '🌈']);
//=> ['🐱', '🦄', '🐻', '🐶', '🌈']
```

---

<div align="center">
	<b>
		<a href="https://tidelift.com/subscription/pkg/npm-array-union?utm_source=npm-array-union&utm_medium=referral&utm_campaign=readme">Get professional support for this package with a Tidelift subscription</a>
	</b>
	<br>
	<sub>
		Tidelift helps make open source sustainable for maintainers while giving companies<br>assurances about security, maintenance, and licensing for their dependencies.
	</sub>
</div>
