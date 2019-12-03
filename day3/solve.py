def makeGrid(path):
    grid = []
    x = 0
    y = 0
    for step in path:
        direction, count = step[:1], int(step[1:])
        # each instruction
        for _ in range(count):
            # append tuple
            grid.append((x, y))
            # increment pos
            if(direction == 'U'):
                y = y+1
            elif(direction == 'R'):
                x = x+1
            elif(direction == 'D'):
                y = y-1
            elif(direction == 'L'):
                x = x-1
            else:
                raise Exception('Invalid direction: {}'.format(direction))
    return grid


def getIntersections(grid1, grid2):
    intersections = set(grid1).intersection(set(grid2))
    # we don't care about the intersection point at the central port
    intersections.remove((0, 0))
    return intersections

def closestIntersection(grid1, grid2):
    # distances are simply the sum of the absolute values of x and y
    distances = [abs(x)+abs(y) for (x, y) in getIntersections(grid1, grid2)]
    return min(distances)

def leastSteps(grid1, grid2):
    intersections = getIntersections(grid1, grid2)
    # total steps are the sum of the indexes of the intersection on each grid
    steps = [grid1.index(intersection) + grid2.index(intersection) for intersection in intersections]
    return min(steps)

if __name__ == '__main__':
    with open('./day3/input.txt') as file:
        wire1 = file.readline().split(',')
        wire2 = file.readline().split(',')
    grid1, grid2 = makeGrid(wire1), makeGrid(wire2)
    print(closestIntersection(
        makeGrid(wire1), makeGrid(wire2)))
    print(leastSteps(
        makeGrid(wire1), makeGrid(wire2)))