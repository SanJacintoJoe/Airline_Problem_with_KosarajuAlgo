import sys


def graph_build(edges, reverse):
    graph = {}
    index_one = 1 if reverse else 0
    index_two = 0 if reverse else 1

    for edge in edges:
        if edge[index_one] not in graph:
            graph[edge[index_one]] = [0, False, []]
        if edge[index_two] not in graph:
            graph[edge[index_two]] = [0, False, []]

    for edge in edges:
        graph[edge[index_one]][2].append(edge[index_two])
    return graph


time = 0
def DFSrev(graph, node):
    global time
    graph[node][1] = True
    for arc in graph[node][2]:
        if not graph[arc][1]:
            DFSrev(graph, arc)

    time += 1
    graph[node][0] = time

    return graph


def First_Pass(graph):
    keys = list(graph.keys())
    keys = sorted(keys, reverse=True)

    for i in keys:
        if not graph[i][1]:
            graph = DFSrev(graph, i)

    return graph


def edge_array_w_finishing_times(edges):
    new_edges = []
    for edge in edges:
        start = edge[0]
        end = edge[1]
        new_edges.append((start, end))
    return new_edges


def DFS(graph, node, s):
    graph[node][1] = True
    graph[node][0] = s
    for arc in graph[node][2]:
        if not graph[arc][1]:
            DFS(graph, arc, s)

    return graph


def Second_Pass(graph):
    leaders = []
    keys = list(graph.keys())
    keys = sorted(keys, reverse=True)
    for i in keys:
        if not graph[i][1]:
            s = i
            leaders.append(s)
            graph = DFS(graph, i, s)

    return graph, leaders


edgeList = [("LAX", "SOF"), ("LAX", "SEA"), ("SEA", "IAH"), ("ORD", "LGA"), ("ORD", "DEN"), ("ORD", "ALT"), ("HW", "SOF"),
            ("ALT", "ORD"), ("SOF", "LAX"), ("PHX", "DEN"), ("DEN", "IAH"), ("IAH", "SOF"), ("LAX", "HW"), ("HK", "HW"), ("HK", "JP"), ("JP","HW"), ("LAX", "ORD")]

print("\n#####################\n",  "\nAll Possible Routes: ")
for i in edgeList:
    print(i)
print("\n#####################\n")
graph = graph_build(edgeList, True)
graph2 = First_Pass(graph)
graph3 = edge_array_w_finishing_times(edgeList)
graph_with_f_times = graph_build(graph3, False)
graph, leaders = Second_Pass(graph_with_f_times)
Departure = input("Enter Airport You Are Departing From: ")
Destination = input("Enter Your Destination Airport: ")


def get_out(position, destination):
    visited = []
    stack = []
    graph
    path = []
    stack.append(position)
    visited.append(position)
    while stack:
        curr = stack.pop()
        path.append(curr)
        values = graph[curr]
        destination_list = values[2]
        for neigh in destination_list:
            if neigh not in visited:
                visited.append(neigh)
                stack.append(neigh)
                if neigh == destination:
                    print("\n#####################", "\nYour Travel Itinerary", "\n#####################", "\n")
                    num_of_stops = len(path)
                    path.insert(len(path), Destination)
                    t = 0
                    for i in range(len(path)):
                        if i < len(path)-1:
                            print("Departing Airport:", path[i], " Arriving Airport:", path[i+1])
                    print("\n#####################", "\nNumber of Stops: ", num_of_stops)
                    sys.exit(0)
    print("Not found")
    print(path)

def find_route(position, destination1):
    list_of_components = graph[position]
    beginning_Main_Node = list_of_components[0]
    ending_Main_Node = []
    for key, value in graph.items():
        if destination1 in value[2]:
            comp = [key, value[0]]
            ending_Main_Node.append(comp)
    for x in ending_Main_Node:
        if x[1] == beginning_Main_Node:
            pass
    get_out(position, destination1)


find_route(Departure, Destination)
