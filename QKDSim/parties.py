# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:23:54 2019

@author: James
"""
import numpy as np
import random
from photon import M

# TODO make superclass for Sender and Receiver


class Sender(object):
    """
    Sender (aka Alice)

    Parameters
    ----------
    key: np.array
    sending_bases: np.array(dtype=int)
    photon_src: PhotonSource
    """

    def __init__(self, name='sender', key=[], sending_bases=[],
                 photon_src=None, qu_chan=None, cl_chan=None):
        self.name = name
        self.key = key
        self.sending_bases = sending_bases
        self.photon_src = photon_src
        self.qu_chan = qu_chan
        self.cl_chan = cl_chan

    def generate_initial_key(self, length):
        self.key = generate_rand_bits(length)
        return

    def generate_sending_bases(self, length):
        self.sending_bases = generate_rand_bases(length)
        return

    def send_photons(self):
        q = self.qu_chan
        for bit in self.key:
            q.send()  # TODO finish
        return


class Receiver(object):
    def __init__(self, name='receiver', key=[], receiving_bases=[],
                 photon_detector=None, qu_chan=None, cl_chan=None):
        self.name = name
        self.key = key
        self.receiving_bases = receiving_bases
        self.photon_detector = photon_detector
        self.qu_chan = qu_chan
        self.cl_chan = cl_chan

    def generate_receiving_bases(self, length):
        self.receiving_bases = generate_rand_bases(length)
        return

    def receive_photons(self):
        pass
        return


class Adversary(object):
    def __init__(self, evesdrop_rate=0):
        self.evesdrop_rate = evesdrop_rate


def generate_rand_bits(length):
    randBits = np.random.randint(0, 2, length)
    return randBits


def generate_rand_bases(length):
    randBases = random.choices([M(0), M(45)], k=length)
    return randBases


if __name__ == '__main__':
    pass
