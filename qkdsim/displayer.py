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

    table = []
    
    def display_initialise(self, sender_name, sender_key, sending_bases):
        """
        create table as a dict, where each (key, value) pair is a row in
        the table with the key being the header and the value being an
        array
        """

        self.table.extend([
            ["INITIALISATION", ''],
            ["{}'s key".format(sender_name), sender_key],
            ["{}'s (sending) bases".format(sender_name), sending_bases]
            ])

        # self.print_table()
        return

    def display_send_key_as_photons(self, sent_photons, receiver_name, 
                                    receiving_bases, receiver_key):
        self.table.extend([
            ["SEND KEY AS PHOTONS", ''],
            ["Sent photons", sent_photons],
            ["{}'s (receiving) bases".format(receiver_name), receiving_bases],
            ["Bits as received by {}".format(receiver_name), receiver_key]
            ])
        self.print_table()
        return

    def display_sift_keys(self):
        pass

    def display_estimate_error(self):
        pass
    
    def print_table(self):   
        for row in self.table:
            header = row[0]
            data = row[1]
            row_str = list()
            row_str.append("{:<25}".format(header))
            # TODO is there a better way to check? only checks first item
            if len(data) > 0:
                if hasattr(data[0], 'tabl'):
                    row_str.extend(["{:>4}".format(e.tabl()) for e in data])
                else:
                    row_str.extend(["{:>4}".format(str(e)) for e in data])
      
            print(''.join(row_str))


if __name__ == '__main__':
    pass
