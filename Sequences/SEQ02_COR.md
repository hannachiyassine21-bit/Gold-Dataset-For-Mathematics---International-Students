### Correction SEQ02

Calculate the difference between consecutive terms:
$$v_{n+1} - v_n = \frac{3(n+1) - 1}{(n+1) + 2} - \frac{3n - 1}{n + 2} = \frac{3n + 2}{n + 3} - \frac{3n - 1}{n + 2}$$
$$v_{n+1} - v_n = \frac{(3n+2)(n+2) - (3n-1)(n+3)}{(n+3)(n+2)} = \frac{7}{(n+3)(n+2)}$$

Since $n \in \mathbb{N}$, $7 > 0$ and the denominator is positive, $v_{n+1} - v_n > 0$, so $(v_n)$ is strictly increasing. 

For boundedness: $v_0 = -\frac{1}{2}$. As $n \to +\infty$, $v_n = \frac{n(3 - 1/n)}{n(1 + 2/n)} \to 3$. Thus, $-\frac{1}{2} \le v_n < 3$. Being increasing and upper-bounded by 3, it converges to $3$.