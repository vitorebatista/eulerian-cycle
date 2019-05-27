## Installation
Make sure you have [Pipenv](https://github.com/pypa/pipenv#installation) and execute:
```shell
$ pipenv install 
```

## Usage

```shell
$ pipenv shell
$ python main.py
```

## Idea of the algorithm
The basic idea of Hierholzer's algorithm is the stepwise construction of the Eulerian cycle by connecting dijunctive circles. It starts with a random node and then follows an arbitrary unvisited edge to a neighbour. This step is repeated until one returns to the starting node. This yields a first circle in the graph. If this circle covers all nodes it is an Eulerian cycle and the algorithm is finished. Otherwise, one chooses another node among the cycles' nodes with unvisited edges and constructs another circle, called subtour. By choice of edges in the construction the new circle does not contain any edge of the first circle, both are disjunct. However, both circles must intersect in at least one node by choice of the starting node of the second circle. Therefore one can represent both circles as one new circle. To do so, one iterates the nodes of the first circle and replaces the subtour's starting node by the complete node sequence of the subtour. Thus, one inegrates additional circles into the first circle. If the extended cycle does include all edges the algorithm is finished. Otherwise, we can find another cycle to include.

In the case of an undirected, semi-Eulerian graph the algorithm starts with one of the two nodes with odd degree. In the directed case with the node with one additional outgoing edge. One of the subtours to be found will then not form a cycle, instead it will also be a path. When integrating this "subtour" into the circle one has to make sure that start and end node of this path also form start and end of the complete Eulerian path.

## Prints

<img src="./data/1.png" width="250" height="250"><img src="./data/2.png" width="250" height="250">
<img src="./data/3.png" width="250" height="250">
<img src="./data/4.png" width="250" height="250">
<img src="./data/5.png" width="250" height="250">
<img src="./data/6.png" width="250" height="250">
<img src="./data/7.png" width="250" height="250">
<img src="./data/8.png" width="250" height="250">
<img src="./data/9.png" width="250" height="250">

## Contributing
PRs are welcome, if you have any questions don't be afraid to open an issue.
