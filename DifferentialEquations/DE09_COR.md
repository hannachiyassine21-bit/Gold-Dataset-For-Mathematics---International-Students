### Correction DE09

* **Step 1: Homogeneous System.** Solve $y'' - y = 0$. The characteristic equation is $r^2 - 1 = 0 \implies r = \pm 1$. This yields:
  $$y_h(x) = C_1 e^x + C_2 e^{-x}$$

* **Step 2: Particular Solution.** The forcing function is a second-degree polynomial, $x^2 - 1$. We can guess a particular solution template of the same degree:
  $$y_p(x) = A x^2 + B x + C$$
  Compute its first and second derivatives:
  $$y_p'(x) = 2A x + B \quad \text{and} \quad y_p''(x) = 2A$$
  Substitute $y_p''$ and $y_p$ back into the original non-homogeneous equation $(E)$:
  $$(2A) - (A x^2 + B x + C) = x^2 - 1 \implies -A x^2 - B x + (2A - C) = x^2 - 1$$

  Match the coefficients for each power of $x$:
  1. For $x^2$: $-A = 1 \implies A = -1$
  2. For $x$: $-B = 0 \implies B = 0$
  3. Constant term: $2A - C = -1 \implies 2(-1) - C = -1 \implies -2 - C = -1 \implies C = -1$

  This gives the particular solution: $y_p(x) = -x^2 - 1$.

* **Step 3: General Solution.** Combine the homogeneous and particular solutions:
  $$y(x) = y_h(x) + y_p(x) = C_1 e^x + C_2 e^{-x} - x^2 - 1 \quad (C_1, C_2 \in \mathbb{R})$$