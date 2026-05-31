### Correction LIM02

Direct calculation leads to an $\infty - \infty$ indeterminate system. Multiply and divide by the algebraic conjugate expression:
$$f(x) = \frac{(\sqrt{x^2 + x + 1} - x)(\sqrt{x^2 + x + 1} + x)}{\sqrt{x^2 + x + 1} + x} = \frac{(x^2 + x + 1) - x^2}{\sqrt{x^2 + x + 1} + x} = \frac{x + 1}{\sqrt{x^2(1 + \frac{1}{x} + \frac{1}{x^2})} + x}$$

Since $x \to +\infty$, $\sqrt{x^2} = |x| = x$:
$$f(x) = \frac{x(1 + \frac{1}{x})}{x(\sqrt{1 + \frac{1}{x} + \frac{1}{x^2}} + 1)} = \frac{1 + \frac{1}{x}}{\sqrt{1 + \frac{1}{x} + \frac{1}{x^2}} + 1}$$

Taking the limit:
$$\lim_{x \to +\infty} f(x) = \frac{1 + 0}{\sqrt{1 + 0 + 0} + 1} = \frac{1}{2}$$