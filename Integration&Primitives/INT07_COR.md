### Correction INT07

Use the cosine double-angle identity to linearize the squared term:
$$\cos^2(x) = \frac{1 + \cos(2x)}{2}$$

Substitute this identity into the integral:
$$I = \int_0^{\pi/2} \frac{1 + \cos(2x)}{2} dx = \frac{1}{2} \int_0^{\pi/2} (1 + \cos(2x)) dx$$

Find the primitive function for the integrand:
$$I = \frac{1}{2} \left[ x + \frac{\sin(2x)}{2} \right]_0^{\pi/2}$$

Evaluate the primitive at the upper and lower integration limits:
$$I = \frac{1}{2} \left( \left( \frac{\pi}{2} + \frac{\sin(\pi)}{2} \right) - \left( 0 + \frac{\sin(0)}{2} \right) \right)$$
Since $\sin(\pi) = 0$ and $\sin(0) = 0$:
$$I = \frac{1}{2} \left( \frac{\pi}{2} + 0 - 0 \right) = \frac{\pi}{4}$$