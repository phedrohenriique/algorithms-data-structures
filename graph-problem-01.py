
# each item has its own array of neighbors
# below is the list of airport routes and airports

airports = ["PHX","LAX","JFK","OKC","HEL","LOS","MEX","BKK","LIM","EZE"]
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

# now to solve the problem we shall create a gryph,
# for that we shall  see all the routes for each airport
# that means the airports are NODES(VERTICES) and routes are LIMITS(EDGES)

adjacency_list = dict()

def add_node(airport):
    """
    nodes are added through each consideration of the problem
    """
    adjacency_list.update({f"{airport}":[]})

def add_edge(origin, destination):
    """ 
    edges are added through each consideration of the problem
    there shall be a looping through both parts of the array
    """
    for destiny in adjacency_list:
        if(adjacency_list.get(origin)):
            adjacency_list.update({f"{origin}":destination})


def creating_graph(adjacency_list):
    graph = []
    for edges in routes:

        pass


if __name__ == "__main__":
    print("starting script")

    for airport in airports:
        add_node(airport)
    
    print(adjacency_list)
    