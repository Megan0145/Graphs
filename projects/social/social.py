import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        self.count = 0

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
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
        self.count = 0
        # !!!! IMPLEMENT ME

        # Add users
        # loop in range 0 -> number of users..
        for i in range(num_users):
            # add new user on each iteration, their name will be an f-string with the current index within loop concatenated
            self.add_user(f'User {i}')
        # Create friendships
        # declare list to hold all possible friendship combinations
        possible_friendship_combos = []
        # iterate over users..
        for user_id in self.users:
            # iterate over users again in a range from user id + 1 to last id + 1...
            for friend_id in range(user_id + 1, self.last_id + 1):
                # add tuple to possible_friendship_combos list containing the user id and friend id
                possible_friendship_combos.append((user_id, friend_id))
        
        # shuffle the possible_friendship_combos to randomise it
        random.shuffle(possible_friendship_combos)

        # the number of friendships to generate can be calculated by multiplying the number of users by the average number of 
        # friendships per user and floor dividing in half (because friendships are biderectional -> ie each time add_friendship() 
        # called it creates two friendships)
        num_friendships_to_gen = num_users * avg_friendships // 2

        # loop in range num_friendships_to_generate...
        for i in range(num_friendships_to_gen):
            # add friendship for tuple at current index of possible_friendship_combos
            self.add_friendship(possible_friendship_combos[i][0], possible_friendship_combos[i][1])
            self.count += 1

    def optimised_populate_graph(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
 
        for i in range(num_users):
            self.add_user(f'User {i}')

        num_friendships_to_gen = num_users * avg_friendships // 2
        curr_num_friendships = 0

        while curr_num_friendships < num_friendships_to_gen:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            add_friends = self.add_friendship(user_id, friend_id)
            if add_friends is True:    
                curr_num_friendships += 1
               

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # instantiate new queue
        q = Queue()
        # add path list containing user_id to queue (starting node)
        q.enqueue([user_id])
        # while the queue is not empty..
        while q.size() > 0:
            # dequeue the path at the top of the queue
            path = q.dequeue()
            # the next user id to visit will be the last element in the path list at the top of the queue
            next_user_id = path[-1]
            # if the next_user_id has not been visited...
            if next_user_id not in visited:
                # add it to visited set with the user_id as the key and the path as the value
                visited[next_user_id] = path
                # if friends of next_user_id have not been visited..
                for friend_id in self.friendships[next_user_id]:
                    if friend_id not in visited:
                        # copy contents of current path to new list
                        new_path = list(path)
                        # append the id of the friend
                        new_path.append(friend_id)
                        # add it to the queue
                        q.enqueue(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.optimised_populate_graph(10,2)
    print(sg.friendships)