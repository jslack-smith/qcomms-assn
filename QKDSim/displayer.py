# -*- coding: utf-8 -*-
"""
This module contains classes for displaying results of simulation
"""


class Displayer(object):

    def display_initialise(self, sender_name, sender_key, sending_bases,
                           receiver_name, receiving_bases):
        raise NotImplementedError('subclass must override')

    def display_send_key_as_photons(self):
        raise NotImplementedError('subclass must override')

    def display_sift_keys(self):
        raise NotImplementedError('subclass must override')

    def display_estimate_error(self):
        raise NotImplementedError('subclass must override')


class ConsolePrinter(Displayer):

    def display_initialise(self, sender_name, sender_key, sending_bases,
                           receiver_name, receiving_bases):
        initialise_str = list()
        initialise_str.append("{}'s key: {}".format(sender_name, sender_key))
        initialise_str.append("Sending bases: {}".format(sending_bases))
        initialise_str.append("Receiving bases: {}".format(receiving_bases))

        initialise_str = '\n'.join(initialise_str)
        print(initialise_str)

    def display_send_key_as_photons(self):
        pass

    def display_sift_keys(self):
        pass

    def display_estimate_error(self):
        pass


if __name__ == '__main__':
    pass
