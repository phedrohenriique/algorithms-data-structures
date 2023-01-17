
# each item has its own array of neighbors
# below is the list of airport routes and airports

airports = ["PHX","LAX","JFK","OKC","HEL","LOS","MEX","BKK","LIM","EZE","LAP"]
routes = [
    ['PHX','LAX'],
    ['PHX', 'JFK'],
    ['JFK', 'OKC'],
    ['JFK','HEL'],
    ['JFK', 'LOS'],
    ['MEX', 'LAX'],
    ['MEX','BKK'],
    ['MEX','LIM'],
    ['MEX','EZE'],
    ['LIM','BKK'] 
]

# to solve the problem we shall create a gryph,
# for that we shall  see all the routes for each airport
# that means the airports are NODES(VERTICES) and routes are LIMITS(EDGES)

adjacency_list = dict()

# first a function to return all the main nodes

def add_node(node):

    """
    nodes are added through each consideration of the problem,
    it creates a dictionary for the nodes as key
    """

    adjacency_list.update({f"{node}":[]})

# secondly we add all nodes possible connections

def add_edge(edges):

    """  
    edges are added through each consideration of the problem
    there shall be a looping through both parts of the array
    """
    # you have to update the dictionary with key value pairs in both sides,
    # since there is a connection from both nodes the list will
    # iterate through the quantity of nodes and update them accordingly

    for edge in edges:
        connection = adjacency_list.get(edge[0])
        connection.append(edge[1])
        adjacency_list.update({f"{edge[0]}":connection})

        connection = adjacency_list.get(edge[1])
        connection.append(edge[0])
        adjacency_list.update({f"{edge[1]}":connection})

def creating_graph():

    for airport in airports:
        add_node(airport)

    add_edge(routes)
    print("Adjacency List from Graph : ", adjacency_list)

def bfs_algorithm(start_node, end_node):

    """
    using the queue technic we search for all te nodes,
    it is represented by an array with the nodes
    """

    queue = [start_node]
    checked_node_list = list()
    checked_node_list.append(start_node)

    solution_paths=[] # needs to store the dictionaries
    current_path=[start_node]

    ## this function will create a path to be seeing at the end
    
    while len(queue) > 0 :

        # checks the nodes and add to control checked list
        # checks the nodes

        checking_node = queue[0]
        neigbour_nodes = adjacency_list.get(checking_node)
        queue.remove(queue[0])

        for node in neigbour_nodes: # checking neighbour nodes

            # if node is the one we want print

            if node == end_node:
                print( node ,'found the route')
                solution_paths.append(current_path + [node])
                

            # if not is not what we want add to the queue
            # and to the checked so the node was visited

            if node not in checked_node_list : 
                
                checked_node_list.append(node)
                queue.append(node)

                if node == end_node:
                    pass
                else:
                    current_path.append(node)
                    print(node)

def bfs(start, goal, adjacency_list):
    # Queue for storing the paths
    queue = [[start]]
    path_list = []
    
    # Set for storing the visited nodes
    visited = set()

    # Iterate until the queue is empty
    while queue:
        # Get the first path in the queue
        path = queue.pop(0)
        
        # Get the last node in the path
        node = path[-1] # since the path puts together the nodes it get the last one, wich is -1
        
        # Check if the node is the goal
        if node == goal:
            # Return the path if it is

            # for path in path_list:
            #     print(path)
            #     if goal in path:
            #         print("Route : ",path)
            #         return path    
            return path
        
        # Mark the node as visited
        visited.add(node)
        
        # Get the neighbors of the node
        neighbors = adjacency_list[node]
        
        # Iterate over the neighbors
        for neighbor in neighbors:
            # Check if the neighbor has been visited
            if neighbor not in visited:
                # Create a new path with the neighbor appended to it
                new_path = list(path)
                new_path.append(neighbor)
                # Add the new path to the queue
                queue.append(new_path)
                path_list.append(new_path)

def bfs_allpaths(start, goal, adjacency_list):
    # Queue for storing the paths
    queue = [[start]]

    path_list = []
    solution_list = []
    
    # Set for storing the visited nodes
    visited = set()

    # Iterate until the queue is empty
    while queue:
        # Get the first path in the queue
        path = queue.pop(0)
        
        # Get the last node in the path
        node = path[-1] # since the path puts together the nodes it get the last one, wich is -1
        
        # Check if the node is the goal
        # if node == goal:
        #     # Return the path if it is

        #     # for path in path_list:
        #     #     print(path)
        #     #     if goal in path:
        #     #         print("Route : ",path)
        #     #         return path    
        #     return path
        
        # Mark the node as visited
        visited.add(node)
        
        # Get the neighbors of the node
        neighbors = adjacency_list[node]
        
        # Iterate over the neighbors
        for neighbor in neighbors:
            # Check if the neighbor has been visited
            if neighbor not in visited:
                # Create a new path with the neighbor appended to it
                new_path = list(path)
                new_path.append(neighbor)
                # Add the new path to the queue
                queue.append(new_path)
                path_list.append(new_path)

    for path in path_list:

        if path[-1] == goal:
            print("Possible Solution : ", path)
            solution_list.append(path)

    return solution_list

def dfs_allpaths(start_node,end_node ,checked_nodes = set(), path = []):

    print(start_node)
    checked_nodes.add(start_node)
    neighbours_nodes = adjacency_list[start_node]
    path.append(start_node)


    for node in neighbours_nodes:

        if node == end_node:
            print(node)
            print('Destinaton Found : ', node)
            path.append(node)
            print(path)
            return

        if node not in checked_nodes:
            dfs_allpaths(node, end_node)


    ###########################################################
    # dfs algorithm working below

    # print(start_node)
    # checked_nodes.add(start_node)
    # neighbours_nodes = adjacency_list[start_node]

    # for node in neighbours_nodes:

    #     if node == end_node:
    #         print('Destinaton Found : ', node);
    #         return

    #     if node not in checked_nodes:
    #         dfs_allpaths(node, end_node)

    
    # needs to use a recursive function

    # queue = [[start_node]]
    # path_list = []
    # path = queue.pop(0)
    # node = path[-1] # getting last node from path
    # checked_nodes.add(node) # adding node to the checked nodes

    #list = adjacency_list[node]

      
    

if __name__ == "__main__":
    print("starting script")
    creating_graph(),
    #print(bfs_algorithm("PHX", "BKK")) # this should print the list of solution paths
    #print("Solution of Graph : ", bfs("PHX", "BKK", adjacency_list))
    #print("Solution of Graph : ", bfs_allpaths("PHX", "BKK", adjacency_list))
    print("Solution of Graph : ", dfs_allpaths("PHX", "BKK"))

    