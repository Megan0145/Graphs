"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # add empty set to the vertices dictionary with the key of the vertex_id passed in
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # firstly check that the vertices being passed in exist in the vertices dictionary
        if v1 not in self.vertices or v2 not in self.vertices:
            # raise error if so
            raise IndexError("One or both vertices do not exist")
        # else add the edge: add v2 to the v1 set in vertices
        else:
            self.vertices[v1].add(v2)
            # add v1 to the v2 set in vertices in order to make the edge bidirectional
            # self.vertices[v2].add(v1)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # simply return the set with given vertex_id within the vertices dictionary
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # firstly instantiate a Queue
        q = Queue()      
        # add the starting_vertex to the queue
        q.enqueue(starting_vertex)
        # instantiate empty set to hold visited vertices
        visited = set ()
        # while the length of the queue is more than zero
        while q.size() > 0:
            # set vert equal to the first item in the queue
            vert = q.dequeue()
            # check if the vertex has been visited before
            if vert not in visited:
                # if not, add it to visited
                visited.add(vert)
                print(vert)
                # for every child vertex of vert
                for child_vert in self.vertices[vert]:
                    # add the child vertex to the queue
                    q.enqueue(child_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # firstly instantiate a Stack
        s = Stack()      
        # add the starting_vertex to the stack
        s.push(starting_vertex)
        # instantiate empty set to hold visited vertices
        visited = set ()
        # while the length of the stack is more than zero
        while s.size() > 0:
            # set vert equal to the last (most recent) item in the stack
            vert = s.pop()
            # check if the vertex has been visited before
            if vert not in visited:
                # if not, add it to visited
                visited.add(vert)
                print(vert)
                # for every child vertex of vert
                for child_vert in self.vertices[vert]:
                    # add the child vertex to the stack
                    s.push(child_vert)
        

    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # print the starting_vertex
        print(starting_vertex)
        # add it to the visited set (will be defaulted to empty set on first pass)
        visited.add(starting_vertex)
        # for every adjacent vertex of starting_vert
        for adjacent_vert in self.vertices[starting_vertex]:
            # check if the vertex has been visited before
            if adjacent_vert not in visited:
                # if not, recur function passing in adjacent_vert as the starting_vertex and the current contents visited set
                self.dft_recursive(adjacent_vert, visited)
                

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # firstly instantiate a Queue
        q = Queue()      
        # add a list containing the starting_vertex to the queue
        q.enqueue([starting_vertex])
        # instantiate empty set to hold visited vertices
        visited = set ()
        # while the length of the queue is more than zero
        while q.size() > 0:
            # set path equal to the first item in the queue (this will be a list containing all vertices within the current route)
            path = q.dequeue()
            # get the last element within the path list
            vert = path[-1]
            # check if the vertex has been visited before
            if vert not in visited:
                # if it is equal to the destination_vertex, we have reached our destination and can return the path
                if vert == destination_vertex:
                    return path
                # else, add it to visited
                visited.add(vert)
                # for every adjacent vertex of vert
                for adj_vert in self.vertices[vert]:
                    # copy the contents of the current path into new path and append the adjacent vertex
                    next_path = list(path)
                    next_path.append(adj_vert)
                    # add the new path to the queue
                    q.enqueue(next_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
