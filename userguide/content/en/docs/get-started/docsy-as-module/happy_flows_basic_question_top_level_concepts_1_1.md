---
weight: 2
date: '2025-06-12'
title: Happy Flows Basic Question Top Level Concepts 1 1
aliases:
- /docs/happy_flows_basic_question_top_level_concepts_1_1/
description: ''
linkTitle: Happy Flows Basic Question Top Level Concepts 1 1
type: docs
---

## "Hello! What can you do?"

I am a user who is asking about the bots capabilities

```mermaid
sequenceDiagram
    box Frontend
    participant UI
    end
    box Main backend logic
    participant Director
    end
    UI -->> Director: Hello! What can you do?
    Director -->> Director: Return pure-LLM response
    Director -->> UI: I'm InferESG and can...
```
