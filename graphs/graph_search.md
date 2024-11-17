# graph search
## types
- BFS(Breadth-First Search) : easy to implement, uses more memory
- DFS(Depth-First Search) : easy to understand, hard to implement, uses less memory


## DFS (Depth-First Search)
### **How it works:**
1. Start at the root (or any arbitrary node) and mark it as visited.
2. Explore each adjacent vertex (neighbor) that has not been visited yet.
3. For each unvisited neighbor, repeat the process until there are no unvisited neighbors left.
4. If you reach a vertex with no unvisited neighbors, backtrack to the previous vertex and continue exploring.

### **Example:**
Consider the following graph:
```
    A
   / \
  B   C
 / \   \
D   E   F
```
- Start at A, mark it as visited.
- Move to B, mark it as visited.
- Move to D, mark it as visited. (D has no unvisited neighbors, backtrack to B)
- From B, move to E, mark it as visited. (E has no unvisited neighbors, backtrack to B, then backtrack to A)
- From A, move to C, mark it as visited.
- Move to F, mark it as visited. (F has no unvisited neighbors, backtrack to C, then backtrack to A)

### **Traversal Order:** A, B, D, E, C, F

## BFS (Breadth-First Search)
### **How it works:**
1. Start at the root (or any arbitrary node) and mark it as visited.
2. Use a queue to explore all adjacent vertices (neighbors) at the present depth before moving on to the next level.
3. For each visited vertex, enqueue its unvisited neighbors.
4. Continue this process until all vertices have been visited.

### **Example:**
Using the same graph:
```
    A
   / \
  B   C
 / \   \
D   E   F
```
- Start at A, mark it as visited and enqueue B and C.
- Dequeue B, mark it as visited and enqueue D and E.
- Dequeue C, mark it as visited and enqueue F.
- Dequeue D, mark it as visited (D has no unvisited neighbors).
- Dequeue E, mark it as visited (E has no unvisited neighbors).
- Dequeue F, mark it as visited (F has no unvisited neighbors).

### **Traversal Order:** A, B, C, D, E, F

### Summary
- **DFS** explores as far as possible down one branch before backtracking, making it suitable for scenarios where you want to explore all possibilities (like solving puzzles).
- **BFS** explores all neighbors at the present depth before moving on, making it ideal for **finding the shortest path in unweighted graphs**.
	-> why? 
		1. **Level-wise Exploration**: BFS explores all nodes at the present depth level before moving on to nodes at the next depth level. This means that when a node is reached for the first time, it is guaranteed to be the shortest path to that node.
		2. **Queue Data Structure**: BFS uses a queue to keep track of the nodes to be explored. This ensures that nodes are processed in the order they are discovered, which is essential for finding the shortest path.
		3. **Unweighted Edges**: In unweighted graphs, all edges are treated equally. BFS does not need to consider edge weights, simplifying the process of finding the shortest path.
		4. **Early Termination**: Once the target node is dequeued and processed, BFS can terminate immediately, ensuring that the shortest path is found without unnecessary exploration.

### implementation
- **DFS** explores as far as possible down one branch before backtracking, making it suitable for scenarios where you want to explore all possibilities (like solving puzzles). 
  - **Common Implementation**: DFS is commonly implemented using recursion, as it naturally follows the depth-first approach by using the call stack.
  - **Recursion**: uses a stack to store the nodes to be explored. so it can be said that DFS is implemented using STACK/Recursion.
  
- **BFS** explores all neighbors at the present depth before moving on, making it ideal for **finding the shortest path in unweighted graphs**. 
  - **Common Implementation**: BFS is typically implemented using an iterative approach with *a queue*, as it requires tracking nodes level by level.

For more detailed comparisons and applications, you can refer to resources like [Open4Tech](https://open4tech.com/bfs-vs-dfs/) and [TechDifferences](https://techdifferences.com/difference-between-bfs-and-dfs.html).