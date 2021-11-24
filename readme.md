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

### Output:

![path from node A to node G](images/experiment1a.png)
![path from node C to node G](images/experiment1b.png)

## Experiment 2: Candidate Elimination Algorithm
#### Problem Statement

For a given set of training data examples stored in a CSV file, implement and demonstrate that Candidate-Elimination Algorithm to output a description of the set of all hypothesis consistent with the training examples.

#### Task:

The Candidate-Elimination algorithm computes the VERSION SPACE containing all hypothesis from H that are consistent with an observed sequence of training examples.

#### Dataset: finds.csv

| Sky     | AirTemp   | Humidity   | Wind     | Water   | Forecast   | EnjoySport   |
| :---    | :---      | :---       | :---     | :---    | :---       | :---         |
| Sunny   | Warm      | Normal     | Strong   | Warm    | same       | Yes          |
| Sunny   | Warm      | High       | Strong   | Warm    | same       | Yes          |
| Rainy   | Cold      | High       | Strong   | Warm    | change     | No           |
| Sunny   | Warm      | High       | Strong   | Warm    | change     | Yes          |

#### Expected Output:
`Final S: ['Sunny' 'Warm' '?' 'Strong' '?' '?']
Final G: [['Sunny', '?', '?', '?', '?', '?'], ['?', 'Warm', '?', '?', '?', '?']]`

#### Actual Output screenshot:
![Final S and Final G](images/experiment2.png)

## Experiment 3: ID3 Algorithm
#### Problem Statement

Write a program to demonstrate the working of the decision tree based ID3 Algorithm. use an appropriate dataset for building the decision tree and apply this knowledge to classify a new sample.

#### Task:

ID3 determines the information gain for each candidate attribute the selects the one with highest information gain as the root node of the tree. the information gain values for all the four attributes are calculated using the following formula:



#### Dataset: Weather.csv

