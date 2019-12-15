def makeGraph(orbits):
    graph = {}
    for (A, B) in orbits:
        if(A not in graph):
            graph[A] = []
        graph[A].append(B)
    return graph

def dfs(node, graph, acc, stack=[]):
    for prevNode in stack:
        acc.add((prevNode, node))

    if(node in graph):
        children = graph[node]
        newStack = stack.copy()
        newStack.append(node)

        for child in children:
            dfs(child, graph, acc, newStack)

def ocb(orbits):
    acc = set()
    dfs("COM", makeGraph(orbits), acc)
    return len(acc)
        


if __name__ == '__main__':
    with open('./day6/input.txt') as file:
        orbits = [tuple(line.strip().split(")")) for line in file]
    print(ocb(orbits))

    
