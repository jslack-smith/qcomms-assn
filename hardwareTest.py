'''
Created on 28 abr. 2019

@author: Emilio Molina
'''
import random
import numpy as np
from photon import Photon
from hardware import PhotonDetector
from hardware import PhotonSource

def main():
    """
    Simulate hardware
    
    """
    
#     photonGeneratorTest()
    photonDetectorTest()
    pass

def photonGeneratorTest():
    print("------This is a test for the photon source generator------")
    photongenTest=  PhotonSource(0.3) #error rate of 0.3 when generating
    count = 0
    goodPhot = 0
    length =30
    generated_photons = [None] *length
    
    for count in range (0,length):
        Photon = photongenTest.generatePhoton(np.pi/4*(random.randint(0,3)))
        if(Photon != None):
            generated_photons[count]=Photon
            goodPhot+=1
        else:
            pass
        count+=1
    perc= (goodPhot/count) *100
    print(perc,"% of photons generated correctly")
    
def photonDetectorTest():
    print("------This is a test for the photonDetector ------")
    photonGenTest=  PhotonSource(0) #error rate of 0 when generating
    photonMeasureTest= PhotonDetector(0) #loss rate of 0 when measuring
    count = 0
    length =5
    generated_photons = [None] *length
    measure_basis = [None] *length
    measured_photons = [None] *length
    out=""
    #generate the photons we are about to measure
    for count in range (0,length):
        Photon = photonGenTest.generatePhoton(np.pi/4*(random.randint(0,3)))
        generated_photons[count]= Photon
        count+=1
    pass
    
    #generate the measuring basis, for the moment is random
    count =0
    for count in range (0,length):
       measure_basis[count] = np.pi/4*(random.randint(0,3))
       count+=1
    pass
    
    #measure photons with measuring basis (not having into account loss rate at the moment)
    count =0
    for count in range (0,length):
        measurement = photonMeasureTest.detectPhoton(generated_photons[count], measure_basis[count])
        measured_photons[count] = measurement
        out += str(measurement)
        count+=1
    pass
    
    print("The measured photons are:", out)
    
if __name__ == '__main__':
    main()