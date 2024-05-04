import math


class NegativeMass(ValueError):
    pass


class NegativeSpringConstant(ValueError):
    pass


class PositionOutOfRange(ValueError):
    pass


class VelocityOutOfRange(ValueError):
    pass


class Diatomic:
    """
    This Class build a diatomic molecule Object

    Parameters
    ---------------

    mass : float
        the reduced mass of the diatomic molecule
    k : float
        the spring constant
    x_0 : float
        the starting position
    v_0 : float
        the starting velocity
    """

    def __init__(self, mass: float, k: float, x_0: float, v_0: float):
        if mass < 0:
            raise NegativeMass("Mass is < 0! Absurd! Only > 0 accepted.")
        if k < 0:
            raise NegativeSpringConstant(
                "Spring constant is < 0! Absurd! Only > 0 accepted."
            )

        self.mass = mass
        self.k = k
        self.x_0 = x_0
        self.x = x_0
        self.v_0 = v_0
        self.constant_energy = (0.5 * self.k * (self.x_0**2)) + (
            0.5 * self.mass * (self.v_0**2)
        )
        self.v = math.sqrt(
            (2 * (self.constant_energy - self.potential_energy()) / self.mass)
        )
        self.omega = math.sqrt(self.k / self.mass)
        self.A = math.sqrt((2 * self.total_energy()) / self.k)
        self.phi = math.atan2(self.v_0, (self.omega * self.x_0))

    def update_position(self, new_x: float):
        """
        Update position and velocity.

        Parameters
        ----------
        new_x : float
            The new position.
        """
        if 0.5 * self.k * (new_x**2) > self.constant_energy:
            raise PositionOutOfRange(
                "New position led to a new Potential Energy > Total Energy! Absurd!"
            )
        else:
            self.x = new_x
            self.v = math.sqrt(
                (2 * (self.constant_energy - self.potential_energy()) / self.mass)
            )

    def update_velocity(self, new_v: float):
        """
        Update velocity and position.

        Parameters
        ----------
        new_v : float
            The new velocity.
        """

        if 0.5 * self.mass * (new_v**2) > self.constant_energy:
            raise VelocityOutOfRange(
                "New velocity led to a new Kinetic Energy > Total Energy! Absurd!"
            )
        else:
            self.v = new_v
            self.x = math.sqrt(
                2 * (self.constant_energy - self.kinetic_energy()) / self.k
            )

    def total_energy(self):
        """
        Calculate the total energy of the system (constant).
        """
        return (0.5 * self.k * (self.x_0**2)) + (
            0.5 * self.mass * (self.v_0**2)
        )  # The total energy remains constant given x_0 and v_0

    def potential_energy(self):
        """
        Calculate the potential energy
        """
        return 0.5 * self.k * (self.x**2)

    def kinetic_energy(self):
        """
        Calculate the kinetic energy
        """
        return 0.5 * self.mass * (self.v**2)

    def analytical_position(self, t):
        """
        Calculate the analytical position

        Parameters
        ----------
        t : float
            the time used to calculate the analytical position
        """
        return (self.A) * (math.cos((self.omega * t) + self.phi))

    def analytical_velocity(self, t):
        """
        Calculate the analytical velocity

        Parameters
        ----------
        t : float
            the time used to calculate the analytical velocity
        """
        return -1 * self.A * self.omega * math.sin((self.omega * t) + self.phi)

    def force(self):
        """
        Calculate the force using Hooke's Law.
        """
        return -1 * self.k * self.x
