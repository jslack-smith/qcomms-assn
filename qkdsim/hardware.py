# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:24:21 2019

@author: James
"""
import random
import numpy as np

from qkdsim.photon import Photon
from qkdsim.photon import M


class PhotonSource(object):
    def __init__(self, error_rate):
        self.error_rate = error_rate  # TODO error rate not used

    def generate_photon(self, bit, basis):
        photon_error = random.choices([True, False],
                                      weights=[self.error_rate,
                                               1-self.error_rate])[0]
        if photon_error:
            # TODO need to update, 
            # it will be hard to keep track of key indexes
            # e.g. send timing info over classical channel
            return None
        else:
            photon_angle = np.degrees(basis.angle + bit*np.deg2rad(90))
            return Photon(photon_angle)


class PhotonDetector(object):
    def __init__(self, loss_rate):
        self.loss_rate = loss_rate

    def detect_photon(self, photon, basis):
        return photon.measure(basis.angle)


if __name__ == '__main__':
    src = PhotonSource(0)
    basis = M(0)
    photon1 = src.generate_photon(0, basis)
    print(src.generate_photon(0, basis))
    print(src.generate_photon(1, basis))
    basis = M(45)
    print(src.generate_photon(0, basis))
    print(src.generate_photon(1, basis))
