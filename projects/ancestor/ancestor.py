from util import Stack, Queue  # These may come in handy
from graph import Graph

#ancestors is a list of tuples that specifies parent child relationships
#DFS and return the last item in the path
def earliest_ancestor(ancestors, starting_node):
        #create an instance of the graph class
        graph = Graph()

        #go through each tuple in the ancestors list
        #CREATE GRAPH IN REVERSE --- THIS IS KEY
        for ancestor in ancestors:
            #check for the first item in each tuple which indicates the parent
            #if it is not already there, make it into a vertex
            if ancestor[0] not in graph.vertices:
                graph.add_vertex(ancestor[0])
            #check for the second item in the tuple which indicates the child
            #if it is not already there, make it into a vertex
            if ancestor[1] not in graph.vertices:
                graph.add_vertex(ancestor[1])
            #if they both exist, then add ancestor[1] pointing to ancestor[0] - CHILD POINTS TO PARENT
            #create graph in reverse
            graph.add_edge(ancestor[1], ancestor[0])

        #If the input individual has no parents, the function should return -1
        if graph.vertices[starting_node] == set():
            return -1
        else:
            #create a queue FOR BFS
            queue = Queue()

        #Add THE STARTING VERTEX TO A PATH (LIST) BEFORE ADDING IT to the queue
        queue.enqueue([starting_node])

        #create a set to store the visited nodes
        visited = set()     

        #keep track of paths to find the longest path
        path_tracker = {}

        #index to be used to add items to the path tracker dictionary
        index = 0            

        #while the stack is not empty
        while queue.size() > 0:

            # dequeue, the first PATH
            path = queue.dequeue()

            #if there is data in path_tracker
            if path_tracker:
                #find the length of the the path that was just dequeued from the front of queue
                current_path_length = len(path)

                #only keeping one other item in the path tracker dictionary
                #so find it's length
                stored_path_length = len(path_tracker[0])

                #If there is more than one ancestor tied for "earliest", 
                # return the one with the lowest numeric ID. 
                #check if the new path is the same length as the path in the path tracker dictionary
                if current_path_length == stored_path_length:
                    #if it is equal, store the last item from the current path in path_last
                    path_last = path[-1]

                    #retrieve the list from path tacker
                    other_path_list = path_tracker[0]

                    #store the last item from the list that was in path tracker in other_path_last
                    other_path_last = other_path_list[-1]

                    #check to see which one is the lowest number and add it's associated path to path tracker
                    if path_last < other_path_last:
                        path_tracker[index] = path    
                    else:
                        path_tracker[index] = other_path_list                   

                #check if the new path's length is greater than the length of the path in the path 
                #tracker dictionary
                elif current_path_length > stored_path_length:
                    path_tracker[index] = path                

            #if there is no data in path tracker
            #add the new path
            else:
                path_tracker[index] = path

            # GRAB THE LAST VERTEX FROM THE PATH
            last_vertex = path[-1]

            #check if it's been visited
            if last_vertex not in visited:
            # If it has not been visited...
                # Mark it as visited
                visited.add(last_vertex)

                # Then add A PATH TO all neighbors to the back of the queue                                                     
                for neighbor in graph.get_neighbors(last_vertex):
                    #(Make a copy of the path before adding)  
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    queue.enqueue(path_copy)
    
        #increment the index
        #i didn't end up using this because i am only storing one list in the path tracker dictionary 
        index = index + 1

        #at this point the only item in path tracker is the longest path
        longest_path = path_tracker[0]
        #remove the last item in path_tracker
        earliest_ancestor = longest_path[-1]
        #and return it
        return earliest_ancestor



        
