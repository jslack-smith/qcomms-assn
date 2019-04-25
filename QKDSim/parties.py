# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:23:54 2019

@author: James
"""
import numpy as np
import random
from photon import M
from channels import QuantumChannel
from channels import ClassicalChannel

class Sender(object):
    """
    Sender (aka Alice)

    Parameters
    ----------
    key: np.array
    sending_bases: np.array(dtype=int)
    photon_src: PhotonSource
    """

    def __init__(self, key=[], sending_bases=[], photon_src=None, 
                 qu_chan, cl_chan):
        self.key = key
        self.sending_bases = sending_bases
        self.photon_src = photon_src

    def generateInitialKey(self, length):
        self.key = generateRandBits(length)
        return

    def generateSendingBases(self, length):
        self.sending_bases = generateRandBases(length)
        return
    
    def sendPhotons(self):
        
        return


class Reciever(object):
    def __init__(self, key=[], recieving_bases=[], photon_detector=None,
                 qu_chan, cl_chan):
        self.key = key
        self.recieving_bases = recieving_bases
        self.photon_detector = photon_detector

    def generateRecievingBases(self, length):
        self.recieving_bases = generateRandBases(length)
        return
    
    def recievePhotons(self):


class Adversary(object):
    def __init__(self, evesdrop_rate=0):
        self.evesdrop_rate = evesdrop_rate


def generateRandBits(length):
    randBits = np.random.randint(0, 2, length)
    return randBits


def generateRandBases(length):
    randBases = random.choices([M(0), M(45)], k=length)
    return randBases


if __name__ == '__main__':
    pass