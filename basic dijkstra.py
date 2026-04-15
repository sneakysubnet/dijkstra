'''
We need
1)List of unvisited nodes
2)Table with cost per node
'''
graph = {
    "R1":{"R2":100,"R3":10},
    "R2":{"R1":100,"R3":5,"R4":50},
    "R3":{"R1": 10, "R2":5, "R4": 200},
    "R4":{"R3": 200, "R2": 50}
}

def dijkstra(graph, source):

    unvisited_nodes = []

    costs = {}

    for node in graph:
        if node == source:
            costs[node]= 0
        else:
            costs[node] = float("inf")
        unvisited_nodes.append(node)

    print('Costs before any manipulations: ',costs)

    while unvisited_nodes:
        min_cost= float("inf")
        for node in unvisited_nodes:
            if costs[node] < min_cost:
                min_cost = costs[node]
                wn=node

        for k,v in graph[wn].items():
            if k in unvisited_nodes:
                if costs[wn]+v < costs[k]:
                    costs[k] = costs[wn]+v

        print(costs)

        unvisited_nodes.remove(wn)


print(dijkstra(graph, "R1"))
