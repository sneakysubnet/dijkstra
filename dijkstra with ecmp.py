import json
from xml.sax.handler import property_dom_node

path = []
def trace(data, src,dst):
    if src==dst:
        return
    trace(data,src,data[dst])
    path.append(data[dst])
    return path

def dijkstra(graph, source, destination=None):
    unvisited_nodes = []
    costs = {}
    pbn={}

    for node in graph:
        if node == source:
            costs[node]= 0
        else:
            costs[node] = float("inf")
        pbn[node]=None
        unvisited_nodes.append(node)

    while unvisited_nodes:
        min_cost= float("inf")
        for node in unvisited_nodes:
            if costs[node] < min_cost:
                min_cost = costs[node]
                wn=node

        if min_cost == float("inf"):
            print('Node {} is unreachable'.format(node))

            return costs

        if wn == destination:
            print('Destination reached, terminating')
            #path = trace(pbn, source, destination)
            #path.append(destination)
            return costs,pbn

        for k,v in graph[wn].items():
            if k in unvisited_nodes:
                if costs[wn]+v <= costs[k]:
                    costs[k] = costs[wn]+v
                    if pbn[k]:
                        pbn[k].append(wn)
                    else:
                        pbn[k]=[wn]
        unvisited_nodes.remove(wn)

    return costs, pbn


with open("graph.json", 'r') as graph_file:
    graph = json.load(graph_file)

print(dijkstra(graph, "R1","R4"))