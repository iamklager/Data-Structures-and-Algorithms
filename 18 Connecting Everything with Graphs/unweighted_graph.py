class WeightedGraphVertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = {}
    
    def add_adjacent_vertex(self, vertex, weight):
        self.adjacent_vertices[vertex] = weight

def dijkstra_shortest_path(start_vertex, end_vertex):
    lowest_weight_table = {}
    lowest_previous_stopover_vertex_table = {}
    unvisited_vertices = []
    visited_vertices = {}
    lowest_weight_table[start_vertex.value] = 0
    current_vertex = start_vertex
    
    while current_vertex is not None:
        visited_vertices[current_vertex.value] = True
        
        if current_vertex in unvisited_vertices:
            unvisited_vertices = [vert for vert in unvisited_vertices if vert != current_vertex]
        
        for v in current_vertex.adjacent_vertices:
            if v.value not in visited_vertices:
                unvisited_vertices.append(v)
            weight_through_current_vertex = lowest_weight_table[current_vertex.value] + current_vertex.adjacent_vertices[v]
                
            if (v.value not in lowest_weight_table) or (weight_through_current_vertex < lowest_weight_table[v.value]):
                lowest_weight_table[v.value] = weight_through_current_vertex
                lowest_previous_stopover_vertex_table[v.value] = current_vertex.value
        
        if len(unvisited_vertices) == 0:
            current_vertex = None
        else:
            adj_vert_keys = [vert.value for vert in unvisited_vertices]
            next_vert_val = min(adj_vert_keys, key = lambda k: lowest_weight_table[k])
            current_vertex = next((vert for vert in unvisited_vertices if vert.value == next_vert_val), None)
        
    shortest_path = []
    current_vertex_value = end_vertex.value
    
    while current_vertex_value != start_vertex.value:
        shortest_path.append(current_vertex_value)
        current_vertex_value = lowest_previous_stopover_vertex_table[current_vertex_value]
    shortest_path.append(start_vertex.value)

    return shortest_path[::-1]


atlanta = WeightedGraphVertex("Atlanta")
boston  = WeightedGraphVertex("Boston")
chicago = WeightedGraphVertex("Chicago")
denver  = WeightedGraphVertex("Denver")
el_paso = WeightedGraphVertex("El Paso")

atlanta.add_adjacent_vertex(boston,  100)
atlanta.add_adjacent_vertex(denver,  160)
boston.add_adjacent_vertex(chicago,  120)
boston.add_adjacent_vertex(denver,   180)
chicago.add_adjacent_vertex(el_paso,  80)
denver.add_adjacent_vertex(chicago,   40)
denver.add_adjacent_vertex(el_paso,  140)
el_paso.add_adjacent_vertex(boston,  100)

print(dijkstra_shortest_path(atlanta, el_paso))

