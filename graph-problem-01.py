
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
    
    # print(adjacency_list)

    add_edge(routes)
    print(adjacency_list)

if __name__ == "__main__":
    print("starting script")
    creating_graph()

    