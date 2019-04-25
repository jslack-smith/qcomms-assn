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
    
    qkd_run = BB84(alice, bob, eve, 10)
    
    


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
                 qu_chan, cl_chan):
        self.sender = sender
        self.reciever = reciever
        self.adversary = adversary
        self.qu_chan = qu_chan
        self.cl_chan = cl_chan
        
    def initialise(self):
        """ 
        Initialise QKD 
        
        Generate random key for sender and random bases for sender and reciever
        """
        pass
    
    def send_key_as_photons(self):
        """
        * generate photons from sender's key and bases 
        * send them through the quantum channel to reciever
        * generate reciever's initial key by measuring photons
        """
        pass
    
    def sift_keys(self):
        """
        Communicate over classical channel to establish which photons 
        reciever measured in correct basis and remove incorrect or missing
        bits from both sender's and reciever's keys
        """
        pass
    
    def estimate_error(self):
        """
        Communicate subset of key over classical channel to estimate error
        and remove shared bits
        """
        pass


if __name__ == '__main__':
    main()
