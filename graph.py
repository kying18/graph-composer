class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.adjacent = {}  # nodes that it points to
        self.probability_map = []

    def __str__(self):
        return self.value + ' '.join([node.value for node in self.adjacent.keys()])

    def add_edge_to(self, vertex, weight=0):
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_adjacent_nodes(self):
        return self.adjacent.keys()

    # initializes probability map
    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.probability_map.extend([vertex for _ in range(weight)])


class Graph(object):
    def __init__(self):
        self.vertices = {}

    def get_vertex_values(self):
        return set(self.vertices.keys())

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()

    # def add_edge(self, start, end, weight=0):
    #     # start and end are values of the nodes, not node objects
    #     self.vertices[start].add_edge_to(self.vertices[end], weight)
    #
    # def increment_edge(self, start, end):
    #     self.vertices[start]
