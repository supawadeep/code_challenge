def result_(result, start, goal):
    res_text = ""
    if result[2] == "error":
        res_text = "Path is not reachable"
    else:
        res_path = ' -> '.join(result[0])
        res_text = "Path from " + start + ' to ' + goal + ' is ' + str(res_path) + ', and have cost '+ str(result[1])
    
    return res_text

def find_shortest_path(graph, start, goal):
    temp_graph = graph
    infinity = 999999
    path = [] 
    cost = {}
    track = {} 
    
    for node in temp_graph:
        cost[node] = infinity
    cost[start] = 0

    while temp_graph:
        min_cost_node = None

        for node in temp_graph:
            if min_cost_node is None:
                min_cost_node = node
            elif cost[node] < cost[min_cost_node]:
                min_cost_node = node
        
        path_option = graph[min_cost_node].items()

        for sub_node, value in path_option:
            if value + cost[min_cost_node] < cost[sub_node]:
                cost[sub_node] = value + cost[min_cost_node]
                track[sub_node] = min_cost_node
        temp_graph.pop(min_cost_node)
    currentNode = goal

    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = track[currentNode]

        except KeyError:
            return [None,None,'error']
            break
    path.insert(0, start)

    if cost[goal] != infinity:
        return [path,cost[goal],'success']

def read_file(file):
    r_file = open('./data/'+file, "r")
    data_file  = r_file.read()

    split_data = data_file.split("\n")

    in_use_data = {}

    for first_item in split_data:
        split_item = first_item.split(",")
        if split_item[0] in in_use_data:
            in_use_data[split_item[0]].update({split_item[1]: int(split_item[2])})
        else:
            in_use_data[split_item[0]] = {split_item[1]: int(split_item[2])}
            
        if split_item[1] in in_use_data:
            in_use_data[split_item[1]].update({split_item[0]: int(split_item[2])})
        else:
            in_use_data[split_item[1]] = {split_item[0]: int(split_item[2])}

    return in_use_data
  
def main():
    file = input("What is graph file name: ")
    start = input("What is start node?: ")
    goal = input("What is goal node?: ")

    graph_data = read_file(file)

    res_data = find_shortest_path(graph_data, start, goal)

    final_result = result_(res_data,start, goal)


if __name__ == "__main__":
    main()


