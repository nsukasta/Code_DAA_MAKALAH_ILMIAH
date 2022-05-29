import sys
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        """
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        """
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes

    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]


nodes = [
    "A1",
    "A2",
    "A3",
    "A4",
    "A5",
    "A6",
    "A7",
    "A8",
    "A9",
    "A10",
    "A11",
    "A12",
    "A13",
    "A14",
    "A15",
    "A16",
    "A17",
    "A18",
    "A19",
    "A20",
    "A21",
    "A22",
]

init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph["A1"]["A2"] = 525
init_graph["A1"]["A8"] = 1700
init_graph["A8"]["A10"] = 500
init_graph["A8"]["A9"] = 360
init_graph["A9"]["A11"] = 370
init_graph["A10"]["A11"] = 420
init_graph["A11"]["A12"] = 690
init_graph["A12"]["A13"] = 220
init_graph["A12"]["A6"] = 1000
init_graph["A2"]["A3"] = 660
init_graph["A3"]["A4"] = 565
init_graph["A3"]["A6"] = 230
init_graph["A6"]["A7"] = 450
init_graph["A7"]["A13"] = 840
init_graph["A4"]["A7"] = 90
init_graph["A4"]["A5"] = 310
init_graph["A5"]["A16"] = 640
init_graph["A16"]["A14"] = 320
init_graph["A13"]["A14"] = 320
init_graph["A14"]["A19"] = 680
init_graph["A5"]["A15"] = 760
init_graph["A15"]["A21"] = 1400
init_graph["A16"]["A17"] = 360
init_graph["A17"]["A18"] = 390
init_graph["A18"]["A19"] = 425
init_graph["A19"]["A20"] = 300
init_graph["A20"]["A21"] = 155
init_graph["A21"]["A22"] = 320


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    
    path.append(start_node)

    print(
        "Rute terbaik dengan total jarak sekitar {} meter.".format(
            shortest_path[target_node]
        )
    )
    print(" -> ".join(reversed(path)))


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())

    
    shortest_path = {}

    
    previous_nodes = {}

   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value

    
    shortest_path[start_node] = 0

    
    while unvisited_nodes:
       
        current_min_node = None
        for node in unvisited_nodes:  
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(
                current_min_node, neighbor
            )
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
               
                previous_nodes[neighbor] = current_min_node

        
        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


graph = Graph(nodes, init_graph)
previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="A1")
print_result(previous_nodes, shortest_path, start_node="A1", target_node="A22")
