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
    - output_items[0] may not be entirely cleared after each iteration,
      but this doesn't seem to interfere with writing new block of input_items[0]
      so perhaps this is a non-issue?

    Yiwei Chai
    Last updated September 10, 2021

    """

    def __init__(self, n_fine_chans, n_ints_in_file):

        self.n_fine_chans = n_fine_chans
        self.n_ints_in_file = n_ints_in_file

        gr.basic_block.__init__(self,
            name="find_et_buffer",
            in_sig=[(np.float32, self.n_fine_chans)],
            out_sig=[(np.float32, self.n_fine_chans)])

        # Set up desired number of signals in data matrix (e.g. 60)
        self.set_output_multiple(self.n_ints_in_file)

        # Set up empty 'spectra' with desired shape (e.g. (60, 1e6))
        # self.spectra = np.empty((0, self.n_fine_chans), dtype=np.float32, order='C')

    def general_work(self, input_items, output_items):

        block_input = input_items[0]
        if DEBUGGING:
            print("DEBUG Input data shape:", block_input.shape)
            print("DEBUG Input data:", block_input)

        block_output = output_items[0]
        if DEBUGGING:
            print("DEBUG Output data shape:", block_output.shape)
            print("DEBUG Output data:", block_output)

        block_output[:] = block_input
        if DEBUGGING:
            print("DEBUG New output data shape:", block_output.shape)
            print("DEBUG New output data:", block_output)

        self.consume(0, len(block_input))

        return len(block_output)
