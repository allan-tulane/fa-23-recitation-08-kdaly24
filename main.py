from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    def sspath(pastset, frontier):
        
        if len(frontier) == 0:
            return pastset
        
        else:
            distance, node_edges = heappop(frontier)
            curr = node_edges[0]
            edges = node_edges[1]

            if curr in pastset:
                if pastset[curr][0] == distance:
                    if pastset[curr][1] > edges:
                      pastset[curr] = (distance, edges)
                return sspath(pastset, frontier)
            
            else:
                pastset[curr] = (distance, edges) 
                for adjacent_node, weight in graph[curr]:
                    heappush(frontier, (distance + weight, (adjacent_node, edges + 1)))
                return sspath(pastset,frontier)
    
    frontier = []
    heappush(frontier, (0, (source, 0)))
    pastset = dict()
    return sspath(pastset, frontier)
    
    
def bfs_path(graph, source):
    
    def bfspath(pastset, frontier,path):
        if len(frontier)==0:
            return path
        else:
            pastset=pastset|frontier 
            frontier_update=set()
            for node in frontier:
                for neighbor in graph[node]:
                    if neighbor not in pastset:
                        path[neighbor]=node
                        frontier_update.add(neighbor)   
            return bfspath(pastset, frontier_update, path)
        
    visitedset=set()
    startfrontier=set([source])
    emptypath=dict()
    return bfspath(visitedset,startfrontier,emptypath)
    

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    current = destination
    final = ''
    while True:
        if current =='s':
            break
        else:
            current = parents[current]
            final += current


    return final[::-1]

