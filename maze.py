import random
from space import Space

def valid_move(current, maze):
    x = current.x
    y = current.y
    #print(x, y)
    moves = []
    if x > 0 and not maze[y][x-1]:
        moves.append(Space(x-1, y))
    if y > 0 and not maze[y-1][x]:
        moves.append(Space(x, y-1))
    if x < len(maze[0])-1 and not maze[y][x+1]:
        moves.append(Space(x+1, y))
    if y < len(maze)-1 and not maze[y+1][x]:
        moves.append(Space(x, y+1))

    if len(moves) == 0:
        return None
    return moves[random.randint(0, len(moves)-1)]

def maze_builder(height, width, start, end):

    maze = [[None for i in range(width)] for j in range(height)];

    print (len(maze), len(maze[0]))

    spaces = []

    spaces.append(start);
    maze[start.y][start.x] = start

    while len(spaces) > 0:

        current = spaces[len(spaces)-1]
        nextSpace = valid_move(current, maze)

        if nextSpace:
            knock_down(current, nextSpace)
            spaces.append(nextSpace)
            maze[nextSpace.y][nextSpace.x] = nextSpace
        else:
            spaces.pop()

    maze[start.y][start.x].id = "S"
    maze[end.y][end.x].id = "E"

    print_maze(maze)

def knock_down(c, n):
    if (c.y < n.y):
        n.top = False
    elif (c.y > n.y):
        c.top = False
    elif (c.y == n.y and c.x < n.x):
        n.left = False
    else:
        c.left = False

def print_maze(maze):

    for i in range(len(maze)):
        string = ""
        for j in range(len(maze[0])):
            if not maze[i][j] or maze[i][j].top:
                string += " ---"
            else:
                string += "    "
        print(string)

        string = ""
        for k in range(len(maze[0])):
            if maze[i][k] and maze[i][k].left:
                string += "| " + maze[i][k].id + " "
            elif maze[i][k]:
                string += "  " + maze[i][k].id + " "
            else:
                string += "|   "
        string += "|"
        print(string)

    string = ""
    for l in range(len(maze[0])):
        string += " ---"
    print(string)