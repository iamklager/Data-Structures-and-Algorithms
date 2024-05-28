# Chapter 18

## Exercise 04

In this chapter, I only provided the code for breadth-first traversal, as discussed in Breadth-First Search, on page 348. That is, the code simply printed the value of each vertex. Modify the code so that it performs an actual search for a vertex value provided to the function. (We did this for depth-first search.) That is, if the function finds the vertex it's searching for, it should return that vertex's value. Otherwise, it should return null.

```python
class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []
    
    def add_adjacent_vertex(self, vertex):
        if vertex in self.adjacent_vertices:
            return None
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex(self)

def bfs(vertex, search_value, visited_vertices = {}):
    queue = []
    visited_vertices = {}
    visited_vertices[vertex.value] = True
    queue.append(vertex)
    while len(queue) > 0:
        current_vertex = queue.pop(0)
        if current_vertex.value == search_value:
            return current_vertex
        for v in current_vertex.adjacent_vertices:
            if v.value not in visited_vertices:
                visited_vertices[v.value] = True
                queue.append(v)


alice = Vertex("alice")
bob = Vertex("bob")
candy = Vertex("candy")
derek = Vertex("derek")
elaine = Vertex("elaine")
fred = Vertex("fred")
gina = Vertex("gina")
helen = Vertex("helen")
irena = Vertex("irena")

alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(candy)
alice.add_adjacent_vertex(derek)
alice.add_adjacent_vertex(elaine)
bob.add_adjacent_vertex(fred)
derek.add_adjacent_vertex(elaine)
derek.add_adjacent_vertex(gina)
fred.add_adjacent_vertex(helen)
gina.add_adjacent_vertex(irena)

print(bfs(alice, "gina").value)
```

