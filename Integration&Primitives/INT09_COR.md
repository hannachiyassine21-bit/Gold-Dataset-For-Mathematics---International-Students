### Correction INT09

To evaluate this improper integral, rewrite it as a limit with a variable upper boundary $B$:
$$I = \lim_{B \to +\infty} \int_0^B x e^{-x} dx$$

Apply integration by parts to evaluate the inner integral:
* Let $u = x \implies u' = 1$
* Let $v' = e^{-x} \implies v = -e^{-x}$

$$\int_0^B x e^{-x} dx = \left[ -x e^{-x} \right]_0^B - \int_0^B 1 \cdot (-e^{-x}) dx$$
$$\int_0^B x e^{-x} dx = \left( -B e^{-B} + 0 \right) + \int_0^B e^{-x} dx = -B e^{-B} + \left[ -e^{-x} \right]_0^B$$
$$\int_0^B x e^{-x} dx = -B e^{-B} - e^{-B} + e^0 = -B e^{-B} - e^{-B} + 1$$

Now, take the limit as $B \to +\infty$:
1. By growth hierarchies, $\lim_{B \to +\infty} B e^{-B} = \lim_{B \to +\infty} \frac{B}{e^B} = 0$.
2. The second exponential term also goes to zero: $\lim_{B \to +\infty} e^{-B} = 0$.

Combine the limits:
$$I = 0 - 0 + 1 = 1$$

**Conclusion:** The improper integral converges cleanly to a value of $1$.