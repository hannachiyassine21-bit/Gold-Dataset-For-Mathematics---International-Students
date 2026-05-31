### Correction SEQ04

Calculate the difference between two consecutive terms:
$$u_{n+1} - u_n = \frac{(n+1)^2 + 1}{2(n+1)^2} - \frac{n^2 + 1}{2n^2} = \frac{n^2 + 2n + 2}{2(n+1)^2} - \frac{n^2 + 1}{2n^2}$$
Combine over a common denominator:
$$u_{n+1} - u_n = \frac{2n^2(n^2 + 2n + 2) - 2(n^2 + 1)(n^2 + 2n + 1)}{4n^2(n+1)^2} = \frac{-2n - 1}{2n^2(n+1)^2}$$

Since $n \in \mathbb{N}^*$, the numerator $-2n - 1 < 0$ and the denominator is strictly positive, meaning $u_{n+1} - u_n < 0$. The sequence is strictly decreasing.
For boundedness: $u_n = \frac{1}{2} + \frac{1}{2n^2}$. Since $\frac{1}{2n^2} > 0$, $u_n > \frac{1}{2}$ for all $n$. 

**Conclusion:** Being strictly decreasing and bounded below by $\frac{1}{2}$, the sequence converges. Its limit is $\frac{1}{2}$.