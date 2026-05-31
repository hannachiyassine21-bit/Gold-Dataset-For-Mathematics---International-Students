### Correction DE03

* **Step 1: Homogeneous System.** Solve $y'' + y = 0$. The characteristic equation roots are $r^2 + 1 = 0 \implies r = \pm i$. This yields:
  $$y_h(x) = C_1\cos(x) + C_2\sin(x)$$

* **Step 2: Particular Solution.** The driving force is $f(x) = \cos(x)$. Because $\cos(x)$ is already present within the basic homogeneous kernel, a normal guess fails due to resonance constraints. We must multiply the particular template by $x$:
  $$y_p(x) = x \cdot (A\cos(x) + B\sin(x))$$

  Compute the second derivative of $y_p(x)$:
  $$y_p'(x) = (A\cos(x) + B\sin(x)) + x(-A\sin(x) + B\cos(x))$$
  $$y_p''(x) = -2A\sin(x) + 2B\cos(x) - x(A\cos(x) + B\sin(x))$$

  Substitute $y_p''$ and $y_p$ back into the complete differential equation $(E)$:
  $$[-2A\sin(x) + 2B\cos(x) - y_p(x)] + y_p(x) = \cos(x) \implies -2A\sin(x) + 2B\cos(x) = \cos(x)$$

  By identifying matching side-by-side coefficients: $-2A = 0 \implies A = 0$, and $2B = 1 \implies B = \frac{1}{2}$.
  Thus, $y_p(x) = \frac{1}{2}x\sin(x)$.

* **Step 3: Total Solution.** Combining both systems provides the complete tracking solution output:
  $$y(x) = C_1\cos(x) + C_2\sin(x) + \frac{1}{2}x\sin(x) \quad (C_1, C_2 \in \mathbb{R})$$