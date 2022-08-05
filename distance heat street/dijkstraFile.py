
from collections import defaultdict
import itertools
import math


import pyperclip


def Array(*content): 
    return list(content)

class Vector:
	x = 0
	y = 0
	z = 0

	def __init__(self, x, y, z):
		self.x = float(x)
		self.y = float(y)
		self.z = float(z)

	
def distance(self, operand):
        return round(math.sqrt((self.x - operand.x)**2 + (self.y - operand.y)**2 + (self.z - operand.z)**2), 0)




class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        if(from_node in connections[to_node] and to_node in connections[from_node]):
            self.edges[from_node].append(to_node)
            self.weights[(from_node, to_node)] = weight
            self.edges[to_node].append(from_node)
            self.weights[(to_node, from_node)] = weight
        else:
            self.edges[from_node].append(to_node)
            self.weights[(from_node, to_node)] = weight
            
def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])
 

def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]

    return path


import MainFile


graph = Graph()

nodePOS = MainFile.nodePOS

connections = MainFile.connections

distance_matrix = ["" for y in range(128 * 8)]
count = 0

v = len(nodePOS)


for i in range(v):
    for t in connections[i]:
        graph.add_edge(i, t, distance(nodePOS[i], nodePOS[t]))



unusedalpha = "0123456789!?#$%"


for i in range(v):
        for t in range(v):
            distance_matrix[count] = distance_matrix[count].__add__(str(unusedalpha[len(dijsktra(graph, i, t)) - 1]))
            if(len(distance_matrix[count]) == 128):
                count += 1

distance_matrix = str(distance_matrix)

distance_matrix = distance_matrix.replace(", ''", "")

print(str(distance_matrix))
    
print("\n\n\n\nOver")

pyperclip.copy("\n" + "distance_matrix = " + str(distance_matrix))

