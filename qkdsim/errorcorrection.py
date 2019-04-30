# -*- coding: utf-8 -*-
"""
This module contains functions related to error correction
"""


def parity_creation(self):
    """
    * Create parity of keys.
    This method will add one last bit to the key with the parity check.
    Parity bit = 1 if parity even, 0 if uneven
    """
    a = self.sender.key
    b = self.reciever.key
    a_parity = 0
    b_parity = 0
    if ((a.sum(axis=0) % 2) == 0):
        a_parity = 1
        a.append(a_parity)

    if ((b.sum(axis=0) % 2) == 0):
        b_parity = 1
        b.append(b_parity)
    return


def parity_check(self):
    """
    * Check parity of keys to see if there are errors on Alice and Bob keys
    """
    a = self.sender.key
    b = self.reciever.key
    a_parity = a[-1]  # get parity bit
    b_parity = b[-1]  # get parity bit
    error_corr = False

    self.reciever.cl_chan.send(b_parity)
    self.sender.cl_chan.send(a_parity)

    if((self.sender.cl_chan.receive() == b_parity)
            and (self.receiver.cl_chan.receive() == a_parity)):
        print("Sucesful parity check")
    else:
        print("Unsucesful parity check")
        # use to decide if we need to perform error corr or not
        error_corr = True

    return error_corr


if __name__ == '__main__':
    pass
