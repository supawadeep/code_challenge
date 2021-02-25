
def find_shortest_path(graph, start, goal):
    # print("TCL: goal", goal)
    # print("TCL: start", start)
    # print("TCL: graph", graph)
    temp_graph = graph
    infinity = 999999
    path = [] 
    cost = {}
    track = {} 
    
    for node in temp_graph:
        cost[node] = infinity
    cost[start] = 0
    # print("TCL: cost", cost)

    while temp_graph:
        min_cost_node = None #min_distance_node

        for node in temp_graph:
            if min_cost_node is None:
                min_cost_node = node
            elif cost[node] < cost[min_cost_node]:
                min_cost_node = node
        
        path_option = graph[min_cost_node].items()
    # print("TCL: path_option", path_option)

        for sub_node, value in path_option:
    # print("sub_node", sub_node, " || value", value, ' || cost[min_cost_node] ', cost[min_cost_node], '   || cost[sub_node]', cost[sub_node])

            if value + cost[min_cost_node] < cost[sub_node]:
                cost[sub_node] = value + cost[min_cost_node]
                track[sub_node] = min_cost_node
        temp_graph.pop(min_cost_node)
    currentNode = goal


#     print("TCL: currentNode", currentNode)
#     print("TCL: start", start)
    while currentNode != start:
        try:
            
            path.insert(0, currentNode)
#             print("TCL: path", path)
#             print("TCL: track[currentNode]", track)
            currentNode = track[currentNode]
#             print("TCL: currentNode", currentNode)
        except KeyError:
#             print("TCL: KeyError", KeyError)
            print("TCL: Path is not reachable")
            break
    path.insert(0, start)

    if cost[goal] != infinity:
#         print("TCL: Shortest distance is " + str(cost[goal]))
        res_path = ' -> '.join(path)
#         print("TCL: Path " + str(res_path))
        print("Path from " + start + ' to ' + goal + ' is ' + str(res_path) + ', and have cost '+ str(cost[goal]))
        
file = input("What is graph file name: ")
start = input("What is start node?: ")
goal = input("What is goal node?: ")
# print("TCL: file", file)
r_file = open(file, "r")
data_file  = r_file.read()
# print("TCL: data_file", data_file)

split_data = data_file.split("\n")
# print("TCL: split_data", split_data)

in_use_data = {}
for first_item in split_data:
    split_item = first_item.split(",") 
    # print("TCL: split_item", split_item)
    if split_item[0] in in_use_data:
        in_use_data[split_item[0]].update({split_item[1]: int(split_item[2])})
    else:
        in_use_data[split_item[0]] = {split_item[1]: int(split_item[2])}
        
    if split_item[1] in in_use_data:
        in_use_data[split_item[1]].update({split_item[0]: int(split_item[2])})
    else:
        in_use_data[split_item[1]] = {split_item[0]: int(split_item[2])}
# print("TCL: in_use_data", in_use_data)

find_shortest_path(in_use_data, start, goal)
