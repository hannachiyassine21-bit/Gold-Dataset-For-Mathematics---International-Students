### Correction DE08

The equation is in the standard linear format $y' + P(x)y = Q(x)$, where $P(x) = 2$.
Compute the integrating factor, $I(x)$:
$$I(x) = e^{\int P(x) dx} = e^{\int 2 dx} = e^{2x}$$

Multiply every term in the differential equation by this integrating factor:
$$e^{2x} y' + 2 e^{2x} y = e^{2x} e^x \implies \frac{d}{dx} \left( e^{2x} y \right) = e^{3x}$$

Integrate both sides with respect to $x$:
$$e^{2x} y = \int e^{3x} dx \implies e^{2x} y = \frac{1}{3} e^{3x} + C \quad (\text{where } C \in \mathbb{R})$$

Isolate $y$ by multiplying the entire equation by $e^{-2x}$:
$$y(x) = \frac{1}{3} e^x + C e^{-2x}$$