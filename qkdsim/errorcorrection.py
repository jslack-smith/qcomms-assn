# -*- coding: utf-8 -*-
"""
This module contains functions related to error correction
"""
import numpy as np
def parity_check(key):
    """
    * Create parity of keys.
    This method will add one last bit to the key with the parity check.
    Parity bit = 1 if parity even, 0 if uneven
    """
    parity = 0 #Uneven parity
    if ((sum(key) % 2) == 0):
        parity = 1 #Even parity

    return parity


def errorCorrection(a_key,b_key,cl_chan):
        """
        Keys must be np arrays of 7 bit long and both keys must have at MOST 1 error!
        """
        a = np.array(a_key)[0:7]
        b = np.array(b_key)[0:7]
        
        hMatrix = np.matrix([[1, 1, 1, 0, 1, 0, 0], [1, 1, 0, 1, 0, 1, 0], [0, 1, 1, 1, 0, 0, 1]])
        sA = hMatrix * a.reshape((7, 1))
        for i in range(0,len(sA)):
            if(sA[i] % 2 == 0):
                sA[i] =0
            else:
                sA[i] =1
        cl_chan.send(sA)
        
        sB = hMatrix * b.reshape((7, 1))
        for i in range(0,len(sB)):
            if(sB[i] % 2 == 0):
                sB[i] =0
            else:
                sB[i] =1
        sA_received = cl_chan.receive()
        s = sB - sA_received
        for i in range(0,len(sB)):
            if(s[i]  == -1):
                s[i] =1
        e = np.zeros(7)
        compareArr = s.reshape((3, 1)) == hMatrix
        checkArray = np.array([[True], 
                               [True], 
                               [True]])
        i = 0
        for i in range (0,7):
            checkColumn = compareArr[:,[i]]
            if(((checkArray.reshape((3, 1))) == (checkColumn.reshape((3, 1)))).all()):
                e[i] = 1
            else:
                pass
        
        return np.absolute((b - e).astype(int))
if __name__ == '__main__':
    pass
