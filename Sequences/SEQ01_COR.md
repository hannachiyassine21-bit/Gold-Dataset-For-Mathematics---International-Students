### Correction SEQ01

* **Initialization:** For $n = 0$, $u_0 = 2$, and $2 < 6$. The property is true for $n = 0$.
* **Heredity:** Assume that $u_n < 6$ for a given $n \in \mathbb{N}$. We want to prove $u_{n+1} < 6$.
  $$u_n < 6 \implies \frac{1}{2}u_n < 3 \implies \frac{1}{2}u_n + 3 < 3 + 3 \implies u_{n+1} < 6$$
* **Conclusion:** By the principle of induction, $u_n < 6$ for all $n \in \mathbb{N}$.