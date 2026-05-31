### Correction LIM05

* **Step 1: Limit Calculation.**
$$\lim_{x \to +\infty} f(x) = \lim_{x \to +\infty} \sqrt{x^2(1 - \frac{4}{x} + \frac{3}{x^2})} = +\infty$$

* **Step 2: Oblique Asymptote Finding.** Find the slope $a = \lim_{x \to +\infty} \frac{f(x)}{x}$:
$$a = \lim_{x \to +\infty} \frac{\sqrt{x^2(1 - 4/x + 3/x^2)}}{x} = \lim_{x \to +\infty} \frac{|x|\sqrt{1 - 4/x + 3/x^2}}{x}$$
Since $x \to +\infty$, $|x| = x$, so $a = \lim_{x \to +\infty} \sqrt{1 - 4/x + 3/x^2} = 1$.

Now find the intercept $b = \lim_{x \to +\infty} (f(x) - ax)$:
$$b = \lim_{x \to +\infty} (\sqrt{x^2 - 4x + 3} - x) = \lim_{x \to +\infty} \frac{(x^2 - 4x + 3) - x^2}{\sqrt{x^2 - 4x + 3} + x}$$
$$b = \lim_{x \to +\infty} \frac{-4x + 3}{x\sqrt{1 - 4/x + 3/x^2} + x} = \lim_{x \to +\infty} \frac{x(-4 + 3/x)}{x(\sqrt{1 - 4/x + 3/x^2} + 1)} = \frac{-4}{1+1} = -2$$

**Conclusion:** The straight line equation $y = x - 2$ is an oblique asymptote for $\zeta_f$ as $x \to +\infty$.