# Chapter 18

## Exercise 05

Write a function that accepts two vertices from a graph and returns the shortest path between them. The function should return the shortest path between them.

*Hint:* The algorithm may contain elements of both breadth-first search and Dijkstra's algorithm.

```python
def shortest_path(start_vertex, end_vertex, visited_vertices = {}):
    queue = []
    previous_vertex_table = {}
    visited_vertices[start_vertex.value] = True
    queue.append(start_vertex)
    while len(queue) > 0:
        current_vertex = queue.pop(0)
        for v in current_vertex.adjacent_vertices:
            if v.value not in visited_vertices:
                visited_vertices[v.value] = True
                queue.append(v)
                previous_vertex_table[v.value] = current_vertex.value
        if end_vertex in visited_vertices:
            break
    shortest_path = []
    current_vertex_value = end_vertex.value
    while current_vertex_value != start_vertex.value:
        shortest_path.append(current_vertex_value)
        current_vertex_value = previous_vertex_table[current_vertex_value]
    shortest_path.append(start_vertex.value)
    return shortest_path[::-1]
```

