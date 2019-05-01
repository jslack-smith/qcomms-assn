# -*- coding: utf-8 -*-
"""
This module contains the class for the BB84 protocol and main() to run it
"""

from qkdsim.parties import Sender, Receiver, Adversary
from qkdsim.channels import QuantumChannel, ClassicalChannel
from qkdsim.displayer import ConsoleTablePrinter, DisplayNothing
# from qkdsim.hardware import PhotonSource, PhotonDetector
# from qkdsim.errorcorrection import parity_check

# from numpy.ma.core import empty
import copy


def main():
    alice = Sender()
    bob = Receiver()
    eve = Adversary(p_meas=1)

    qu_chan = QuantumChannel(eve, p_loss=0)
    cl_chan = ClassicalChannel()

    initial_key_length = 50

    qkd = BB84(alice, bob, eve, initial_key_length, qu_chan,
               cl_chan, ConsoleTablePrinter())

    qkd.run()
    return


class BB84(object):
    """
    BB84 protocol

    Parameters
    ----------
    sender: Sender
        aka Alice

    receiver: receiver
        aka Bob

    adversary: Adversary
        aka Eve

    init_key_len: int
        Initial length of the random bit array generated by the sender
        which will become the shared secret key

    qu_chan: QuantumChannel
        Quantum channel used to share photons between sender and receiver

    cl_chan: ClassicalChannel
        Classical channel used to share messages between sender and receiver
    """

    def __init__(self,
                 sender=Sender(),
                 receiver=Receiver(),
                 adversary=Adversary(),
                 init_key_len=10,
                 qu_chan=None,
                 cl_chan=ClassicalChannel(),
                 displayer=DisplayNothing()):
        self.sender = sender
        self.receiver = receiver
        self.adversary = adversary
        if qu_chan is None:
            qu_chan = QuantumChannel(adversary=adversary)
        self.qu_chan = qu_chan
        self.cl_chan = cl_chan
        self.n = init_key_len
        self.displayer = displayer

    def run(self):
        self.initialise()
        self.send_key_as_photons()
        self.sift_keys()
        self.correct_keys()
        self.privacy_amplification()
        return

    def initialise(self):
        """
        Initialise QKD

        Generate random key and bases for sender.
        Generate random bases for receiver.
        """
        self.sender.generate_initial_key(self.n)
        self.sender.generate_sending_bases(self.n)
        self.receiver.generate_receiving_bases(self.n)

        self.display_initialise()
        return

    def send_key_as_photons(self):
        """
        * generate photons from sender's key and bases
        * send them through the quantum channel to receiver
        * generate random bases for receiver
        * generate receiver's initial key by measuring photons
        """
        self.receiver.generate_receiving_bases(self.n)
        self.receiver.key = [None] * self.n  # TODO update for future loss
        generated_photons = self.sender.send_photons(self.qu_chan)
        self.receiver.receive_photons(self.qu_chan)
        self.display_send_key_as_photons(generated_photons)
        return

    def sift_keys(self):
        """
        Communicate over classical channel to establish which photons
        receiver measured in correct basis and remove incorrect or missing
        bits from both sender's and receiver's keys
        """
        # Receiver sends measuring bases to Sender
        self.cl_chan.send(self.receiver.receiving_bases)
        # Sender compares her bases with Receiver bases
        good_measures = self.compare_bases(self.sender.sending_bases,
                                           self.cl_chan.receive())
        # Sender sends which measures were correct to Receiver
        # self.cl_chan.send(good_measures)
        # Receiver sifts its key
        receiver_sifted_key_print = self.sift_key(self.receiver, good_measures)
        # Sender sifts its key
        sender_sifted_key_print = self.sift_key(self.sender, good_measures)

        self.display_sift_keys(good_measures, sender_sifted_key_print,
                               receiver_sifted_key_print)
        return

    def compare_bases(self, a_bases, b_bases):
        compare_result = [a == b for (a, b) in zip(a_bases, b_bases)]
        return compare_result

    def sift_key(self, party, measures):
        party_key = party.key
        party_key_printing = copy.deepcopy(party.key)
        for i in range(len(measures)-1, -1, -1):
                if(measures[i] is True):
                    pass
                else:
                    party_key_printing[i] = 'x'
                    del(party_key[i])
        party.key = party_key
        return party_key_printing

    def correct_keys(self):
        """
        Communicate subset of key over classical channel to estimate error
        and remove shared bits
        """
        self.display_correct_keys()
        return

    def privacy_amplification(self):
        """
        Communicate subset of key over classical channel to estimate error
        and remove shared bits
        """
        self.display_privacy_amplification()
        return

    def display_initialise(self):
        self.displayer.display_initialise(
                self.sender.name,
                self.sender.key,
                self.sender.sending_bases,
                )
        return

    def display_send_key_as_photons(self, gend_photons):
        self.displayer.display_send_key_as_photons(
                self.sender.name,
                gend_photons,
                self.adversary.name,
                self.adversary.bases,
                self.adversary.key,
                self.adversary.get_adversary_generated_photons(),
                self.receiver.name,
                self.receiver.receiving_bases,
                self.receiver.key
                )
        return

    def display_sift_keys(self, good_measures, sender_key_p, receiver_key_p):
        self.displayer.display_sift_keys(good_measures,
                                         self.sender.name,
                                         self.receiver.name,
                                         sender_key_p,
                                         receiver_key_p
                                         )
        return

    def display_correct_keys(self):
        self.displayer.display_correct_keys()
        return

    def display_privacy_amplification(self):
        self.displayer.display_privacy_amplification()
        return


if __name__ == '__main__':
    main()
