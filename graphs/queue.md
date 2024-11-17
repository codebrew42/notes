# queue
## definition
- a queue is a data structure that follows the First-In-First-Out (FIFO) principle. This means that the first element added to the queue will be the first one to be removed like a line of people waiting for a bus.

## queue in BFS
- In BFS, a queue is used to keep track of the nodes to be explored next.
	-> When you visit a node, you enqueue its unvisited neighbors.
	-> Then you dequeue the next node from the queue and visit its unvisited neighbors.
	-> This process continues until the queue is empty, indicating that all nodes have been visited.

