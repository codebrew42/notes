#ifndef GRAPH_H
#define GRAPH_H

// #include 
// #include //for print_graph?

enum visit_flag { unreachable = -1, not_visited = 0, visited = 1 }; // Explicitly set values

typedef int v_datatype;

typedef struct tag_vertex
{
	v_datatype			data;
	int					visited;
	int					idx;
	struct tag_vertex	*next;
	struct tag_edge		*adjacency_list;
}	Vertex;

typedef struct tag_edge
{
	Vertex				*from;
	Vertex				*to;
	int					weight; //can be (1)distance (2)cost of traversing btw two points
	struct tag_edge		*next;
}	Edge;

typedef struct tag_edge
{
	Vertex				*vertices;
	int					verticex_count;
}	Graph;

Graph	*create_graph();
void	distroy_graph(Graph *G);

Edge	*create_edge(Vertex *from, Vertex *to, int weight);
void	distroy_edge(Edge *e);

void	add_vertex(Graph *G, Vertex *V); //add one vertex on one func call
void	add_edge(Vertex *V, Edge *E); //add one edge to one vertex
void	print_graph(Graph *G);

#endif