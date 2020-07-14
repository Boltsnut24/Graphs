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
        #this is just an empty vertex, we must add edges still
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        
        #if not self.vertices[v2]:
        #    print(F'{v2} is not a vertice currently')
        #    return
        #elif not self.vertices[v1] == None:
        #    print(F'{v1} is not a vertice currently')
        #    return

        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        #uses a queue
        start = starting_vertex
        q = Queue()
        q.enqueue(starting_vertex)

        visited = set()

        while q.size() > 0:

            #deq current
            current = q.dequeue()
            #add current vertex to visited if it isn't already there
            if current not in visited:
                print(current)
                visited.add(current)

                #add all neighbors to q
                for vert in self.get_neighbors(current):
                    q.enqueue(vert)
            

    def dft(self, starting_vertex):
        #uses a stack
        start = starting_vertex
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:

            #pop current
            current = s.pop()
            #add current vertex to visited if it isn't already there
            if current not in visited:
                print(current)
                visited.add(current)

                #add all neighbors to q
                for vert in self.get_neighbors(current):
                    s.push(vert)

    def dft_recursive(self, starting_vertex, visited_nodes=set()):
        curr = starting_vertex
        print(curr)
        if curr not in visited_nodes:
            visited_nodes.add(curr)

            for vert in self.get_neighbors(curr):
                if vert not in visited_nodes:
                    self.dft_recursive(vert)
                

    def bfs(self, starting_vertex, destination_vertex):
        
        start = starting_vertex
        q = Queue()
        q.enqueue([starting_vertex])

        while q.size() > 0:
            current_path = q.dequeue()
            if current_path[-1] == destination_vertex:
                return current_path

            for vert in self.get_neighbors(current_path[-1]):
                
                new_path = [*current_path, vert]
                q.enqueue(new_path)
                
    def dfs(self, starting_vertex, destination_vertex):
        start = starting_vertex
        s = Stack()
        s.push([starting_vertex])

        while s.size() > 0:
            current_path = s.pop()
            if current_path[-1] == destination_vertex:
                return current_path

            for vert in self.get_neighbors(current_path[-1]):
                
                new_path = [*current_path, vert]
                s.push(new_path)

    def dfs_recursive(self, vertex, destination_vertex, path=[], visited=set()):

        visited.add(vertex)
        ## check if it's our target node, if so return
        if vertex == destination_vertex:
            return path
            
        if len(path) == 0:
            path.append(vertex)
        
        ## iterate over neighbors
        neighbors = self.get_neighbors(vertex)
        ### check if visited
        for neighbor in neighbors:
            if neighbor not in visited: 
        #### if not, recurse with a path
                result = self.dfs_recursive(neighbor, destination_vertex, path + [neighbor], visited)
        ##### if this recursion returns a path,
                if result is not None:
            ###### return from here
                    return result


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
    graph.add_edge(6, 1)
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
    print(graph.get_neighbors(2))

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
