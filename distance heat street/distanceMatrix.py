from calendar import c
from collections import defaultdict
import math
from queue import Queue



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

	
def distanceBetween(self, operand):
        return round(math.sqrt((self.x - operand.x)**2 + (self.y - operand.y)**2 + (self.z - operand.z)**2), 0)


intmax=9999999999 
class Graph:
    # Constructor
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)
		
        # Directed or Undirected
        self.m_directed = directed
		
        # Graph representation - Adjacency list
        # We use a dictionary to implement an adjacency list
        self.m_adj_list = {node: set() for node in self.m_nodes}      
	
    # Add edge to the graph
    def add_edge(self, node1, node2, weight=1):
        self.m_adj_list[node1].add((node2, weight))

        if not self.m_directed:
            self.m_adj_list[node2].add((node1, weight))
    
    # Print the graph representation
    def print_adj_list(self):
      for key in self.m_adj_list.keys():
        print("node", key, ": ", self.m_adj_list[key])

    def bfs(self, start_node, target_node):
    # Set of visited nodes to prevent loops
        visited = set()
        queue = Queue()

        # Add the start_node to the queue and visited list
        queue.put(start_node)
        visited.add(start_node)
        
        # start_node has not parents
        parent = dict()
        parent[start_node] = None

        # Perform step 3
        path_found = False
        while not queue.empty():
            current_node = queue.get()
            if current_node == target_node:
                path_found = True
                break

            for (next_node, weight) in self.m_adj_list[current_node]:
                if next_node not in visited:
                    queue.put(next_node)
                    parent[next_node] = current_node
                    visited.add(next_node)
                    
        # Path reconstruction
        path = []
        if path_found:
            path.append(target_node)
            while parent[target_node] is not None:
                path.append(parent[target_node]) 
                target_node = parent[target_node]
            path.reverse()
        return path 



# Driver program

import MainFile


nodePOS = MainFile.nodePOS

connections = MainFile.connections

distance_matrix = ["" for y in range(128 * 10)]

count = 0

v = len(nodePOS)

unusedalpha = "0123456789!?#$%&*{}"

graph = Graph(v)

for i in range(v):
    for t in connections[i]:
        graph.add_edge(i, t)

for i in range(v):
    for t in range(v):
        path = []
        path = graph.bfs(i, t)
        distance_matrix[count] += unusedalpha[len(path) - 1]
        if(len(distance_matrix[count]) == 128):
            count += 1



distance_matrix = str(distance_matrix)

distance_matrix = distance_matrix.replace(", ''", "")

distance_matrix = distance_matrix.replace("[", "Array(")
distance_matrix = distance_matrix.replace("]", ")")
secondgraph = distance_matrix
secondgraph = distance_matrix.replace("Array(", "").replace(")", "")
secondgraph = secondgraph.split(",")

for i in range(len(secondgraph)):
    secondgraph[i] = secondgraph[i].replace("'", '")')
    secondgraph[i] = secondgraph[i].replace('")', 'Custom String("', 1)

secondgraph = str(secondgraph)
secondgraph = secondgraph.replace("[", "Array(")
secondgraph = secondgraph.replace("]", ")")
secondgraph = str(secondgraph)

secondgraph = secondgraph.replace("'", "")

distance_matrix = secondgraph

print(str(distance_matrix))
    
print("\n\n\n\nOver")

pyperclip.copy("actions{\n" + "Global.distance_matrix = " + str(distance_matrix) + ";\n}")
