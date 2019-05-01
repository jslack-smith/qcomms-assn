# -*- coding: utf-8 -*-
"""
This module contains code for anlysis and plotting of simulation data
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

from qkdsim.bb84 import BB84
from qkdsim.parties import Adversary, Sender
from qkdsim.hardware import PhotonSource


def main():
    # key_error_vs_eve_p_meas()
    key_error_vs_polarisation_error()
    return


def key_error_vs_polarisation_error(printResults=False, plotResults=True):
    x = np.linspace(-45, 45, 50)
    errors = list()
    initial_key_length = 10000
    qkd_list = [BB84(init_key_len=initial_key_length,
                     sender=Sender(photon_src=PhotonSource(pol_offset=p)))
                for p in x]

    x, errors = calculate_errors(x, qkd_list)
    if printResults is True:
        print_key_error_vs_polarisation_error(x, errors)
    if plotResults is True:
        plot_key_error_vs_polarisation_error(x, errors, initial_key_length)
    return


def print_key_error_vs_polarisation_error(x, errors):
    print(x)
    print(errors)
    return


def plot_key_error_vs_polarisation_error(x, errors, initial_key_length):
    plt.figure()
    plt.plot(x, errors, 'x')
    plt.gca().yaxis.set_major_formatter(PercentFormatter())
    plt.xlabel("Polarisation offset")
    plt.ylabel("QBER (%)")
    plt.title("QBER vs. Polarisation offset between sender and receiver\n"
              "(for key length = {})".format(initial_key_length))
    return


def key_error_vs_eve_p_meas(printResults=False, plotResults=True):
    x = np.linspace(0, 1, 20)
    error = list()
    initial_key_length = 10000
    qkd_list = [BB84(init_key_len=initial_key_length,
                     adversary=Adversary(p_meas=p))
                for p in x]

    for (p, qkd) in zip(x, qkd_list):
        qkd.run()
        sender_key = qkd.sender.key_after_sifting
        receiver_key = qkd.receiver.key_after_sifting
        e = calculate_key_error(sender_key, receiver_key)
        error.append(e)

    if printResults is True:
        print_key_error_vs_eve_p_meas(x, error)
    if plotResults is True:
        plot_key_error_vs_eve_p_meas(x, error, initial_key_length)
    return


def plot_key_error_vs_eve_p_meas(x, error, initial_key_length):
    plt.figure()
    plt.plot(x, error, 'x')
    plt.xlabel("Eve's measurement probability")
    plt.ylabel("QBER (%)")
    plt.title("QBER vs. Eve's measurement probability\n"
              "(for key length = {})".format(initial_key_length))
    return


def print_key_error_vs_eve_p_meas(x, error):
    raise NotImplementedError('needs to be updated')
# =============================================================================
#     header_left = 'Evesdrop probability:' + 3*' '
#     header_right = 'Key bit error:'
#     header = header_left+header_right
#     print(header)
#     data_str = '{:^{left_width}}{:^{right_width}}'.format(
#                 '{:.2%}'.format(p),
#                 '{:.2%}'.format(e),
#                 left_width=len(header_left),
#                 right_width=len(header_right)
#                 )
#     print(str(data_str))
# =============================================================================
    return


def calculate_key_error(a_key, b_key):
    errors = [a for (a, b) in zip(a_key, b_key) if a != b]
    # TODO in case of divide by zero
    percent_error = len(errors)/len(a_key)
    return percent_error*100


def calculate_errors(x, qkd_list):
    errors = list()
    for (p, qkd) in zip(x, qkd_list):
        qkd.run()
        sender_key = qkd.sender.key_after_sifting
        receiver_key = qkd.receiver.key_after_sifting
        e = calculate_key_error(sender_key, receiver_key)
        errors.append(e)
    return x, errors


if __name__ == '__main__':
    main()
