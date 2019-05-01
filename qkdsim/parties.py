# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:23:54 2019

@author: James
"""
import random

from qkdsim.photon import M
from qkdsim.hardware import PhotonSource, PhotonDetector

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

    def __init__(self, name='Alice', key=[], sending_bases=[],
                 photon_src=PhotonSource(error_rate=0)):
        self.name = name
        self.key = key
        self.sending_bases = sending_bases
        self.photon_src = photon_src
        self.key_after_sifting = []

    def generate_initial_key(self, length):
        self.key = generate_rand_bits(length)
        return

    def generate_sending_bases(self, length):
        self.sending_bases = generate_rand_bases(length)
        return

    def send_photons(self, quantum_channel):
        generated_photons = []
        for bit, basis in zip(self.key, self.sending_bases):
            photon = self.generate_photon(bit, basis)
            quantum_channel.send(photon)
            # create two identical photons, for printing table
            generated_photons.append(self.generate_photon(bit, basis))
        return generated_photons

    def generate_photon(self, bit, basis):
        return self.photon_src.generate_photon(bit, basis)


class Receiver(object):
    def __init__(self, name='Bob', key=[], receiving_bases=[],
                 photon_detector=PhotonDetector(loss_rate=0)):
        self.name = name
        self.key = key
        self.receiving_bases = receiving_bases
        self.photon_detector = photon_detector
        self.key_after_sifting = []

    def generate_receiving_bases(self, length):
        self.receiving_bases = generate_rand_bases(length)
        return

    def receive_photons(self, quantum_channel):
        for i in range(0, len(self.receiving_bases)):
            photon = quantum_channel.receive()
            self.key[i] = self.detect_photon(photon, self.receiving_bases[i])
        return

    def detect_photon(self, photon, basis):
        return self.photon_detector.detect_photon(photon, basis)

    def send_bases(self, cl_chan):
        cl_chan.send(self.receiving_bases)
        return


class Adversary(object):
    def __init__(self,
                 name='Eve',
                 photon_source=PhotonSource(error_rate=0),
                 photon_detector=PhotonDetector(loss_rate=0),
                 p_meas=0
                 ):
        self.name = name
        self.key = []
        self.bases = []
        self.photon_detector = photon_detector
        self.photon_source = photon_source
        self.p_meas = p_meas

    def measure_resend(self, photon):
        # if eve chooses to measure
        if random.choices([True, False], [self.p_meas, 1-self.p_meas])[0]:
            # choose random basis
            m = random.choice([M(0), M(45)])
            self.bases.append(m)
            # measure photon
            measurement_outcome = self.detect_photon(photon, m)
            self.key.append(measurement_outcome)
            # generate new photon
            new_photon = self.generate_photon(measurement_outcome, m)
            return new_photon
        else:
            return photon

    def detect_photon(self, photon, basis):
        return self.photon_detector.detect_photon(photon, basis)

    def generate_photon(self, bit, basis):
        return self.photon_source.generate_photon(bit, basis)

    def get_adversary_generated_photons(self):
        generated_photons = []
        for bit, basis in zip(self.key, self.bases):
            generated_photons.append(self.generate_photon(bit, basis))
        return generated_photons


def generate_rand_bits(length):
    randBits = random.choices([0, 1], k=length)
    return randBits


def generate_rand_bases(length):
    randBases = random.choices([M(0), M(45)], k=length)
    return randBases


if __name__ == '__main__':
    pass
