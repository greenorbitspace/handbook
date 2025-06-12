---
weight: 2
date: '2025-06-12'
title: Poolstats 1 1
aliases:
- /docs/PoolStats_1_1/
description: ''
linkTitle: Poolstats 1 1
type: docs
---

# Class: PoolStats

Aggregate stats for a [Pool](Pool.md) or [BalancedPool](BalancedPool.md).

## `new PoolStats(pool)`

Arguments:

* **pool** `Pool` - Pool or BalancedPool from which to return stats.

## Instance Properties

### `PoolStats.connected`

Number of open socket connections in this pool.

### `PoolStats.free`

Number of open socket connections in this pool that do not have an active request.

### `PoolStats.pending`

Number of pending requests across all clients in this pool.

### `PoolStats.queued`

Number of queued requests across all clients in this pool.

### `PoolStats.running`

Number of currently active requests across all clients in this pool.

### `PoolStats.size`

Number of active, pending, or queued requests across all clients in this pool.
