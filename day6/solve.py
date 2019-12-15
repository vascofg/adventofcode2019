def makeGraph(orbits):
    graph = {}
    for (A, B) in orbits:
        if(A not in graph):
            graph[A] = []
        graph[A].append(B)
    return graph

def dfs(node, graph, stack=[]):
    sum = 0
    if(node in graph):
        children = graph[node]
        newStack = stack.copy()
        newStack.append(node)

        for child in children:
            # for each branch, go until the end and sum the number of previous edges
            sum = sum + dfs(child, graph, newStack)

    return sum + len(stack)

def ocb(orbits):
    return dfs("COM", makeGraph(orbits))
        


if __name__ == '__main__':
    with open('./day6/input.txt') as file:
        orbits = [tuple(line.strip().split(")")) for line in file]
    print(ocb(orbits))

    
