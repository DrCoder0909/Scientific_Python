import math

body = {"Sun": (1.988e30, 6.955e5),
        "Merrcury": (3.301e23, 2440.),
        "Venus": (4.867e+24, 6052.),
        "Earth": (5.972e24, 6371.),
        "Mars": (6.417e23, 3390),
        "Jupiter": (1.899e27, 69911.),
        "Saturn": (5.685e26, 58232.),
        "Uranus": (8.682e25, 25362.),
        "Neptune": (1.024e26, 24622.)
        }

planets = list(body.keys())
planets.remove("Sun")


def calc_density(m, r):
    """ Return the density of a sphere with mass m and raius r"""
    return m / (4/3 * math.pi * r**3)


rho = {}
for planet in planets:
    m, r = body[planet]
    rho[planet] = calc_density(m*1000, r*1.e5)

for planet, density in sorted(rho.items()):
    print("The density of {0} is {1:3.2f} g/cm3".format(planet, density))
