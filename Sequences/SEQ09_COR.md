### Correction SEQ09

Rewrite the expression for $S_n$ by factoring out $n^2$ from the denominator to match a standard Riemann sum template:
$$S_n = \sum_{k=1}^n \frac{n}{n^2\left(1 + \left(\frac{k}{n}\right)^2\right)} = \frac{1}{n} \sum_{k=1}^n \frac{1}{1 + \left(\frac{k}{n}\right)^2}$$

This expression matches the Riemann sum for the continuous function $f(x) = \frac{1}{1 + x^2}$ on the interval $[0, 1]$, with a step size of $\Delta x = \frac{1}{n}$.
As $n \to +\infty$, the sum converges to the definite integral of $f(x)$:
$$\lim_{n \to +\infty} S_n = \int_0^1 \frac{1}{1 + x^2} dx$$

Evaluate the integral using its primitive function, $\arctan(x)$:
$$\int_0^1 \frac{1}{1 + x^2} dx = \left[ \arctan(x) \right]_0^1 = \arctan(1) - \arctan(0) = \frac{\pi}{4} - 0 = \frac{\pi}{4}$$

**Conclusion:** The limit of the sequence is $\frac{\pi}{4}$.