#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 Yiwei Chai.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#


import numpy as np
import logging #make sure this is here
from gnuradio import gr

DEBUGGING = True

class find_et_buffer(gr.basic_block):
    """
    docstring for block find_et_buffer
    """
    def __init__(self, n_fine_chans, n_ints_in_file):

        self.n_fine_chans = n_fine_chans
        self.n_ints_in_file = n_ints_in_file

        self.spectra = np.empty((0, self.n_fine_chans), dtype=np.float32, order='C')

        gr.basic_block.__init__(self,
            name="find_et_buffer",
            in_sig=[(np.float32, self.n_fine_chans)],
            out_sig=[(np.float32, (self.n_ints_in_file, self.n_fine_chans))])

    #def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        #for i in range(len(ninput_items_required)):
        #    ninput_items_required[i] = noutput_items

    def general_work(self, input_items, output_items):
        #output_items[0][:] = input_items[0]
        #consume(0, len(input_items[0]))        #self.consume_each(len(input_items[0]))
        #return len(output_items[0])

        i = 0
        j = 0
        while True:
            if self.spectra.shape[0] < self.n_ints_in_file: # spectra rows < 60
                if DEBUGGING:
                    print("DEBUG Buffer spectra row #:", i,"/60")
                    print("DEBUG Incoming vector #:", j)
                    print("DEBUG Incoming vector (i.e. input_items[0]):", input_items[0])
                    print("DEBUG Incoming vector shape:", input_items[0].shape) # Expect (1, 1000000)
                    print("DEBUG Initial spectra shape:", self.spectra.shape)
                self.spectra = np.append(self.spectra, input_items[0], axis=0)
                if DEBUGGING:
                    print("DEBUG New row appended. New spectra shape:", self.spectra.shape)
                i += 1
                j += 1
                if DEBUGGING:
                    print("DEBUG Next buffer spectra row #:", i, "/60")
                    print("DEBUG Next incoming vector #:", j)
                #consume(0, len(input_items[0]))
            else:
                if DEBUGGING:
                    print("DEBUG Filled spectra:", self.spectra)
                    print("DEBUG Filled spectra shape:", self.spectra.shape) # Expect (60, 1000000)
                output_items[0] = self.spectra
                #consume(0, len(self.spectra))
                #output_items[0] = np.empty((0, self.n_fine_chans), dtype=np.float32, order='C')
                #i = 0
                #if DEBUGGING:
                #    print("DEBUG Reset spectra shape:", self.spectra.shape[0])
                #    print("DEBUG Next spectra row:", i,"/60")
                #    print("DEBUG Next vector #:", j)
        return len(output_items[0])
