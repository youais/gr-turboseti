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
from gnuradio import gr

class decim_buffer(gr.decim_block):

    """
    Not needed, to delete.
    
    """

    def __init__(self, n_fine_chans, n_ints_in_file):

        self.n_fine_chans = n_fine_chans
        self.n_ints_in_file = n_ints_in_file

        gr.decim_block.__init__(self,
            name="decim_buffer",
            in_sig=[(np.float32, self.n_fine_chans)],
            out_sig=[(np.float32, self.n_fine_chans)],
            decim=self.n_ints_in_file)
        self.set_relative_rate(60.0/self.n_ints_in_file)

    def work(self, input_items, output_items):
        in0 = input_items[0]
        print("in.shape:", in0.shape)
        print("in:", in0)
        out = output_items[0]
        print("output items shape:", out.shape)
        print("output items:", out)
        # <+signal processing here+>
        out[:] = in0
        print("output items check:", out)
        return len(output_items[0])
