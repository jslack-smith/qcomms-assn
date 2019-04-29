'''
Created on 28 abr. 2019

@author: Emilio Molina
'''
import random
from qkdsim.photon import M
from qkdsim.hardware import PhotonDetector
from qkdsim.hardware import PhotonSource


def main():
    """
    Simulate hardware
    """

    photon_generator_test()
    photon_detector_test()
    return


def photon_generator_test():
    print("------This is a test for the photon source generator------")
    source = PhotonSource(0.3)  # error rate of 0.3 when generating
    good_photons = 0
    num_photons = 30
    generated_photons = [None] * num_photons

    for count in range(0, num_photons):
        photon = source.generate_photon(45*(random.randint(0, 3)))
        if photon is not None:
            generated_photons[count] = photon
            good_photons += 1
    perc = (good_photons/num_photons)*100
    print("{}% of photons generated correctly".format(perc))


def photon_detector_test():
    print("------This is a test for the photonDetector ------")
    source = PhotonSource(0)  # error rate of 0 when generating
    detector = PhotonDetector(0)  # loss rate of 0 when measuring
    num_photons = 5
    generated_photons = [None]*num_photons
    measure_basis = [None]*num_photons
    measured_photons = [None]*num_photons
    out = ""
    # generate the photons we are about to measure
    for count in range(0, num_photons):
        photon = source.generate_photon(45*(random.randint(0, 3)))
        generated_photons[count] = photon

#     print("Generated photons: {}".format(generated_photons))

    # generate the measuring basis, for the moment is random
    for count in range(0, num_photons):
        measure_basis[count] = M(45*(random.randint(0, 3)))

    print("Random measurement bases: {}".format(measure_basis))

    # measure photons with measuring basis
    # (not taking into account loss rate at the moment)
    for count in range(0, num_photons):
        measurement = detector.detect_photon(generated_photons[count],
                                             measure_basis[count])
        measured_photons[count] = measurement
        out += str(measurement)

    print("The measured photons are: {}".format(out))


if __name__ == '__main__':
    main()