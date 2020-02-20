from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

#unexplored rooms have a ?
#visited rooms have a direction filled in

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"

#map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

#this statment in world.py (self.starting_room = self.rooms[0]) sets starting_room to rooms[0]
player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    #a way of storing the connections
    #each key is the name of the vertex(node) and the value for each key is an array with the associated edges
    def __init__(self):
        #stores the relationships between the vertices and the edges
        #creates a hash table called rooms to store the nodes and their connected edges
        self.rooms = {}

    #a vertex is a node or one of the circles
    #before we can draw the connections we need to add the nodes
    def add_room(self, room_id):
        """
        Add a vertex to the graph.
        """       
        #sets have no duplicates, have to be unique
        # unordered so order doesn't matter
        # 0(1) or very fast
        # sets are just hash tables underneath the hood without keys 
        if room_id in self.rooms:
            print("WARNING: That room already exists")
        else:
            #adding a directed edge
            self.rooms[room_id] = set()

    #add pathway is entering a direction
    def add_pathway(self, room1, room2):
        """
        Add a directed edge to the graph.
        """
        #if v1 and v2 are vertexes or nodes
        #add a directed or one way edge
        #.add is how we add something to a set
        if room1 == room2:
            print("WARNING: You cannot add a pathway that leads from your current room back to your current room")
        elif room1 in self.rooms and room2 in self.vertices:
            self.rooms[room1].add(room2)
            self.rooms[room2].add(room1)            
        else:
            raise IndexError("That room does not exist")        


    def get_neighbors(self, room_id):
        """
        Get all neighbors (edges) of a vertex.
        """        
        #find vertex_id in the dictionary and return all it's values
        return self.rooms[room_id]


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

#write a traversal method


#for every direction in traversal_path = [n, s, e, w]
for move in traversal_path:
    #call the travel method in player.py
    player.travel(move)

    #player.current room will be upated after with either the room in that direction or an error message
    #after a call to player.travel
    #add the new current room to visited_rooms set
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
