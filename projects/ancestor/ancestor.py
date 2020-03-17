class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 not in self.vertices or v2 not in self.vertices:
            raise IndexError("One or both vertices do not exist")
        else:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)        

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
    # initialize the graph
    g = Graph()

    # loop over ancestors list...
    for k, v in ancestors:
        # add key in tuple at current index as vertex in graph
        g.add_vertex(k)
        # add value in tuple at current index as vertex in graph
        g.add_vertex(v)
        # add edges between appropriate vertices in graph by passing the key of tuple at current index as vertex1 and value as vertex2 
        g.add_edge(k, v)
    return g    
    
test_g = earliest_ancestor(test_ancestors, 0)
for v in test_g.vertices:
    print(v, test_g.vertices[v])