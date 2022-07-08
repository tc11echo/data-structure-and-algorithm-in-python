# Graph

### Definition
* Discrete structures consisting of vertices and edges that connect these vertices

$$
G=(V,E)
$$

### Graph Representations
Adjacency lists, Adjacency matrices, Incidence matrices

* Adjacency lists

![graph_note_adjacency_lists](/pic/graph_note_pic/graph_note_adjacency_lists.png)

* Adjacency matrices

![graph_note_adjacency_matrices](/pic/graph_note_pic/graph_note_adjacency_matrices.png)

### Graph Type

|Term|Edge|Multiple edges allow|Loops allow|
|:---|:---:|:---:|:---:|
|Simple graph|Undirected|No|No|
|Multigraph|Undirected|Yes|No|
|Pseudograph|Undirected|Yes|Yes|
|Directed graph|Directed|No|Yes|
|Directed multigraph|Directed|Yes|Yes|

Degree of a Vertex: $\displaystyle\sum_{v \in V}deg(v)=2|E|$

$$
\displaystyle\sum_{v \in V}deg^-(v)=\displaystyle\sum_{v \in V}deg^+(v)=\frac{1}{2}\displaystyle\sum_{v \in V}deg(v)=|E|
$$

* The degree of $v$ , $deg(v) = deg^-(v)+deg^+(v)$, is the sum of $v$ ’s in-degree and out-degree
	* The in-degree of $v$ , $deg^−(v)$, is the number of edges going to $v$
	* The out-degree of $v$ , $deg^+(v)$, is the number of edges coming from $v$

* **Corollary **: Any undirected graph has an even number of vertices of odd degree

---

### Isomorphism

* Two graphs $G_1 = V_1, E_1$ and $G_2 = V_2, E_2$ are isomorphic iff
    1. There exists a 1-to-1 and onto function f from $G_1$ to $G_2$ such that for any a, b \in G1, a and b are adjacent in $G_1$ iff f a and f b are adjacent in $G_2$
    2. The only way to show that two graphs are isomorphic is to give a bijection

* Two graphs are NOT isomorphic if
    1. $|V_1| \neq |V_2|$
    2. $|E_1| \neq |E_2|$
    3. The number of vertices with degree $n$ is **different** in $G_1$ and $G_2$
    4. The **inexistence** of a circuit or simple circuit of length k in 1$G_1$ and $G_2$
    5. For every proper subgraph $g$ of one graph, there is no proper subgraph of the other graph that is isomorphic to $g$

---

### Special Graph Structures

* Complete graphs $K_n$
	* Vertex number: $n$
	* Edge number: $\frac{n(n-1)}{2}$
	1. $K_1$ not enough to form, $K_2$ is bipartite, $n>2$ is not bipartite
	2. $K_4$ is planar

* Cycles $C_n$ ($n\geq 3$)
	* Vertex number: $n$
	* Edge number: $n$
	1. If n is even, $C_n$ is bipartite. If n is odd, $C_n$ is not bipartite

* Wheels $W_n$ ($n\geq 3$)
	* Vertex number: $n+1$
	* Edge number: $2(n+1)$
	1. No $W_n$ is not bipartite

* n-Cubes $Q_n$
	* Vertex number: $2^n$
	* Edge number: $\frac{n2^n}{2}=n2^{n-1}$
	1. All $Q_n$ is bipartite. Without $Q_1$
	2. $Q_3$ is planar

* Complete bipartite graphs $K_{m,n}$
	* Vertex number: $m+n$
	* Edge number: $m*n$
	1. $K_{2,3}$, $K_{2,4}$ is not planar

---

<div style="page-break-after: always; break-after: page;"></div>

# Path and Circuit

### Definition

* In an undirected graph, a **path** of length $n$ from $u$ to $v$ is a sequence of adjacent edges going from vertex $u$ to vertex $v$
* A path is a circuit if $u = v$
* A path or circuit is simple if it contains no edge more than once
* Paths in Directed Graphs are the same as in undirected graphs, but the path must go in the direction of the arrows

### Connectedness

* An undirected graph is connected iff there is a path between every pair of distinct vertices in the graph
* Theorem: There is a simple path between any pair of vertices in a connected undirected graph
    * **Connected components**: connected subgraphs
    * **Cut vertex / Cut edge**: separates 1 connected component into 2 if removed

* A directed graph is strongly connected iff there is a directed path from $a$ to $b$ and from $b$ to $a$, for any two vertices $a$ and $b$
* It is weakly connected iff the underlying undirected graph (i.e. with edge directions removed) is connected
* Note strongly implies weakly but not vice-versa

---

### Euler Circuit/Paths

* An Euler circuit in a graph $G$ is a simple circuit containing every edge of $G$
* An Euler path in $G$ is a simple path containing every edge of $G$
* i.e. focus edges

##### Euler Circuits

* A connected multigraph with at least two vertices has an Euler circuit if and only if each vertex has even degree

##### Euler Path

* A connected multigraph with at least two vertices has an Euler path (but not an Euler circuit) if and only if it has exactly 2 vertices of odd degree

### Hamilton Circuits/Paths

* A Hamilton circuit is a circuit that traverses each vertex in $G$ exactly once
* A Hamilton path is a path that traverses each vertex in $G$ exactly once
* i.e. focus vertices

##### Dirac’s theorem

* If (but not only if) $G$ is connected, simple, has $n\geq 3$ vertices, and $deg(v)\geq\frac{n}{2}$ for each vertice, then $G$ has a Hamilton circuit

##### Ore’s corollary

* If (but not only if) $G$ is connected, simple, has $n\geq 3$ nodes, and $deg(u)+deg(v) \geq n$ for every pair $u$, $v$ of non-adjacent nodes, then $G$ has a Hamilton circuit

### Euler’s Formula

* Let $G$ be a connected planar simple graph with $e$ edges and $v$ vertices. Let $r$ be the number of regions in a planar representation of $G$. Then

$$
r=e–v+2
$$

* **Corollary 1**: If $G$ is a connected planar simple graph with $e$ edges and $v$ vertices, where $v \geq 3$. Then

$$
e\leq 3v-6
$$

* **Corollary 2**: If $G$ is a connected planar simple graph ,then $G$ has at least one vertex of degree not exceeding five

---

### Graph Coloring

* The Five Color Theorem (五色定理)
    * easy to prove

* The Four Color Theorem (四色定理)
  * hard to prove
  * The chromatic number of a planar graph is no greater than four


---

### Shortest-Path Problem

##### How to find
* Dijkstra’s algorithm
