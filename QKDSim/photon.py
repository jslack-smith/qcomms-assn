# -*- coding: utf-8 -*-
"""
This module contains Photon class and related helper functions
"""

import numpy as np
import random


class Photon(object):
    """
    Create a photon defined by polarisation angle

    Parameters
    ----------
    theta: int
        default is 0
        polarisation angle in degrees

    state_vector: np.array
        state vector in rectilinear basis
    """

    def __init__(self, theta=0):
        # TODO angle checking
        th = np.deg2rad(theta)
        self.theta = th
        self.state_vector = np.array([[np.cos(th), np.sin(th)]]).T

    """
    Measure photon linear polarisation with respect to a measurement basis
    defined by polarisation angle alpha (updating the photon's state)

    Parameters
    ----------
    alpha: int
        measurement basis angle with respect to horizontal in degrees

    Return
    ------
    outcome: int
        measurement outcome (0 or 1)
        #TODO is there a better type to restrict value to 0 or 1 (without
        logic connotation of boolean)
    """
    def measure(self, alpha):
        m = M(alpha).matrix
        p = [calc_meas_prob(self.state_vector, meas_vec) for meas_vec in m.T]
        outcome = random.choices([0, 1], weights=[p[0], p[1]])[0]
        self.state_vector = m[:, [outcome]]
        self.theta = calc_polarisation_angle(self.state_vector)
        return outcome

    def __str__(self):
        """Compute printable representation"""
        string = 'polarisation angle:\n{} {}\n'.format(np.degrees(self.theta),
                                                       self.arrow())
        string += 'state vector:\n{}'.format(self.state_vector)
        return string

    def arrow(self):
        """Return UTF-8 arrow for photons in basis states"""
        if np.isclose(self.theta, 0):
            return '⭢'
        elif np.isclose(self.theta, np.pi/2):
            return '⭡'
        elif np.isclose(self.theta, np.pi/4):
            return '⭧'
        elif np.isclose(self.theta, 3*np.pi/4):
            return '⭦'
        else:
            return ''


class M(object):
    def __init__(self, angle):
        self.angle = np.deg2rad(angle)
        self.matrix = self.m_alpha(angle)
        self.char = self.to_char(self.angle)

    def m_alpha(self, alpha):
        a = np.deg2rad(alpha)
        m = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
        return m

    def to_char(self, angle):
        if np.isclose(angle, 0):
            return 'R'
        elif np.isclose(angle, np.pi/4):
            return 'D'
        else:
            return ''

    def __repr__(self):
        return self.char


def calc_meas_prob(psi, m):
    """
    Calculate probability using ket psi and measurement basis vector m
    """
    # np.dot() returns 1x1 np.array(), .item() converts to scalar
    return (np.abs(np.dot(psi.T, m).item()))**2


def calc_polarisation_angle(psi):
    """ Calculate polarisation angle of state vector psi"""
    return np.arccos(np.dot(psi.T, np.array([[1, 0]]).T))


if __name__ == '__main__':
    np.set_printoptions(precision=3, suppress=True)

    angles = [0, 45, 90, 135]
    for a in angles:
        photon = Photon(a)
        print('Angle: {}\nPhoton:\n{}\n'.format(a, photon))

    # calculate average outcome of repeated experiments
    N = 1000    # number of experiments
    theta = 0   # photon polarisation
    alpha = 45  # measurement basis polarisation
    s = 0       # sum of outcomes (for calculating average)
    for i in range(N):
        photon = Photon(theta)
        s += photon.measure(alpha)

    avg_outcome = s/N
    print('\nMeasurement test:')
    print('{}\nM({})\n{} trials'.format(Photon(theta).arrow(), alpha, N))
    print('Average outcome: {}'.format(avg_outcome))
    print(photon)
    