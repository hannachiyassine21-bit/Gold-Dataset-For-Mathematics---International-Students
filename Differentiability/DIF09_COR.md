### Correction DIF09

1. **Existence and Uniqueness Proof:**
   * **Continuity:** $f$ is a polynomial function, so it is continuous on $\mathbb{R}$.
   * **Monotonicity:** Compute the first derivative:
     $$f'(x) = 5x^4 + 3x^2 + 1$$
     Since $x^4 \ge 0$ and $x^2 \ge 0$ for all real numbers, $5x^4 + 3x^2 + 1 \ge 1 > 0$. The derivative is strictly positive, meaning $f$ is strictly increasing on $\mathbb{R}$.
   * **Limits:** Compute the limits at the boundaries:
     $$\lim_{x \to -\infty} f(x) = -\infty \quad \text{and} \quad \lim_{x \to +\infty} f(x) = +\infty$$
   Since $f$ is continuous, strictly increasing, and changes sign across its domain, the Intermediate Value Theorem guarantees that the equation $f(x) = 0$ has exactly one real root $\alpha$ on $\mathbb{R}$.

2. **Bounding the Root:**
   Evaluate the function at the endpoints $x = 0$ and $x = 1$:
   * $f(0) = 0 + 0 + 0 - 1 = -1 < 0$
   * $f(1) = 1^1 + 1^3 + 1 - 1 = 2 > 0$
   Since $f(0) \cdot f(1) < 0$, the root $\alpha$ must lie strictly within the interval $]0, 1[$.