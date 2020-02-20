import random
from util import Stack, Queue  # These may come in handy

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    #add vertexes
    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        #add a user as a vertex/node
        self.users[self.last_id] = User(name)
        #create a friendship node associated with the user with an empty set(no friends assigned)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        # Create friendships
        # create a list with all possible friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))


        # Shuffle the list
        random.shuffle(possible_friendships)
        print("----")
        print(possible_friendships)
        print("----")
        # Grab the first N pairs from the list and create those friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        # avg_friendships = total_friendships / num_users
        # total_friendships = avg_friendships * num_users
        # N = avg_friendships * num_users // 2

    #use a BFS
    #associate the list of friends with 1 key
    #friend's id is the key and the value is the path with all users in that user's extended network with
    #the shortest friendship path between them
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        #store visited nodes
        visited = {}  # Note that this is a dictionary, not a set 
        # !!!! IMPLEMENT ME

        #create an empty queue
        queue = Queue()

        # Add THE STARTING VERTEX TO A PATH BEFORE ADDING IT to the queue
        #use a list as our path, for our path the order does matter
        queue.enqueue([user_id])         

        #index to be used to add items to the visited dictionary
        index = 0   

        #While the queue is not empty...
        while queue.size() > 0:
            #remove the first path from the queue
            #list with user/friend ids
            path = queue.dequeue()  

            # GRAB THE LAST VERTEX FROM THE PATH
            #this is going to be the friend id
            last_friend_id = path[-1]         

            # Check if it's been visited 
            if last_friend_id  not in visited:
            # If it has not been visited...
                # add the path to the visited dictionary
                visited[last_friend_id ] = path
       

                # Then add A PATH of all friends of last_friend_id to the back of the queue
                for friend_id in self.friendships[last_friend_id]:
                     #(Make a copy of the path before adding)  
                    path_copy = path.copy()
                    path_copy.append(friend_id)
                    queue.enqueue(path_copy)       


        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.users)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
