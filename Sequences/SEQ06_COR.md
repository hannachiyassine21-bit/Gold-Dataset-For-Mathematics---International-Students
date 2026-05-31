### Correction SEQ06

1. **Monotonicity and Bounds:**
For $x \in [0, 1]$, $x^{n+1} \le x^n$. Since $1 + x^2 > 0$:
$$I_{n+1} - I_n = \int_0^1 \frac{x^{n+1} - x^n}{1 + x^2} dx = \int_0^1 \frac{x^n(x - 1)}{1 + x^2} dx$$
On the interval $[0, 1]$, $x \le 1 \implies x - 1 \le 0$, while $x^n \ge 0$. The integrand is negative, so $I_{n+1} - I_n \le 0$. The sequence is decreasing. 
Since $x^n \ge 0$ and $1 + x^2 > 0$ on $[0, 1]$, the integral $I_n \ge 0$ for all $n$. It is bounded below by $0$.

2. **Limit Calculation:**
For all $x \in [0, 1]$, we can bound the denominator: $1 \le 1 + x^2 \le 2 \implies \frac{1}{2} \le \frac{1}{1 + x^2} \le 1$.
Multiply by $x^n \ge 0$:
$$0 \le \frac{x^n}{1 + x^2} \le x^n$$
Integrating across the boundaries from $0$ to $1$:
$$0 \le I_n \le \int_0^1 x^n dx \implies 0 \le I_n \le \left[ \frac{x^{n+1}}{n+1} \right]_0^1 \implies 0 \le I_n \le \frac{1}{n+1}$$
Since $\lim_{n \to \infty} \frac{1}{n+1} = 0$, by the Squeeze Theorem (Théorème des Gendarmes), $\lim_{n \to \infty} I_n = 0$.