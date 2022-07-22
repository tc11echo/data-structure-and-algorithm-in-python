# Algorithm

### Definition

* An algorithm is a step by step method of solving a problem
* It is commonly used for data processing, calculation and other related computer and mathematical operations



### Types of Algorithm Strategy

* Brute Force Algorithm
* Greedy Algorithm
* Divide and Conquer
* Backtracking
* Branch and Bound Method
* Dynamic Programming

---
# Algorithm Efficiency

The process of measuring the complexity of algorithms is called analysis of algorithms


### Complexity
* Time Complexity – The time it takes to execute
* Space Complexity –The memory it needs to execute


### Different Cases of Running time
* Best-case
  * The algorithm takes the least time and it can do no better than that
* Worst-case
  * The algorithm takes the most time and it can do no worse than that
  * Worst-case count = maximum count
* Average-case
  * The average case on take typical data
  * often difficult to determine

---

# Big-O Notation

### Definition

* Given functions $f(n)$ and $g(n)$, we say that $f(n)$ is $O(g(n))$ if there are positive constants $c$ and $n_0$ such that

$$f(n)\leq cg(n)\ for\ n \geq n_0$$

* $cg(n)$ gives the upper-bound on $f(n)$

### How to find Big-O:

1. Drop lower-order terms
2. Drop constant factors

### Properties

* All log are in base2

* The meaning of Big-Oh functions in running time.
  * O(1) is constant time
  * O(logn) is logarithmic time
  * O(n) is linear time
  * O(n<sup>2</sup>) is quadratic time


### Growth Rate:

$$1 < log(log(n)) < log(n) < n < nlog(n) < n^2 < n^3 < 2^n < n!$$

![algorithm_note_big_o](/algorithm/pic/algorithm_note_pic/algorithm_note_big_o.png)

---

#Calculating Big-O from equation

**Example1:**

$$\begin{split}
f(n)&=5n^2+3n+4 \\
f(n) &\leq5n^2+3n^2+4n^2,\ where(n^2)\ is\ the\ leading\ term \\
&=12n^2 \\
&\leq cg(n),\ where(n\geq n_0)
\end{split}$$

$c=12,\ g(n)=n^2,\ n_0=1$

$f(n)=O(g(n))$

-->$5n^2+3n+4=O(n^2)$

<br/>

**Example2:**

$$\begin{split}
f(n)&=3logn+5 \\
f(n) &\leq3 logn+5logn,\ where(logn)\ is\ the\ leading\ term \\
&=8logn \\
&\leq cg(n),\ where(n \geq n_0) \\
\end{split}$$

$c=8,\ n_0=2$

$f(n)=O(g(n))$

-->$3logn+5=O(logn)$


---

#Calculating Big-O from code

```
for i in range(0,N):
  for j in range(N,i,-1):
    a=a+i+j
```

|i|j|number of looping|
|:---|:---|:---:|
|i=0|j:N,N-1,N-2,...,1|N|
|i=1|j:N,N-1,N-2,...,2|N-1|
|i=2|j:N,N-1,N-2,...,3|N-2|
|i=k|j:N,N-1,N-2,...,k+1|N-k|

<br/>

The total number of running time is (N)+(N-1)+(N-2)+...+(N-k), and k = N-1 (by code):

<br/>

$$\begin{split}
\displaystyle\sum_{i=0}^{N-1}(N-i)
&=\displaystyle\sum_{i=0}^{N-1}N-\displaystyle\sum_{i=0}^{N-1}i \\
&=N\displaystyle\sum_{i=0}^{N-1}-(0+1+...+(N-1)) \\
&=N(N)-\frac{N-1}{2}(1+(N-1)) \\
&=N^2-(\frac{N^2-N}{2}) \\
&=\frac{N^2}{2}+\frac{N}{2} \\
&=O(N^2)
\end{split}$$

---
# Reference

[Big-O Complexity Chart](https://www.bigocheatsheet.com/)

![algorithm_note_big_o1](/algorithm/pic/algorithm_note_pic/algorithm_note_big_o1.png)

![algorithm_note_big_o2](/algorithm/pic/algorithm_note_pic/algorithm_note_big_o2.png)
