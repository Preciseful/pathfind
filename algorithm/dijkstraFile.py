
from collections import defaultdict
import math
from collections import OrderedDict
import string


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

    # String represntation
	def __str__(self):
		return '<%s, %s, %s>' % (self.x, self.y, self.z)

	# Produce a copy of itself
	def __copy(self):
		return Vector(self.x, self.y, self.z)

	# Signing
	def __neg__(self):
		return Vector(-self.x, -self.y, -self.z)

	# Scalar Multiplication
	def __mul__(self, number):
		return Vector(self.x * number, self.y * number, self.z * number)

	def __rmul__(self, number):
		return self.__mul__(number)

	# Division
	def __div__(self, number):
		return self.__copy() * (number**-1)

	# Arithmetic Operations
	def __add__(self, operand):
		return Vector(self.x + operand.x, self.y + operand.y, self.z + operand.z)


	def __sub__(self, operand):
		return self.__copy() + -operand

	# Cross product
	# cross = a ** b
	def __pow__(self, operand):
		return Vector(self.y*operand.z - self.z*operand.y, 
			                self.z*operand.x - self.x*operand.z, 
			                self.z*operand.y - self.y*operand.x)

	# Dot Project
	# dp = a & b
	def __and__(self, operand):
		return (self.x * operand.x) + \
		       (self.y * operand.y) + \
		       (self.z * operand.z)
 
	# Operations

	def normal(self):
		return self.__copy() / self.magnitude()

	def magnitude(self):
		return (self.x**2 + self.y**2 + self.z**2)**(.5)

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
    overwatch_graph[initial][end] = path[1];
    return path


import MainFile

graph = Graph()

nodePOS = MainFile.nodePOS

connections = MainFile.connections

v = len(nodePOS)
overwatch_graph = [[0 for x in range(v)] for y in range(v)]

for i in range(v):
    for t in connections[i]:
        graph.add_edge(i, t, distance(nodePOS[i], nodePOS[t]))

for i in range(v):
        for t in range(v):
            if(i != t):
                dijsktra(graph, i, t)
            else:
                overwatch_graph[i][t] = 999;

stringgraph = ["" for y in range(v)]
secondgraph = stringgraph
encoded = []


unusedalpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáçèéêëìíîïð!@#$%^&*()-_=+[{]};:<,>.?/~`€ƒ‰Œ•"
alphabet = unusedalpha[0:v+1]

for i in range(v):
    tempstring = ""
    
    for t in overwatch_graph[i]:
        if(t == 999):
            tempstring = tempstring + " "
        else:
            tempstring = tempstring + alphabet[t]

    stringgraph[i] = tempstring

stringgraph = str(stringgraph)

stringgraph = stringgraph.replace("[", "Array(")
stringgraph = stringgraph.replace("]", ")")
secondgraph = stringgraph
secondgraph = stringgraph.replace("Array(", "").replace(")", "")
secondgraph = secondgraph.split(",")

for i in range(len(secondgraph)):
    secondgraph[i] = secondgraph[i].replace("'", '")')
    secondgraph[i] = secondgraph[i].replace('")', 'Custom String("', 1)

secondgraph = str(secondgraph)
secondgraph = secondgraph.replace("[", "Array(")
secondgraph = secondgraph.replace("]", ")")
secondgraph = str(secondgraph)

secondgraph = secondgraph.replace("'", "")
print(secondgraph)
    



print("\n\n\n\nOver")
pyperclip.copy("actions\n{\n    Global.stringmap = " + secondgraph + ';\n    Global.alphabet = Custom String("' + alphabet + '");\n}')

