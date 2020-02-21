from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"

map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

#print the room graph dictionary for testing purposes
#print(room_graph)

# Print an ASCII map
#world.print_rooms()

#this statment in world.py (self.starting_room = self.rooms[0]) sets starting_room to the first room rooms[0]
#puts the player in the first room
player = Player(world.starting_room)

#make the first room the current room
current_room = world.starting_room

#You may find the following commands useful:
#player.current_room.id - returns current room id, 
#player.current_room.get_exits - every exit in the current_room.get_exits() that leads somewhere 
#player.travel(direction) - if there is a room in the selected direction change current room to that room 

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#empty set to store visited rooms
visited = set()

#dictionary with regular directions
directions = {"north": "n", "south": "s", "east": "e", "west": "w"} 

#dictionary with opposite directions
opposite_directions = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}        

#create an empty stack
stack = Stack()

#place player in the first room
player.current_room = world.starting_room

#add the first room to the visited set
visited.add(player.current_room.id)

visited_rooms = set()

#move from room to room while there are unexplored rooms
#You start in room 0, which contains exits ['n', 's', 'w', 'e']
while len(visited) != len(room_graph):
    visited_rooms.add(current_room)

    
    #the exits for a room will contain either [n, s, e, or w] but not necessarily all of them
    #only the exits that lead to somewhere 
    #get all the exits for the current room    
    exits = current_room.get_exits()   
  
    #choose a random direction to move from the exits list               
    #direction_to_move = random.choice(exits)   
        
   
    #if the current room is not in visited
    if current_room.id not in visited:
        #add it to the visited set
        visited.add(current_room.id) 

    #reverse_direction = opposite_directions.get(direction_to_move)    
           

    #if there is a w in the list of valid exits for a room
    #check if there is a room in that direction and if was already visited
    if "w" in exits and current_room.get_room_in_direction("w") not in visited_rooms:

            #add it to the stack to keep track of directions
            stack.push("w")

            #if it wasn't already visited add the direction to traversal_path
            traversal_path.append("w")

            #go in that direction
            #if there is a room in the selected direction 
            #player.current_room.get_room_in_direction(direction_to_move) will 
            #change current room to that room           
            current_room = current_room.get_room_in_direction("w")  
       
            #now the loop will iterate with the new player.current_room.id
    elif "s" in exits and current_room.get_room_in_direction("s") not in visited_rooms:

            #add it to the stack to keep track of directions
            stack.push("s")

            #if it wasn't already visited add the direction to traversal_path
            traversal_path.append("s")

            #go in that direction
            #if there is a room in the selected direction 
            #player.current_room.get_room_in_direction(direction_to_move) will 
            #change current room to that room           
            current_room = current_room.get_room_in_direction("s")  
       
            #now the loop will iterate with the new player.current_room.id
    elif "n" in exits and current_room.get_room_in_direction("n") not in visited_rooms:

            #add it to the stack to keep track of directions
            stack.push("n")

            #if it wasn't already visited add the direction to traversal_path
            traversal_path.append("n")

            #go in that direction
            #if there is a room in the selected direction 
            #player.current_room.get_room_in_direction(direction_to_move) will 
            #change current room to that room           
            current_room = current_room.get_room_in_direction("n")  
       
            #now the loop will iterate with the new player.current_room.id

    #if the direction was already visited
    elif "e" in exits and current_room.get_room_in_direction("e") not in visited_rooms:

            #add it to the stack to keep track of directions
            stack.push("e")

            #if it wasn't already visited add the direction to traversal_path
            traversal_path.append("e")

            #go in that direction
            #if there is a room in the selected direction 
            #player.current_room.get_room_in_direction(direction_to_move) will 
            #change current room to that room           
            current_room = current_room.get_room_in_direction("e")  
       
            #now the loop will iterate with the new player.current_room.id    

    #if a "?" was found
    else:
            #remove the last valid direction from the stack        
            direction_to_move = stack.pop()

            #and get the reverse direction from the oppoite_directions dictionary
            reverse_direction = opposite_directions.get(direction_to_move)

            #add the reverse direction to traversal_path
            traversal_path.append(reverse_direction)

            #change current room to back to the previous or opposite room          
            current_room = current_room.get_room_in_direction(reverse_direction) 
        
    

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

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
"""player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")"""



