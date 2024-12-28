# Graph Algorithms and Data Structures Study Guide

## Introduction to Graph Algorithms

A **graph** consists of **vertices (V)** and **edges (E)**, which can be of two types:

- **Undirected Graph**: Edges go both ways between vertices.
- **Directed Graph**: Edges go in a specific direction from one vertex to another.

### Representations

1. **Adjacency Matrix**:
   - A 2D matrix where `G[i][j] = 1` if an edge exists from vertex `i` to `j`.
   - Space Complexity: \( O(V^2) \).

2. **Adjacency List**:
   - A list where each vertex points to a list of adjacent vertices.
   - Space Complexity: \( O(V + E) \).

#### Choosing the Representation:
- **Sparse Graph** (\( E << V \)): Adjacency List is better.
- **Dense Graph** (\( E \approx V^2 \)): Adjacency Matrix is preferred.

---

## Depth First Search (DFS)

DFS explores as far as possible along each branch before backtracking. It uses a **stack** (implicitly via recursion).

### Pseudocode for `explore(v)`:
```python
Function explore(v):
    visited(v) ← true
    for (v, x) ∈ E do
        if ¬visited(x) then
            explore(x)
```
## Breadth First Search (BFS)

BFS explores vertices level by level. It uses a queue.

```python
Function BFS(G = (V, E), root):
    q ← Queue
    dist ← {}
    enqueue(q, root)
    while q is not empty do:
        v ← dequeue(q)
        for (v, w) ∈ E do:
            if w ∉ dist then:
                enqueue(q, w)
                dist[w] ← dist[v] + 1
    return dist
```
## Dijkstra’s Algorithm

Finds the shortest paths from a source to all vertices in a weighted graph.
Uses a Priority Queue to track the closest vertex
Updates distances iteratively for all neighbors

```python
Function Dijkstra(G, weights, root):
    seen ← PriorityQueue(V)
    dist ← {}
    while seen is not empty do:
        curr ← PopMin(seen)
        for (curr, w) ∈ E do:
            alt ← dist[curr] + weight[curr, w]
            if alt < dist[w] then:
                dist[w] ← alt
                DecKey(seen, w, alt)
    return dist
```
Runtime: O((V+E)log(V)) 

## Mininum Spanning Tree (MST)

An MST connects all vertices in a graph with the minimum total edge weight.

- Kruskal's Algorithm
  1. Sort edges by weight
  2. Add edge to the MST unless they form a cycle
  3. Use a Union-Find Data Structure for cycle detection

  Runtime: O(Elog(E) + Elog(V))
    
- Prim's Algorithm
  1. Start from any vertex
  2. Add the smallest edge connecting the MST to a new vertex
  3. Use a Priority Queue to track edge weights 

  Runtime: O((V+E)log(V))

## Union-Find Data Structure

efficiently supports: 
  1. Find(x): find the root of the component containing x
  2. Union(x,y): Merge two components

Optimizations; 
  - Path Compression
  - Union by Rank

Runtime: O(log(n)) 

## Bellman-Ford Algorithm

Finds the shortest path from a single source vertex to all other vertices in a weighted graph. Unlike Dijkstra's algorithm, it works with graphs that have negative weight edges.

### Key Characteristics:
- Handles negative edge weights.
- Detects negative weight cycles in the graph.
- Slower than Dijkstra’s algorithm (\(O(VE)\)).

### Pseudocode:
```python
Function BellmanFord(G, source):
    dist ← {v: ∞ for v in V}
    dist[source] ← 0

    for i in range(len(V) - 1):  # Relax all edges |V| - 1 times
        for (u, v, weight) in E:
            if dist[u] + weight < dist[v]:
                dist[v] ← dist[u] + weight

    for (u, v, weight) in E:  # Check for negative weight cycles
        if dist[u] + weight < dist[v]:
            return "Negative weight cycle detected"

    return dist
```
Runtime: O(VE)

## Floyd-Warshall Algorithm

Calculates the shortest paths between all pairs of vertices in a weighted graph.

### Key Characteristics:
- Works with both positive and negative weights.
- Cannot handle graphs with negative weight cycles.
- Computes all-pairs shortest paths.

### Pseudocode:
```python
Function FloydWarshall(G):
    dist ← 2D array initialized with ∞
    for v in V:
        dist[v][v] ← 0
    for (u, v, weight) in E:
        dist[u][v] ← weight

    for k in V:  # Iterate through all intermediate nodes
        for i in V:
            for j in V:
                dist[i][j] ← min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
```
Runtime: O(V<sup>3</sup>)




