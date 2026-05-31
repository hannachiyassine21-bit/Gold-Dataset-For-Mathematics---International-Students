### Correction DIF06

Let $x > 0$. Consider the function $f(t) = e^t$ on the interval $[0, x]$.
* $f$ is continuous on $[0, x]$ and differentiable on $]0, x[$.
By the Mean Value Theorem, there exists a point $c \in ]0, x[$ such that:
$$\frac{f(x) - f(0)}{x - 0} = f'(c) \implies \frac{e^x - 1}{x} = e^c$$

Since $c \in ]0, x[$ and the exponential function is strictly increasing:
$$e^0 < e^c < e^x \implies 1 < \frac{e^x - 1}{x} < e^x$$
Multiply by $x > 0$:
$$x < e^x - 1 < x e^x$$
Add $1$ to all sections of the inequality chain layout:
$$1 + x < e^x < 1 + x e^x$$