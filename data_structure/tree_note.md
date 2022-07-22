# Tree

### Definition

* A tree is a connected undirected graph with no simple circuits

![tree-example.png](/data_structure/pic/tree_note_pic/tree_note_example.png)

##### Node/Vertex

* **Degree of Node**: the number of edges that connected to its child
	> degree of A is 3, degree of F is 2, degree of N is 0
* **Height of Node**: the number of edges on the longest path from the node to a descendant leaf
	> the height of F is 1, the height of D is 2, the height of leaf node is 0
* **Depth of Node**: the number of edges from the node to root
	> depth of F is 2, depth of L is 3
* **Parent <--> Child**: Indicated by pointer, the pointed node is the child, and the pointing node is the parent
	> A is C parent, C is A child
	> E is K parent, K is E child
* **Root**: the top node in the tree, and the only node whose parent is NULL
	> A
* **Internal Node**: a Node/Vertex that has at least one child
	> A,B,C,D,E,F,I
* **External Node, Terminal Node, Leaf**: a Node/Vertex that has no children
	> G,H,J,K,L,M,N
* **Siblings**: the nodes with the same parent
	> B,C,D
* **Ancestor(祖先)**: all nodes that can be found in the way of "finding the parent" are called the ancestors that node
	> E,B,A are K's ancestor
* **Descendant(子嗣)**: all nodes that can be found in the way of "parent pointing to child" are called descendants of that node
	> F,L,M are C's descendant

##### Tree

* **Degree of Tree**: max node degree
	> degree of above tree is 3
* **Height of Tree**: the root's height
	> height of tree is height of A, which equal 3
* **Depth of Tree**: the number of edge from one leaf to root
	> depth of Tree is 3
* **Level**: Define the level of root as 0, the level of the remaining nodes is increased by one to the level of its parent
* **Height of Tree = Depth of Tree = Highest Level Number**
	
	* $h = max\{ l(v) \},\ v \in V(T),\ level=l(v)$
* **Path**: form by the edges between ancestor and descendant
	> ABEK, ACFN
* **Subtree**: a subtree of a tree $T$ is a tree $T'$ such that
	* $V(T') \subseteq V(T)\ and\ E(T') \subseteq E(T)$

### Property

**Theorem**:

* A tree with $n$ nodes has $n−1$ edges
* As a vertex in a tree can either be an internal vertex or a leaf
	* $n = i + l$ where $i$ is the number of internal nodes and $l$ is the number of leaves
* A full $m$-ary tree with $i$ internal nodes has
	* $n=mi+1$ nodes
	* $l=(m-1)i+1$ leaves
* There are at most $m^h$ leaves in an m-ary tree of height $h$

### Tree Type

* **Binary Tree**: 2-ary tree
* **Full Binary Tree**: every parent node/internal node has either two or no children
* **Complete Binary Tree**: all the levels are completely filled except possibly the last level and the last level has all keys as left as possible
* **Perfect Binary Tree**: all the internal nodes have two children and all leaf nodes are at the same level

---

### Forest

* An undirected graph (but not necesarily connected) without simple circuits is called a forest
* i.e. a branch of trees

---

### Spanning Tree

* Given a graph $G$, a tree $T$ is a spanning tree of $G$ if
	* $T$ is a subgraph of $G$
	* $T$ contains all the vertices of $G$
* **Theorem**: a simple graph is connected if and only if it has a spanning tree

##### How to find

* Depth-first search to find a spanning tree

> **procedure** $DFS$($G$: connected graph with vertices $v_1, v_2,…, v_n$)
> $T$ := tree consisting only of the vertex $v_1$
> $visit$($v_1$)

> **procedure** $visit$($v$: vertex of $G$)
> **for** each vertex $w$ adjacent to $v$ and not yet in $T$
> &nbsp;&nbsp;&nbsp;&nbsp;add vertex $w$ and edge {$v, w$} to $T$
> &nbsp;&nbsp;&nbsp;&nbsp;$visit$($w$)

* Breadth-first search to find a spanning tree

> **procedure** BFS(G: connected graph with vertices $v_1, v_2,…, v_n$)
> $T$ := tree consisting only of vertex $v_1$
> $L$ := empty list
> put $v_1$ in the list $L$ of unprocessed vertices
> **while** $L$ is not empty
> &nbsp;&nbsp;&nbsp;&nbsp;remove the first vertex, $v$, from $L$
> &nbsp;&nbsp;&nbsp;&nbsp;**for** each neighbor $w$ of $v$
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**if** $w$ is not in $L$ and not in $T$ **then**
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;add $w$ to the end of the list $L$
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;add $w$ and edge {$v, w$} to $T$

---

### Minimum Spanning Tree

* A **minimum spanning tree** (for undirected graphs) is a connected sub-graph with the minimum number of edges connecting all the vertexes of the original simple graph

##### How to find
* Prim’s algorithm

> **procedure** $Prim$($G$: weighted connected undirected graph with $n$ vertices)
> $T$ := a minimum-weight edge
> **for** $i$ := $1$ **to** $n − 2$
> &nbsp;&nbsp;&nbsp;&nbsp;$e$ := an edge of minimum weight incident to a vertex in T and not forming a simple circuit in $T$ if added to $T$
> &nbsp;&nbsp;&nbsp;&nbsp;$T$ := $T$ with e added
> **return** $T$ {$T$ is a minimum spanning tree of $G$}

![prim.JPG](/data_structure/pic/tree_note_pic/tree_note_prim.jpg)

* Kruskal’s algorithm

> **procedure** $Kruskal$($G$: weighted connected undirected graph with $n$ vertices)
> $T$ := empty graph
> **for** $i$ := $1$ **to** $n − 1$
> &nbsp;&nbsp;&nbsp;&nbsp;$e$ := any edge in $G$ with smallest weight that does not form a simple circuit when added to $T$
> &nbsp;&nbsp;&nbsp;&nbsp;$T$ := $T$ with $e$ added
> **return** $T$ {$T$ is a minimum spanning tree of $G$}

![kruskal.JPG](/data_structure/pic/tree_note_pic/tree_note_prim.jpg)
