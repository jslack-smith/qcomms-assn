# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:24:30 2019

@author: James
"""

import numpy as np


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
        self.theta = theta
        self.state_vector = np.array([np.cos(theta), np.sin(theta)])


if __name__ == '__main__':
    pass
