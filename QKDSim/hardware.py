# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:24:21 2019

@author: James
"""

from photon import Photon
from photon import M

class PhotonSource(object):
    def __init__(self, error_rate):
        self.error_rate = error_rate  # TODO error rate not used

    def generate_photon(self, angle):
        return Photon(angle)


class PhotonDetector(object):
    def __init__(self, loss_rate):
        self.loss_rate = loss_rate
        
    def detect_photon(self, Photon, basis):
        return Photon.measure(basis.angle)

if __name__ == '__main__':
    pass
