"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

#***dft/dfs uses stacks because they are LIFO and bft/bfs uses queues because they are FIFO***
#***TO GO FROM A TRAVERSAL TO A SEARCH. ADD THE STARTING VERTEX TO A PATH(LIST) BEFORE ADDING IT TO THE 
# QUEUE/STACK***

#undirected graphs are two way connections between each node, can go from A to B but also B to A
#directed graphs have directions assigned to each edge, can go from A to B but not B to A
#weighted graphs have numbers assigned to each edge
#unweighted graphs do not have numbers assigned to each edge
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    #a way of storing the connections
    #each key is the name of the vertex(node) and the value for each key is an array with the associated edges
    def __init__(self):
        #stores the relationships between the vertices and the edges
        self.vertices = {}

    #a vertex is a node or one of the circles
    #before we can draw the connections we need to add the nodes
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """       
        #sets have no duplicates, have to be unique
        # unordered so order doesn't matter
        # 0(1) or very fast
        # sets are just hash tables underneath the hood without keys 
        if vertex_id in self.vertices:
            print("WARNING: That vertex already exists")
        else:
            self.vertices[vertex_id] = set()

    #an edge is the connection between the nodes
    #relationship between vertices
    #to add an edge we need the two vertices
    #it should find in the self.vertices dictionary, the key of v1 and push v2 into that dictionary
    #and then find in the self.vertices dictionary, the key of v2 and push v1 into that dictionary
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        #if v1 and v2 are vertexes or nodes
        #add a directed or one way edge
        #.add is how we add something to a set
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """        
        #find vertex_id in the dictionary and return all it's values
        return self.vertices[vertex_id]

    #visit neighbors at current depth first before moving downwards or visiting neighbors of neighbors
    #accepts a starting vertex
    #memorize the algorithm
    #traversal is to visit each node
    #search is to find a particular value or path
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        """
        BFT ALGORITHM
        # Create an empty queue
        # Add the starting vertex to the queue
        # Create an empty set to store visited nodes
        # While the queue is not empty...
            # Dequeue, the first vertex (remove from the front)
            # Check if it's been visited
            # If it has not been visited...
                # Mark it as visited
                # Then add all neighbors to the back of the queue
        """
        #create a queue and place the starting vertex in it
        queue = Queue()
        queue.enqueue(starting_vertex)

        #create a set to store the visited nodes
        visited = set()       
       
        #loop as long as there is anything in the queue
        #while the queue is not empty
        while queue.size() > 0:
            #remove/shift the first vertex from the queue
            currentVertex = queue.dequeue()

            #if it is not inside the set that stores visited nodes
            if currentVertex not in visited:
                #print the vertex
                print(currentVertex)

                #and add it into the set that store nodes visited
                visited.add(currentVertex)

                 #Then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(currentVertex):          
                    #and enqueue/add that vertex to the queue                
                    queue.enqueue(neighbor)    

            print()#extra line for formatting purposes    
        
    #explore as far as possible down one branch before backtracking
    #there is no root node. pick one neighbor of a given node and continue to follow the neighbors of that node 
    #before we visit its siblings. always choose the lowest number as our next item to visit
    #depth first traversal
    #should accept a starting node or vertex
    #changing our queue to a stack changes our bft to a dft because queue is FIFO and stack is LIFO
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        """
        DFT ALGORITHM
        # Create an empty stack
        # Push the starting vertex to the stack
        # Create an empty set to store visited nodes
        # While the stack is not empty...
            # Pop, the first vertex (remove from the back)
            # Check if it's been visited
            # If it has not been visited...
                # Mark it as visited
                # Then push all neighbors to the back of the stack
        """

        #create an empty stack
        stack = Stack()

        # Push the starting vertex to the stack
        stack.push(starting_vertex)

        # Create an empty set to store visited vertices
        visited = set()       

        #while the stack has something in it
        #use the stack's size method
        while stack.size() > 0:
            #pop the next vertex from the stack
            currentVertex = stack.pop()

            #if that vertex hasn't been visited yet
            if currentVertex not in visited:
                #print the current vertex
                print(currentVertex)

                #mark it as visited
                visited.add(currentVertex)

                #push all of its neighbors on to the stack
                for neighbor in self.get_neighbors(currentVertex):
                    stack.push(neighbor)        

        print()#extra line for formatting purposes

    #the function should accept a starting node
    #traverse is to visit each node     
    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        """
        DFT RECURSIVE ALGORITHM
        # check if the node is visited
        # if not...
            # mark it as visited
            # print
            # call dft_recursive on each child            
        """

        #create a set to store visited vertices if one has not been created yet
        if visited is None:
            visited = set()       

        #add the starting vertex to visited
        visited.add(starting_vertex)  

        #and print the vertex
        print(starting_vertex)     
        
        #loop over all the values in the adjency list for that vertex
        for neighbor in self.get_neighbors(starting_vertex):
            #if the value has not been visited, 
            if neighbor not in visited:
                #recursively call dft_recursive on that vertex(neighbor)
                self.dft_recursive(neighbor, visited)      
       

    #a search is to check each node and only return the thing or path you are looking for
    #a path extends from the starting node to the ending node
    #checks everything that's one step away, then two steps away, then three steps away, etc.
    #TO GO FROM A TRAVERSAL TO A SEARCH. ADD THE STARTING VERTEX TO A PATH(LIST) BEFORE ADDING IT TO THE QUEUE/STACK
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        """
        BFS ALGORITHM
        # Create an empty queue
        # Add THE STARTING VERTEX TO A PATH (LIST) BEFORE ADDING IT to the queue
        # Create an empty set to store visited nodes
        # While the queue is not empty...
            # Dequeue, the first PATH
            # GRAB THE LAST VERTEX FROM THE PATH
            # CHECK IF IT'S THE TARGET
                # IF SO, RETURN THE PATH
            # Check if it's been visited
            # If it has not been visited...
                # Mark it as visited
                # Then add A PATH TO all neighbors to the back of the queue
                    # (Make a copy of the path before adding)
        """
        #create an empty queue
        queue = Queue()

        # Add THE STARTING VERTEX TO A PATH BEFORE ADDING IT to the queue
        #use a list as our path
        queue.enqueue([starting_vertex])

        #Create an empty set to store visited nodes
        visited = set()

        #While the queue is not empty...
        while queue.size() > 0:
            # Dequeue, the first PATH
            path = queue.dequeue()

            # GRAB THE LAST VERTEX FROM THE PATH
            last_vertex = path[-1]

            # CHECK IF IT'S THE TARGET           
            if last_vertex == destination_vertex:
                # IF SO, RETURN THE PATH
                return path

            # Check if it's been visited 
            if last_vertex not in visited:
            # If it has not been visited...
                # Mark it as visited
                visited.add(last_vertex)

                # Then add A PATH TO all neighbors to the back of the queue                                                     
                for neighbor in self.get_neighbors(last_vertex):
                     #(Make a copy of the path before adding)  
                    new_path = list(path) 
                    new_path.append(neighbor)
                    queue.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        """
        BFS ALGORITHM
        # Create an empty stack
        # Add THE STARTING VERTEX TO A PATH (LIST) BEFORE ADDING IT to the stack
        # Create an empty set to store visited nodes
        # While the stack is not empty...
            # Pop, the last PATH
            # GRAB THE LAST VERTEX FROM THE PATH
            # CHECK IF IT'S THE TARGET
                # IF SO, RETURN THE PATH
            # Check if it's been visited
            # If it has not been visited...
                # Mark it as visited
                # Then add A PATH TO all neighbors to the back of the stack
                    # (Make a copy of the path before adding)
        """
        #Create an empty stack
        stack = Stack()

        #Add THE STARTING VERTEX TO A PATH (LIST) BEFORE ADDING IT to the stack
        stack.push([starting_vertex])

        #Create an empty set to store visited nodes
        visited = set()

        # While the stack is not empty...
        while stack.size() > 0:
            # Pop, the last PATH
            last_path = stack.pop()

            # GRAB THE LAST VERTEX FROM THE PATH
            last_vertex = last_path[-1]

            # CHECK IF IT'S THE TARGET
            if last_vertex == destination_vertex:                
                # IF SO, RETURN THE PATH
                return last_path

            # Check if it's been visited
            # If it has not been visited...
            if last_vertex not in visited:
                # Mark it as visited
                visited.add(last_vertex)           
                
                # Then add A PATH TO all neighbors to the back of the stack                   
                for neighbor in self.get_neighbors(last_vertex):
                    #(Make a copy of the path before adding)  
                    new_path = list(last_path) 
                    new_path.append(neighbor)
                    stack.push(new_path)


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
    #print(graph.dfs_recursive(1, 6))
