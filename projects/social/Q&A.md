## QUESTION ONE:
To create 100 users with an average of 10 friends each, how many times would you need to call add_friendship()? Why?

add_friendship() would be called 500 times. 
We are using a formula to generate the number of friendships that should be generated when populating the graph with users and frienships. 
The number of friendships to be generated will be the result of:
        number of users * average number of friendships per user // 2
Which in this case is:
        100 * 10 // 2
        = 500        


## QUESTION TWO:
If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended 
social network? What is the average degree of separation between a user and those in his/her extended network?

# A: Percentage of other users in a particular user's extended social network:
```python
    # instantiate the graph
    sg = SocialGraph()
    # populate it with 1000 users with an average of 5 friendships per user
    sg.populate_graph(1000, 5)
    # generate a random user id between 0 and 1000 (total number of users)
    rnd_user_id = random.randint(0, 1000)
    # get the social paths for all connections in the random user's extended social network
    connections = sg.get_all_social_paths(rnd_user_id)
    # save the number of people in the random user's extended social network to variable
    # this can be calculated by getting the length of the connections dictionary that holds all social paths for that user and minusing 1 (we dont want to include that user themselves)
    num_friends = len(connections) - 1
    # the percentage of other users in the user's network can be obtained by dividing num_friends by the total number of users (1000 in this case) and multiplying by 100
    percentage_users_in_network = num_friends/1000 * 100
    print(f"Percentage of other users in user's network: {percentage_users_in_network}%")
```
The above code produces 99.2% as the average percentage of other users in a user's network for a social network of 1000 users with an average of 5 friendships per user.

# B: Degree of Seperation:
The average degree of separation between a user and those in his/her extended network can be obtained by iterating over the connections in 
their extended social network. This is a dictionary with the id of the friend as the key and a list containing the shortest path to that friend within
the graph. For example:
    User has id of 3
    Their extended social network may look like this:
       {3: [3], 1: [3, 1], 2: [3, 2], 4: [3, 1, 4]}
    So the shortest path to their friend with the id of 1 is [3, 1]: they have a friendship with a degree of seperation of 1.
    Thinking about this in terms of vertices in the graph; if we are at the vertex with the id of 3, we don't have to pass through any other
    vertices to get to the vertex with the id of 1. It's a direct relationship with only one edge.
    The friendship that they have with the user with the id of 4 has a degree of seperation of 2:
        Shortest path = [3, 1, 4] -> they have to pass through vertex with id of 1 to get to vertex with id of 4 (user 4 is a friend of a friend)
    
Therefore the degree of seperation between any user and another can be calculated by minusing 1 from the length of the shortest path between them.
In the above example for user 3:
    - Degree of seperation from user 1:
        len([3, 1]) - 1 
        = 1     
    - Degree of seperation from user 2:
        len([3, 2]) - 1 
        = 1     
    - Degree of seperation from user 3:
        len([3]) - 1 
        = 0 (current user)         
    - Degree of seperation from user 4:
        len([3, 1, 4]) - 1 
        = 2     

```python
    # initalise graph
    sg = SocialGraph()
    # populate it with 1000 users and an average of 5 friendships per user
    sg.populate_graph(1000, 5)
    # generate random user id
    rnd_user_id = random.randint(0, 1000)
    # get all social paths for user with random user id 
    connections = sg.get_all_social_paths(rnd_user_id)
    # initalise the average degree of seperation to be 0
    avg_deg_of_sep = 0
    # iterate over connections dictionary..
    for friend_id in connections:
        # check that id of the user at the current position in the connections dictionary is not the random user id (we don't care about the degree of seperation between the current user and themselves)
        if friend_id != rnd_user_id:
            # add the length of the path - 1 at current index to avg_deg_of_sep variable
            avg_deg_of_sep += (len(connections[friend_id]) - 1)
    # divide value of average degree of seperation by the length of connections minus one        
    avg_deg_of_sep = avg_deg_of_sep // (len(connections) - 1)        
    # print
    print(avg_deg_of_sep)
```

The above code produces an average degree of seperation of 4 for a social network of 1000 users with an average of 5 friendships per user.