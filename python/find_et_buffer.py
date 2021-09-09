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
    This is the script for the DopplerFinder Buffer block, which accumulates 60
    incoming vectors of shape (1, 1e6) to create a data matrix of shape (60, 1e6).
    This data matrix is then passed to the DopplerFinder block for turboSETI analysis.

    Issues:
    - general_work() needs to run 60 times to collect 60 lots of input_items[0]

    Yiwei Chai
    Last updated August 13, 2021

    """
    def __init__(self, n_fine_chans, n_ints_in_file):

        self.n_fine_chans = n_fine_chans
        self.n_ints_in_file = n_ints_in_file

        #self.set_output_multiple(self.n_ints_in_file)

        self.spectra = np.empty((0, self.n_fine_chans), dtype=np.float32, order='C')

        gr.basic_block.__init__(self,
            name="find_et_buffer",
            in_sig=[(np.float32, self.n_fine_chans)],
            out_sig=[(np.float32, self.n_fine_chans)])
            #out_sig=[(np.float32, (self.n_ints_in_file, self.n_fine_chans))],
            #self.set_output_multiple(self.n_ints_in_file))

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        #for i in range(len(ninput_items_required)):
        ninput_items_required = self.n_ints_in_file
        print("ninput_items_required:", ninput_items_required)

        noutput_items = self.n_ints_in_file
        print("noutput_items:", noutput_items)

    def general_work(self, input_items, output_items):

        block_input = input_items[0]
        print("input size:", block_input.size)
        print("input data:", block_input)

        block_output = output_items[0]
        print("output size:", block_output.size)
        print("output data:", block_output)

        block_output[:] = block_input
        print("new output size:", block_output.size)
        print("new output data:", block_output)

        self.consume(0, len(block_input))

        return len(block_output)


        """while True:
            if self.spectra.shape[0] < self.n_ints_in_file:
                print("Initial self.spectra.shape:", self.spectra.shape)
                print("input_items[0] shape:", input_items[0].shape)
                print("input_items[0]:", input_items[0])
                self.spectra = np.append(self.spectra, input_items[0], axis=0)
                print("New self.spectra.shape:", self.spectra.shape)
                self.consume(0, len(input_items[0]))
            else:
                print("Full self.spectra.shape:", self.spectra.shape)
                output_items[0][:] = self.spectra
                print("output_items[0] shape:", output_items[0].shape)
                print("output_items[0]:", output_items[0])
                print(len(output_items[0]))
                break
                #self.spectra = np.empty((0, self.n_fine_chans), dtype=np.float32, order='C')
                return len(output_items[0])"""
