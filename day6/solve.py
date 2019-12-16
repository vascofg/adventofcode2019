def makeGraph(orbits):
    graph = {}
    for (A, B) in orbits:
        if(A not in graph):
            graph[A] = []
        graph[A].append(B)
    return graph


def ocbSolve(node, graph, previousEdges=0):
    sum = 0
    if(node in graph):
        children = graph[node]

        for child in children:
            # for each branch, go until the end
            sum = sum + ocbSolve(child, graph, previousEdges + 1)

    # count the number of previous edges
    return sum + previousEdges


def ocb(orbits):
    return ocbSolve("COM", makeGraph(orbits))


def orbitalTransfers(orbits):
    invertedGraph = makeGraph([(B, A) for A, B in orbits])
    origin = invertedGraph["YOU"][0]
    destination = invertedGraph["SAN"][0]
    originToCOM = getVisited(invertedGraph, origin, "COM", [])
    destinationToCOM = getVisited(invertedGraph, destination, "COM", [])
    commonAncestor = firstCommonAncestor(originToCOM, destinationToCOM)
    return originToCOM.index(commonAncestor) + destinationToCOM.index(commonAncestor)


def getVisited(graph, node, destination, stack):
    # get all visited nodes to get to COM
    stack.append(node)
    if(node == destination):
        return stack
    else:
        return getVisited(graph, graph[node][0], destination, stack)


def firstCommonAncestor(visited1, visited2):
    return next(node for node in visited1 if node in visited2)


if __name__ == '__main__':
    with open('./day6/input.txt') as file:
        orbits = [tuple(line.strip().split(")")) for line in file]
    print(ocb(orbits))

    print(orbitalTransfers(orbits))
