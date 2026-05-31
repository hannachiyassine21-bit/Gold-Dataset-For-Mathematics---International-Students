### Correction INT05

* **First Pass Integration by Parts:**
  Let $u = e^x \implies u' = e^x$ and $v' = \cos(x) \implies v = \sin(x)$.
  $$K = [e^x \sin(x)]_0^\pi - \int_0^\pi e^x \sin(x) dx = (0 - 0) - \int_0^\pi e^x \sin(x) dx = -\int_0^\pi e^x \sin(x) dx$$

* **Second Pass Integration by Parts:** Use the new target tracking integral segment:
  Let $u = e^x \implies u' = e^x$ and $v' = \sin(x) \implies v = -\cos(x)$.
  $$\int_0^\pi e^x \sin(x) dx = [-e^x \cos(x)]_0^\pi - \int_0^\pi e^x (-\cos(x)) dx$$
  $$\int_0^\pi e^x \sin(x) dx = (-e^\pi \cos(\pi) - (-e^0 \cos(0))) + \int_0^\pi e^x \cos(x) dx = (e^\pi + 1) + K$$

* **Combine Loops Algebraically:** Substitute back into the expression for $K$:
  $$K = - \left( e^\pi + 1 + K \right) \implies K = -e^\pi - 1 - K$$
  $$2K = -e^\pi - 1 \implies K = \frac{-e^\pi - 1}{2}$$