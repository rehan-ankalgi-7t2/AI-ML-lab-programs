# step 1: define graph nodes
# step 2: define heuristic values
# step 3: prepare get neighbors function
# step 4: A* Logic
# step 5: function call

graph = {
    'A' : [('B', 2), ('E', 3)],
    'B' : [('C', 1), ('G', 9)],
    'C' : None,
    'D' : [('G', 1)],
    'E' : [('D', 6)]
}

def heuristic(n):
    heuristic_dict = {
        'A' : 11,
        'B' : 6,
        'C' : 99,
        'D' : 1,
        'E' : 7,
        'G' : 0,
    }
    return heuristic_dict[n]

def get_neighbors(v):
    if v in graph:
        return graph[v]
    else:
        return None

def aStar(startnode, stopnode):
    openset = set(startnode)
    closedset = set()
    g = {}
    parents = {}
    parents[startnode] = startnode
    g[startnode] = 0

    while len(openset) > 0:
        n = None

        for v in openset:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stopnode or graph[n] == None:
            pass
        else:
            for (m ,weight) in get_neighbors(n):
                if m not in openset and m not in closedset:
                    openset.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        parents[m] = n
                        g[m] = g[n] + weight

                        if m in closedset:
                            closedset.remove(m)
                            openset.add(m)
        
        if n == None:
            print('path not found')
            return None

        if n == stopnode:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(startnode)
            path.reverse()

            print('path found: {}'.format(path))
            return path
        
        openset.remove(n)
        closedset.add(n)

    print('path not found')
    return None

aStar('A', 'G')