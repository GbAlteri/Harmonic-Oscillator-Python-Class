import math
from diatomic import Diatomic

"""
Pytest tests to check the Diatomic Class.

Parameters used
---------------

mass : the reduced mass of the diatomic molecule
k : the spring constant
x_0 : the starting position
v_0 : the starting velocity
t : the time used to calculate the analytical position (or velocity) at the given time (t)
"""


def test_Diatomic_type():
    if not isinstance(Diatomic(1, 1, 1, 0), Diatomic):
        raise TypeError


def test_Diatomic_mass():
    mass = 1
    k = 2
    x_0 = 3
    v_0 = 4
    assert Diatomic(mass, k, x_0, v_0).mass == 1


def test_Diatomic_k():
    mass = 1
    k = 2
    x_0 = 3
    v_0 = 4
    assert Diatomic(mass, k, x_0, v_0).k == 2


def test_Diatomic_x_0():
    mass = 1
    k = 2
    x_0 = 3
    v_0 = 4
    assert Diatomic(mass, k, x_0, v_0).x_0 == 3


def test_Diatomic_v_0():
    mass = 1
    k = 2
    x_0 = 3
    v_0 = 4
    assert Diatomic(mass, k, x_0, v_0).v_0 == 4


def test_Diatomic_omega():
    mass = 1
    k = 2
    x_0 = 3
    v_0 = 4
    assert Diatomic(mass, k, x_0, v_0).omega == math.sqrt(k / mass)


def test_Diatomic_phi():
    mass = 1
    k = 2
    x_0 = 3
    v_0 = 4
    assert Diatomic(mass, k, x_0, v_0).phi == math.atan2(
        v_0, (Diatomic(mass, k, x_0, v_0).omega * x_0)
    )


def test_Diatomic_kinetic_energy():
    mass = 1
    k = 1
    x_0 = 1
    v_0 = 0
    assert Diatomic(mass, k, x_0, v_0).kinetic_energy() == 0


def test_Diatomic_kinetic_energy_2():
    mass = 1
    k = 1
    x_0 = 1
    v_0 = 1
    assert Diatomic(mass, k, x_0, v_0).kinetic_energy() == 0.5 * mass * (v_0**2)


def test_Diatomic_potential_energy():
    mass = 1
    k = 1
    x_0 = 1
    v_0 = 0
    assert Diatomic(mass, k, x_0, v_0).potential_energy() == 0.5 * k * (x_0**2)


def test_Diatomic_potential_energy_2():
    mass = 1
    k = 1
    x_0 = 10
    v_0 = 1
    assert Diatomic(mass, k, x_0, v_0).potential_energy() == 0.5 * k * (x_0**2)


def test_Diatomic_analytical_position():
    mass = 1
    k = 1
    x_0 = 1
    v_0 = 0
    t = 0
    assert Diatomic(mass, k, x_0, v_0).analytical_position(t) == Diatomic(
        mass, k, x_0, v_0
    ).A * (
        math.cos(
            Diatomic(mass, k, x_0, v_0).omega * t + Diatomic(mass, k, x_0, v_0).phi
        )
    )


def test_Diatomic_analytical_position_2():
    mass = 1
    k = 1
    x_0 = 10
    v_0 = 1
    t = 10
    assert Diatomic(mass, k, x_0, v_0).analytical_position(t) == Diatomic(
        mass, k, x_0, v_0
    ).A * (
        math.cos(
            Diatomic(mass, k, x_0, v_0).omega * t + Diatomic(mass, k, x_0, v_0).phi
        )
    )


def test_Diatomic_analytical_velocity():
    mass = 1
    k = 1
    x_0 = 1
    v_0 = 0
    t = 0
    assert Diatomic(mass, k, x_0, v_0).analytical_velocity(t) == -1 * Diatomic(
        mass, k, x_0, v_0
    ).A * (
        math.sin(
            Diatomic(mass, k, x_0, v_0).omega * t + Diatomic(mass, k, x_0, v_0).phi
        )
    )


def test_Diatomic_analytical_velocity_2():
    mass = 1
    k = 1
    x_0 = 10
    v_0 = 1
    t = 0
    assert Diatomic(mass, k, x_0, v_0).analytical_velocity(t) == -1 * Diatomic(
        mass, k, x_0, v_0
    ).A * (
        math.sin(
            Diatomic(mass, k, x_0, v_0).omega * t + Diatomic(mass, k, x_0, v_0).phi
        )
    )




def test_Update_position():
    mass = 1
    k = 1
    x_0 = 10
    v_0 = 1
    t = 0
    mol = Diatomic(mass, k, x_0, v_0)
    kinetic_1 = mol.kinetic_energy()
    mol.update_position(2)
    assert kinetic_1 != mol.kinetic_energy

def test_Update_position_2():
    mass = 1
    k = 1
    x_0 = 10
    v_0 = 1
    t = 0
    mol = Diatomic(mass, k, x_0, v_0)
    potential_1 = mol.potential_energy()
    mol.update_position(2)
    assert potential_1 != mol.potential_energy


def test_Update_velocity():
    mass = 1
    k = 1
    x_0 = 10
    v_0 = 1
    t = 0
    mol = Diatomic(mass, k, x_0, v_0)
    kinetic_1 = mol.potential_energy()
    mol.update_velocity(2)
    assert kinetic_1 != mol.potential_energy


def test_Update_velocity_2():
    mass = 1
    k = 1
    x_0 = 10
    v_0 = 1
    t = 0
    mol = Diatomic(mass, k, x_0, v_0)
    kinetic_1 = mol.kinetic_energy()
    mol.update_velocity(2)
    assert kinetic_1 != mol.kinetic_energy

    