# -*- coding: utf-8 -*-
"""
This module contains the class for the BB84 protocol and main() to run it
"""

from parties import Sender
from parties import Reciever
from parties import Adversary
from channels import QuantumChannel
from channels import ClassicalChannel


def main():
    alice = Sender()
    bob = Reciever()
    eve = Adversary()
    qu_chan = QuantumChannel(0)
    cl_chan = ClassicalChannel()

    qkd_run = BB84(alice, bob, eve, 10, qu_chan, cl_chan, verbose=True)

    qkd_run.initialise()
    
    qkd_run.send_key_as_photons()
    
    
    qkd_run.sift_keys()
    qkd_run.estimate_error()

    return


class BB84(object):
    """
    BB84 protocol

    Parameters
    ----------
    sender: Sender
        aka Alice

    reciever: Reciever
        aka Bob

    adversary: Adversary
        aka Eve

    init_key_len: int
        Initial length of the random bit array generated by the sender
        which will become the shared secret key

    qu_chan: QuantumChannel
        Quantum channel used to share photons between sender and reciever

    cl_chan: ClassicalChannel
        Classical channel used to share messages between sender and reciever
    """

    def __init__(self, sender, reciever, adversary, init_key_len,
                 qu_chan, cl_chan, verbose=False):
        self.sender = sender
        self.reciever = reciever
        self.adversary = adversary
        self.qu_chan = qu_chan
        self.cl_chan = cl_chan
        self.n = init_key_len
        self.verbose = verbose

    def initialise(self):
        """
        Initialise QKD

        Generate random key for sender and random bases for sender and reciever
        """
        self.sender.generateInitialKey(self.n)
        self.sender.generateSendingBases(self.n)
        self.reciever.generateRecievingBases(self.n)
        
        self.sender.qu_chan = self.qu_chan
        self.reciever.qu_chan = self.qu_chan
        self.sender.cl_chan = self.cl_chan
        self.reciever.cl_chan = self.cl_chan
        
        self.print_status()


    def send_key_as_photons(self):
        """
        * generate photons from sender's key and bases
        * send them through the quantum channel to reciever
        * generate reciever's initial key by measuring photons
        """
        
        
        self.print_status()

    def sift_keys(self):
        """
        Communicate over classical channel to establish which photons
        reciever measured in correct basis and remove incorrect or missing
        bits from both sender's and reciever's keys
        """
        self.print_status()

    def estimate_error(self):
        """
        Communicate subset of key over classical channel to estimate error
        and remove shared bits
        """
        self.print_status()
    
    def print_status(self):
        if not self.verbose:
            return
        # TODO make printing functions in parties' classes
        print("Sender's key:")
        print(self.sender.key)
        print("Alice's sending bases:")
        print(self.sender.sending_bases)
        print("Bob's recieving bases:")
        print(self.reciever.recieving_bases)
        print("Bob's key:")
        print(self.reciever.key)
        return

if __name__ == '__main__':
    main()
