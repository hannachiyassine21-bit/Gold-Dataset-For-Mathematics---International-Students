### Correction SEQ03

1. If $u_n \in ]0, 1[$, then $u_n^2 < u_n \implies u_n - u_n^2 > 0$. Also, the function $f(x) = x - x^2$ reaches its maximum at $x = \frac{1}{4} < 1$. Thus $u_{n+1} \in ]0, 1[$. Since $u_{n+1} - u_n = -u_n^2 < 0$, the sequence is strictly decreasing and bounded below by 0, so it converges to a real value $L$ where $L = L - L^2 \implies L = 0$.

2. Write the transformation:
$$\frac{1}{u_{n+1}} - \frac{1}{u_n} = \frac{1}{u_n - u_n^2} - \frac{1}{u_n} = \frac{1}{u_n(1-u_n)} - \frac{1}{u_n} = \frac{1 - (1-u_n)}{u_n(1-u_n)} = \frac{1}{1-u_n}$$

Since $\lim_{n \to \infty} u_n = 0$, we have $\lim_{n \to \infty} \left(\frac{1}{u_{n+1}} - \frac{1}{u_n}\right) = \frac{1}{1-0} = 1$. By algebraic properties of running averages, $\frac{1}{u_n} \sim n$, which explicitly proves that $\lim_{n \to \infty} (n \cdot u_n) = 1$.