### Correction INT06

1. **Differentiability Justification:**
Let $f(t) = e^{-t^2}$. This function is continuous on $\mathbb{R}$, so it admits a primitive function $F$ such that $F'(t) = f(t)$.
By the Fundamental Theorem of Calculus, we can write the integral using this primitive template:
$$G(x) = F(x^2) - F(0)$$
Since $x \mapsto x^2$ is differentiable on $\mathbb{R}$ and $F$ is differentiable, the composite chain function $G(x)$ is fully differentiable on $\mathbb{R}$.

2. **Derivative Calculation:**
Using the chain rule formula for differentiation $(F(u(x)))' = u'(x) \cdot F'(u(x))$:
$$G'(x) = (x^2)' \cdot F'(x^2) - 0 = 2x \cdot f(x^2)$$
Substitute the explicit mapping expression for $f$:
$$G'(x) = 2x \cdot e^{-(x^2)^2} = 2x e^{-x^4}$$