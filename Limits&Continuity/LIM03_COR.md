### Correction LIM03

Let's define a new auxiliary continuous function $g$ on $[0, 1]$ by $g(x) = f(x) - x$. 
Evaluate $g$ at the domain boundaries:
* $g(0) = f(0) - 0 = f(0)$. Since the codomain of $f$ is $[0, 1]$, $f(0) \ge 0 \implies g(0) \ge 0$.
* $g(1) = f(1) - 1$. Since the codomain of $f$ is $[0, 1]$, $f(1) \le 1 \implies g(1) \le 0$.

We have $g(1) \le 0 \le g(0)$. Since $g$ is continuous on the interval, by the Intermediate Value Theorem (TVI), there exists at least one real number $c \in [0, 1]$ such that $g(c) = 0$.
$$g(c) = 0 \iff f(c) - c = 0 \iff f(c) = c$$