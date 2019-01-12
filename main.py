from space import Space
from maze import maze_builder
import sys

# driver
if not len(sys.argv) == 3:
    print("Usage: python main.py height width")
    exit()

h = int(sys.argv[1])
w = int(sys.argv[2])
start = Space(0, 0)
end = Space(w-1, h-1)
maze_builder(h, w, start, end)