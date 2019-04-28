# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:24:21 2019

@author: James
"""

from photon import Photon
from photon import M
import random
import numpy as np

class PhotonSource(object):
    def __init__(self, error_rate):
        self.error_rate = error_rate  # TODO error rate not used

    def generatePhoton(self, angle):
        photon_error = random.choices([True, False], 
                                     weights=[self.error_rate, 1-self.error_rate])    
        if photon_error:
                # TODO need to update, it will be hard to keep track of key indexes
                # e.g. send timing info over classical channel
                return None  
        else:
                return Photon(angle)


class PhotonDetector(object):
    def __init__(self, loss_rate):
        self.loss_rate = loss_rate
        
    def detectPhoton(self, Photon, basis):
        return Photon.measure(basis.angle)

if __name__ == '__main__':
    pass
