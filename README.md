# maze
Inspired by an interview question I got in the past.

Generates a random maze with a given height and width and prints it to the console. This currently puts the start position at the top left and the end position at the bottom right. It uses a DFS to find the path to the end, which then generates all of the false paths as well. Every square is reachable from the start and there is only one path to the end position.

Usage: 
`python main.py height width`
