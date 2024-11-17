# graphs
## definition
- *a graph* is a collection of nodes and edges
	- *a vertex/a node* is a point in the graph
	- *an edge* is a connection between two nodes
	- if two vertices/nodes are connected by an edge, its called *adjacent nodes*
- *a path* is a sequence of vertices and edges which are connected
- *a cycle* is a path that starts and ends at the same vertex

## types of graphs
- *a directed graph* is a graph where each edge has a direction
- *an undirected graph* is a graph where each edge does not have a direction

# graph representation
- *an adjacency matrix* is a 2D array where the rows and columns represent the vertices, and the value at the intersection of a row and a column represents the edge between the two vertices

-> example:
1. undirected graph : symmetric
```
   [1][2][3][4][5]
[1] 0  1  0  0  1
[2] 1  0  1  0  0
[3] 0  1  0  1  0
[4] 0  0  1  0  1
[5] 1  0  0  1  0
```
2. directed graph : not symmetric
```
   [1][2][3][4][5]
[1] 0  1  0  0  1
[2] 0  0  1  0  0
[3] 0  0  0  1  0
[4] 0  0  0  0  1
[5] 0  0  0  0  0
```
- *an adjacency list* is a list of lists where each list represents the vertices adjacent to the vertex at the index of the list
-> example:
1. undirected graph : same length of lists
```
0: [1, 4]
1: [0, 2]
2: [1, 3]
3: [2, 4]
4: [0, 3]
```
2. directed graph : different length of lists
```
0: [1, 4]
1: [2]
2: [3]
3: [4]
4: []
```

## adjacency matrix
### characteristics
- symmetric if the graph is undirected

### pros
- easy to understand, implement
- needs one array of size V^2
### cons
- takes up more space

	- why? because it is a 2D array, and the number of rows and columns is equal to the number of vertices
- slower to iterate through edges
- slower to check if there is an edge between two vertices

## adjacency list
### characteristics
- faster to iterate through edges
### pros
- takes up less space
- faster to check if there is an edge between two vertices
### cons
- needs at least *3 structures*(see [implementation](#implementation)) to represent
- harder to understand, implement
	- why? because it is a list of lists, and it is not as intuitive as the adjacency matrix
### implementation
```c
//정점 구조체(Edge Structure): 정점 정보를 담는 구조체
typedef struct tag_vertax
{	
	ElementType			data; //
	int					index; //
	int					is_visited;
	struct tag_vertax	*next;
	struct tag_vertax	*adjacent_list;
} vertex;

//간선 구조체(Edge Structure): 간선 정보를 담는 구조체
typedef struct tag_edge
{
	int		weight; //distance or cost
	vertex	*from; //start point
	vertex	*to; //end point
} edge;

//그래프 구조체(Graph Structure): 그래프 정보를 담는 구조체
typedef struct tag_graph
{
	vertex	*vertices;
	int		vertex_count;
} graph;
```
- example : [Graph Directory](file:///Users/jin1/coding/notes.git/others_ThisIsAlgorithm/09_graphs/Graph/Graph.c)