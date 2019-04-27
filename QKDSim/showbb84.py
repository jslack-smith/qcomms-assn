# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 21:58:17 2019

@author: James
"""

from bb84 import BB84
from bb84 import BB84Stage

class Show(object):
    def __init__(self, bb84, display_style=DisplayStyle.CONSOLE):
        self.bb84 = bb84
        self.display_style = display_style
        
    def show_stage(self, stage):
        if not bb84.verbose:
            return
        
        # TODO extend for different display options
        # e.g. printing in console, print to file, show graph...

        if self.display_style == DisplayStyle.CONSOLE:
            self.console_print_stage(stage)
        elif self.display_style == DisplayStyle.PRINT_TO_FILE:
            self.print_to_file_stage(stage)
        else:
            self.console_print_stage(stage)
            
    def console_print_stage(self, stage):
        if stage == BB84Stage.INITIALISE:
            self.console_print_initialise()
        elif stage == BB84Stage.SEND_PHOTONS:
            self.console_print_send_photons()
        elif stage == BB84Stage.SIFT_KEYS:
            pass
        # TODO finish stages, functions
        # TODO refactor to get rid of so many if statements
            

class DisplayStyle(Enum):
    CONSOLE = 1
    PRINT_TO_FILE = 2


if __name__ == '__main__':
    main()