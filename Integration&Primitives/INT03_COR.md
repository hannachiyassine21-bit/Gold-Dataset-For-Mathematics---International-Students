### Correction INT03

Deconstruct the power structure inside the integrand:
$$I_{n+2} = \int_0^{\pi/2} \sin(x) \cdot (\sin(x))^{n+1} dx$$

Set up integration by parts steps:
* Let $u(x) = (\sin(x))^{n+1} \implies u'(x) = (n+1)\cos(x)(\sin(x))^n$
* Let $v'(x) = \sin(x) \implies v(x) = -\cos(x)$

Applying the formula:
$$I_{n+2} = [-\cos(x)(\sin(x))^{n+1}]_0^{\pi/2} - \int_0^{\pi/2} -(n+1)\cos^2(x)(\sin(x))^n dx$$

The left bracket boundary evaluation evaluates to $0$ because $\cos(\pi/2)=0$ and $\sin(0)=0$.
$$I_{n+2} = (n+1)\int_0^{\pi/2} (1 - \sin^2(x))(\sin(x))^n dx$$
$$I_{n+2} = (n+1)\int_0^{\pi/2} (\sin(x))^n dx - (n+1)\int_0^{\pi/2} (\sin(x))^{n+2} dx$$
$$I_{n+2} = (n+1)I_n - (n+1)I_{n+2}$$

Isolate the matching $I_{n+2}$ term algebraically:
$$I_{n+2} + (n+1)I_{n+2} = (n+1)I_n \implies (n+2)I_{n+2} = (n+1)I_n \implies I_{n+2} = \frac{n+1}{n+2}I_n$$