### Correction INT02

Let's assign our integration parts variables systematically:
* Let $u(x) = x \implies u'(x) = 1$
* Let $v'(x) = \sin(x) \implies v(x) = -\cos(x)$

Applying the integration by parts rule $\int uv' = [uv] - \int u'v$:
$$J = [-x \cdot \cos(x)]_0^\pi - \int_0^\pi 1 \cdot (-\cos(x)) dx$$
$$J = (-\pi \cdot \cos(\pi) - 0) + \int_0^\pi \cos(x) dx$$

Since $\cos(\pi) = -1$:
$$J = \pi + [\sin(x)]_0^\pi = \pi + (\sin(\pi) - \sin(0)) = \pi$$