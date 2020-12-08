class Vertex:
    # value
    # connection stored as an adjacency list
    def __init__(self, value):
        self.value = value
        self.connections = {}
        
    # displaying the graph as string?
    def __str__(self):
        return f" {self.value} connections: {[v.value for v in self.connections]}"
    
    # add a connection?
    def add_connection(self, vert, weight = 0):
        self.connection[vert] = weight

    # display the connections
    def get_connections(self):
        return self.connections.keys()

    # display / get the value
    def get_value(self):
        return self.value

    # a possible get weight
    def get_weight(self, weight):
        return self.connections[vert]


# Graph contains vertices
class Graph:
    # init
    def __init__(self):
        # dictionary of vertices
        self.vertices = {}
        # keep track of size
        self.count = 0

    def __contains__(self, value):
        return vert in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    # add a vertex
    def add_vertex(self, value):
        # increment size or count
        self.count += 1
        # set a new vertex as vertex object and wrap the value
        new_vert = Vertex(value)
        # set the vertices at key of value to the value of the new vert
        self.vertices[value] = new_vert
        # return the new vert
        return new_vert

    # add edge?
    def add_edge(self, vert1, vert2, weight=0):
        # check if vert1 is not in the graph
        if vert1 not in self.vertices:
            # add vert1 to the graph
            self.add_vertex(vert1)
        # check if vert2 is not in the graph
        if vert2 not in self.vertices:
            # add vert1 to the graph
            self.add_vertex(vert2)
        
        # add a connection from vert1 to vert2 pass in a weight
        self.vertices[vert1].add_connection(self.vertices[vert2], weight)

    # get vertices?
    def get_vertices(self):
        return self.vertices.keys()


 


g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_edge("A", "B", 1)
g.add_edge("B", "C", 3)
g.add_edge("B", "D", 2)
g.add_edge("E", "D", 1)
# g.add_edge("A", "B", 1)
# g.add_edge("A", "B", 1)
# g.add_edge("A", "B", 1)


g.print_matrix()

print("------")

g.add_vertex()

g.print_matrix()