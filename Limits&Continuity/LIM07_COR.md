### Correction LIM07

Direct substitution yields the indeterminate form $\frac{0}{0}$. Multiply and divide the fraction by the conjugate of the numerator:
$$\frac{\sqrt{x + 3} - 2}{x - 1} = \frac{(\sqrt{x + 3} - 2)(\sqrt{x + 3} + 2)}{(x - 1)(\sqrt{x + 3} + 2)} = \frac{(x + 3) - 4}{(x - 1)(\sqrt{x + 3} + 2)}$$
$$\frac{x - 1}{(x - 1)(\sqrt{x + 3} + 2)} = \frac{1}{\sqrt{x + 3} + 2} \quad (\text{for } x \neq 1)$$

Now, evaluate the limit of the simplified expression:
$$\lim_{x \to 1} \frac{1}{\sqrt{x + 3} + 2} = \frac{1}{\sqrt{1 + 3} + 2} = \frac{1}{2 + 2} = \frac{1}{4}$$