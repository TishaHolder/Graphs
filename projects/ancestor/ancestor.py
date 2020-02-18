from util import Stack, Queue  # These may come in handy
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
        graph = Graph()

        for ancestor in ancestors:
            if ancestor[0] not in graph.vertices:
                graph.add_vertex(ancestor[0])
            if ancestor[1] not in graph.vertices:
                graph.add_vertex(ancestor[1])
            graph.add_edge(ancestor[1], ancestor[0])

        #If the input individual has no parents, the function should return -1
        if graph.vertices[starting_node] == set():
            return -1
        else:
            #create a queue
            queue = Queue()

        #add the starting vertex to the queue
        queue.enqueue([starting_node])

        #create a set to store the visited nodes
        visited = set()  

        #set the starting_node as the oldest_ancestor
        oldest_ancestor = starting_node

        current_length = 0

        #while the queue is not empty
        while queue.size() > 0:
            # Dequeue, the first PATH
            path = queue.dequeue()

            # GRAB THE LAST VERTEX FROM THE PATH
            last_vertex = path[-1]



        
