### Correction LIM09

* **Step 1: Check Continuity.** For $f$ to be continuous at $x = 1$, the left-hand and right-hand limits must be equal to $f(1)$:
  $$f(1) = 1^2 + a(1) + b = 1 + a + b$$
  $$\lim_{x \to 1^+} f(x) = \lim_{x \to 1^+} \ln(x) = \ln(1) = 0$$
  Equating the limits gives our first condition:
  $$1 + a + b = 0 \implies b = -1 - a \quad \text{(Equation 1)}$$

* **Step 2: Check Differentiability.** For $f$ to be differentiable at $x = 1$, the derivatives from both sides must match at $x = 1$:
  * For $x < 1$: $f'(x) = 2x + a \implies \lim_{x \to 1^-} f'(x) = 2 + a$
  * For $x > 1$: $f'(x) = \frac{1}{x} \implies \lim_{x \to 1^+} f'(x) = \frac{1}{1} = 1$
  Equating these derivative values gives:
  $$2 + a = 1 \implies a = -1$$

* **Step 3: Solve for $b$.** Substitute $a = -1$ back into Equation 1:
  $$b = -1 - (-1) = 0$$

**Conclusion:** The function is continuous and differentiable at $x = 1$ if $a = -1$ and $b = 0$.