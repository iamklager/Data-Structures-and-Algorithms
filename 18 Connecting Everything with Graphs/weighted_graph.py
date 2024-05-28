class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []
    
    def add_adjacent_vertex(self, vertex):
        if vertex in self.adjacent_vertices:
            return None
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex(self)
    
def dfs_traverse(vertex, visited_vertices = {}):
    visited_vertices[vertex.value] = True
    print(vertex.value) # printing vertex value to check if it works
    for v in vertex.adjacent_vertices:
        if v.value in visited_vertices:
            continue
        dfs_traverse(v, visited_vertices)
        
def dfs(vertex, search_value, visited_vertices = {}):
    if vertex.value == search_value:
        return vertex
    visited_vertices[vertex.value] = True
    for v in vertex.adjacent_vertices:
        if v.value in visited_vertices:
            continue
        if v.value == search_value:
            return v
        searched_for_vertex = dfs(v, search_value, visited_vertices)
        if searched_for_vertex is not None:
            return searched_for_vertex 
    return None

def bfs_traverse(starting_vertex):
    queue = []
    visited_vertices = {}
    visited_vertices[starting_vertex.value] = True
    queue.append(starting_vertex)
    while len(queue) > 0:
        current_vertex = queue.pop(0)
        print(current_vertex.value)
        
        for v in current_vertex.adjacent_vertices:
            if v.value not in visited_vertices:
                visited_vertices[v.value] = True
                queue.append(v)

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

print(shortest_path(alice, irena))
