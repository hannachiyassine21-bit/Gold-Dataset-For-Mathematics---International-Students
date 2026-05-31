### Correction DIF04

Using the quotient differentiation rule layout where $u(x) = 2x+1 \implies u'(x)=2$ and $v(x) = x^2+3 \implies v'(x)=2x$:
$$f'(x) = \frac{u'v - uv'}{v^2} = \frac{2(x^2 + 3) - (2x + 1)(2x)}{(x^2 + 3)^2}$$
$$f'(x) = \frac{2x^2 + 6 - 4x^2 - 2x}{(x^2 + 3)^2} = \frac{-2x^2 - 2x + 6}{(x^2 + 3)^2} = \frac{-2(x^2 + x - 3)}{(x^2 + 3)^2}$$

Find roots for the numerator: $\Delta = (1)^2 - 4(1)(-3) = 13$. The solutions are $x_1 = \frac{-1-\sqrt{13}}{2}$ and $x_2 = \frac{-1+\sqrt{13}}{2}$.
* For $x \in ]x_1, x_2[$, $f'(x) > 0 \implies f$ is strictly increasing.
* For $x \in ]-\infty, x_1[ \cup ]x_2, +\infty[$, $f'(x) < 0 \implies f$ is strictly decreasing.