# Artificial Intelligence and Machine Learning laboratory
## Experiment 1: A* Search Algorithm

A* Algorithm in Python or in general is basically an artificial intelligence problem used for the pathfinding \(from point A to point B\) and the Graph traversals. This algorithm is flexible and can be used in a wide range of contexts.
A* Search algorithm is one of the best and popular technique used in path-finding and graph traversals.

This Algorithm is the advanced form of the BFS algorithm \(Breadth-first search\), which searches for the shorter path first than, the longer paths. It is a complete as well as an **optimal** solution for solving path and grid problems.

**Optimal** – find the least cost from the starting point to the ending point. Complete – It means that it will find all the available paths from start to end.

### Basic concepts of A*

**f\(n\) = g\(n\) + h\(n\)**

Where

- g\(n\) : The actual cost path from the start node to the current node. 
- h\( n\) : The actual cost path from the current node to goal node.
- f\(n\) : The actual cost path from the start node to the goal node.

For the implementation of A* algorithm we have to use two arrays namely OPEN and CLOSE.

**OPEN:**

An array that contains the nodes that have been generated but have not been yet examined till yet.

**CLOSE:**

An array which contains the nodes which are examined.

### Algorithm

