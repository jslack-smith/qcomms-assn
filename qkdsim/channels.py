# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:24:09 2019

@author: James
"""

from collections import deque
import random


class QuantumChannel(object):
    def __init__(self, adversary, p_loss=0):
        self.p_loss = p_loss
        self.queue = deque([])
        self.adversary = adversary

    def send(self, photon):
        self.queue.append(photon)
        return

    def receive(self):
        sent_photon = self.queue.popleft()

        photon_lost = random.choices([True, False],
                                     weights=[self.p_loss, 1-self.p_loss])[0]
        if photon_lost:
            # TODO need to update, it will be hard to keep track of key indexes
            # e.g. send timing info over classical channel
            return None

        received_photon = self.adversary.measure_resend(sent_photon)
        return received_photon


class ClassicalChannel(object):
    def __init__(self):
        self.queue = deque([])

    def send(self, message):
        self.queue.append(message)
        return

    def receive(self):
        return self.queue.popleft()


if __name__ == '__main__':
    pass
