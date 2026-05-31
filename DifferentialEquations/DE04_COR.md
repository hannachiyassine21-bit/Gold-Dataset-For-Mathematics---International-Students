### Correction DE04

The characteristic equation is $r^2 + 9 = 0 \iff r^2 = -9 \implies r = \pm 3i$.
Since the roots are purely imaginary complex conjugates, the general solution on $\mathbb{R}$ is:
$$y(x) = A \cos(3x) + B \sin(3x) \quad (A, B \in \mathbb{R})$$

Find the derivative to map initial velocity vectors:
$$y'(x) = -3A \sin(3x) + 3B \cos(3x)$$
Apply boundary coordinates:
1. $y(0) = 2 \implies A \cos(0) + B \sin(0) = 2 \implies A = 2$
2. $y'(0) = 0 \implies -3(2)\sin(0) + 3B\cos(0) = 0 \implies 3B = 0 \implies B = 0$

**Conclusion:** The unique solution is $y(x) = 2\cos(3x)$.