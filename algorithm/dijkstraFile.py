from collections import defaultdict
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

def vectstr(self):
	return  str("Vector(" + str(self.x) + ", " + str(self.y) + ", " + str(self.x) + ")")

def distance(self, operand):
        return round(math.sqrt((self.x - operand.x)**2 + (self.y - operand.y)**2 + (self.z - operand.z)**2), 0)




class Graph():
    def __init__(self):

        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        if(from_node in connections[to_node] and to_node in connections[from_node]):
            self.edges[from_node].append(to_node)
            self.weights[(from_node, to_node)] = weight
            self.edges[to_node].append(from_node)
            self.weights[(to_node, from_node)] = weight
        else:
            self.edges[from_node].append(to_node)
            self.weights[(from_node, to_node)] = weight
            
 

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

graph1 = ["" for y in range(v)]
graphinstring = graph1
finalgraph2 = graph1


unusedalpha = "23456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿ"
alphabet = unusedalpha[0:v+1]

for i in range(v):
    tempstring = ""
    
    for t in overwatch_graph[i]:
        if(t == 999):
            tempstring += " "
        else:
            tempstring += alphabet[t]

    if v > 128:
        finalgraph2[i] = tempstring[128:]
        graph1[i] = tempstring[0:128]
    else:
        graph1[i] = tempstring
        

graph1 = str(graph1)

graph1 = graph1.replace("[", "Array(")
graph1 = graph1.replace("]", ")")
graphinstring = graph1
graphinstring = graph1.replace("Array(", "").replace(")", "")
graphinstring = graphinstring.split(",")

for i in range(len(graphinstring)):
    graphinstring[i] = graphinstring[i].replace("'", '")')
    graphinstring[i] = graphinstring[i].replace('")', 'Custom String("', 1)

graphinstring = str(graphinstring)
graphinstring = graphinstring.replace("[", "Array(")
graphinstring = graphinstring.replace("]", ")")
graphinstring = str(graphinstring)

graphinstring = graphinstring.replace("'", "")
graph1 = graphinstring

print(graph1)

secondPOS = "";

if(v > 128):   
    finalgraph2 = str(finalgraph2) 
    graphinstring = ["" for y in range(v)]

    finalgraph2 = finalgraph2.replace("[", "Array(")
    finalgraph2 = finalgraph2.replace("]", ")")
    graphinstring = finalgraph2
    graphinstring = finalgraph2.replace("Array(", "").replace(")", "")
    graphinstring = graphinstring.split(",")

    for i in range(len(graphinstring)):
        graphinstring[i] = graphinstring[i].replace("'", '")')
        graphinstring[i] = graphinstring[i].replace('")', 'Custom String("', 1)

    graphinstring = str(graphinstring)
    graphinstring = graphinstring.replace("[", "Array(")
    graphinstring = graphinstring.replace("]", ")")
    graphinstring = str(graphinstring)

    graphinstring = graphinstring.replace("'", "")
    finalgraph2 = graphinstring
    print("graph2\n" + graphinstring)


for i in range(v):
    if(i != v - 1):
        secondPOS += vectstr(nodePOS[i]) + ", "
    else:
        secondPOS += vectstr(nodePOS[i])

secondPOS = "Array(" + secondPOS + ");"

    
print("\n\n\n\nOver")

if(v > 128):
    pyperclip.copy("actions\n{\n    Global.graph = " + graph1 + ";\n    Global.graph1 = " + finalgraph2 + ';\n    Global.alphabet = Custom String("' + alphabet + '");\n' + 
    "    Global.nodePOS = " + secondPOS + "\n}")

else:   
    pyperclip.copy("actions\n{\n    Global.graph = " + graph1 + ';\n    Global.alphabet = Custom String("' + alphabet + '");\n' + 
    "    Global.nodePOS = " + secondPOS + "\n}")