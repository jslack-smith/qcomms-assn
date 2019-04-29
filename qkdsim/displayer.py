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


class ConsoleTablePrinter(Displayer):

    def display_initialise(self, sender_name, sender_key, sending_bases,
                           receiver_name, receiving_bases):
        """
        create table as a dict, where each (key, value) pair is a row in
        the table with the key being the header and the value being an
        array
        """
        # s_key_str =

        table = (
            ("{}'s key".format(sender_name), sender_key),
            ("{}'s sending bases".format(sender_name), sending_bases),
            ("{}'s receiving bases".format(receiver_name), receiving_bases)
            )

        print("INITIALISATION")

        for row in table:
            header = row[0]
            data = row[1]
            print("{:25}".format(header)
                  + ''.join(["{:3}".format(str(e)) for e in data]))

    def display_send_key_as_photons(self):
        pass

    def display_sift_keys(self):
        pass

    def display_estimate_error(self):
        pass


if __name__ == '__main__':
    pass
