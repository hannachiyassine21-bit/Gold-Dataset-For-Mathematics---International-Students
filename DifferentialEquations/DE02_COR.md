### Correction DE02

Write down the characteristic polynomial equation associated with this second-order system:
$$r^2 - 3r + 2 = 0$$

Factoring reveals two distinct real roots: $(r-1)(r-2) = 0 \implies r_1 = 1 \text{ and } r_2 = 2$.
The general baseline equation formula is:
$$y(x) = C_1e^x + C_2e^{2x} \quad (C_1, C_2 \in \mathbb{R})$$

Compute the derivative function to apply velocity boundary limits: $y'(x) = C_1e^x + 2C_2e^{2x}$.
Set up the linear equations using initial values:
1. $y(0) = 0 \implies C_1 + C_2 = 0$
2. $y'(0) = 1 \implies C_1 + 2C_2 = 1$

Subtracting equation (1) from equation (2) gives $C_2 = 1$. Substituting this back yields $C_1 = -1$.
**Conclusion:** The specific solution matching the dataset condition is $y(x) = e^{2x} - e^x$.