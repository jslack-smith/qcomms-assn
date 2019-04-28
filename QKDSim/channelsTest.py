'''
Created on 28 abr. 2019

@author: Emilio Molina
'''
from channels import ClassicalChannel
from channels import QuantumChannel
from photon import Photon
import random
import numpy as np


def main():
    """
    Simulate channels
    
    """
    
    
    classicalChannelTest()
    quantumChannelTest()
    pass

def classicalChannelTest():
    print("------This is a test for the classical communication channel------")
    cl_chan_test = ClassicalChannel() #initialize channel
    message = "test"
    cl_chan_test.send(message)
    print("Sent message: " +message)
  
    
    received_message = cl_chan_test.receive()
    if (message == received_message):
        print("Received message: " + received_message)
        print("Sucessful communication")
    else:
        print("Unsucessful communication")
        
    pass

def quantumChannelTest():
    print("------This is a test for the quantum communication channel------")
    qu_chan_test=  QuantumChannel (0)
    count = 0
    length =10
    sent_photons = [None] *length
    received_photons = [None] *length
    
    for count in range (0,length):
        newPhoton = Photon(np.pi/4*(random.randint(0,3))) 
        qu_chan_test.send(newPhoton)
        sent_photons[count] = newPhoton
        count+=1
    
    
    count=0
    while qu_chan_test.queue.__len__()>=1:
        received_photons[count]=qu_chan_test.receive()
        count+=1
    
    count=0
    noLoss= True
    for count in range (0,length):
        if(received_photons[count]==sent_photons[count]):
            pass
        else:
            print("Sent photons and received photons are different!")
            noLoss = False
        count+=1
    
    if(noLoss):
        print("All photons were sucesfully sent")
    else:
        pass
    
    pass
    
if __name__ == '__main__':
    main()