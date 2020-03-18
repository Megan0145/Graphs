class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
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

def earliest_ancestor(ancestors, starting_node):
    # initialize the graph
    g = Graph()

    # loop over ancestors list...
    for k, v  in ancestors:
        # add key in tuple at current index as vertex in graph
        g.add_vertex(k)
        # add value in tuple at current index as vertex in graph
        g.add_vertex(v)
        # add edges between appropriate vertices in graph by passing the key of tuple at current index as vertex1 and value as vertex2 
        g.add_edge(v, k)

    # use BFT to traverse graph from starting node and find the earliest ancestor ->
    # initalize queue
    q = Queue()
    # enqueue a list containing the starting node
    q.enqueue([starting_node])
    # set a max path length to 1
    max_path_length = 1
    # set an initial earliest ancestor 
    # (defaulted to -1 because if there is no earliest ancestor it should return -1 )
    earliest_ancestor = -1
    # while the queue is not empty...
    while q.size() > 0 :
        # remove the first path list from queue
        path = q.dequeue()
        # set vert equal to the id of the last vert in the path list
        vert = path[-1]
        # if the length of the path longer/equal to the max_path length and the vertex is less than the current value of earliest_ancestor
        # OR the length of the current path is more than the max_path_length
        if (len(path) >= max_path_length and vert < earliest_ancestor) or (len(path) > max_path_length):
            # set the earliest_ancestor equal to the vertex
            earliest_ancestor = vert
            # set the max_path_length equal to the length of the current path
            max_path_length = len(path)
        # for every neighbour of the current vertex..    
        for neighbour in g.get_neighbors(vert):
            # copy the contents of the current path to a new path list
            new_path = list(path)
            # append the neighbour vertex to it
            new_path.append(neighbour)
            # and add to the queue
            q.enqueue(new_path)
    # return the earliest ancestor        
    return earliest_ancestor        
