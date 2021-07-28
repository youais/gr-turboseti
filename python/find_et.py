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
#from ?.main import DopplerFinder

class find_et(gr.basic_block):

    """

    GNU Radio block that runs yolo'd version of turboSETI that can directly
    analyse data stored in RAM, rather than a .fil/.h5 file. Outputs .dat and .log
    file into user-specified out_dir.

    Part of the ATA GNU Radio pipeline. See examples folder for use in flowgraph.

    Yolo'd source code @ https://github.com/youais/turboseti-stream/blob/patch-1/main.py

    """

    def __init__(self, filename, out_dir, source_name, src_raj, src_dej,
                 tstart, tsamp, f_start, f_stop,
                 coarse_chan=0, n_coarse_chan=1, n_fine_chans, n_ints_in_file,
                 min_drift=0.00001, max_drift=4.0, drift_rate_resolution, snr=25.0,
                 flagging=False, obs_info=None, append_output=False, blank_dc=True,
                 kernels=None, gpu_backend=False, precision=1, gpu_id=0):

        gr.basic_block.__init__(self,
            name="find_et",
            in_sig=[np.float32],
            out_sig=None)

        self.filename = filename
        self.out_dir = out_dir
        self.source_name = source_name
        self.src_raj = src_raj
        self.src_dej = src_dej
        self.tstart = tstart
        self.tsamp = tsamp
        self.f_start = f_start
        self.f_stop = f_stop
        self.coarse_chan = coarse_chan
        self.n_coarse_chan = n_coarse_chan
        self.n_fine_chans = n_fine_chans
        self.n_ints_in_file = n_ints_in_file
        self.min_drift = min_drift
        self.max_drift = max_drift
        self.drift_rate_resolution = drift_rate_resolution
        self.snr = snr
        self.flagging = flagging
        self.obs_info = obs_info
        self.append_output = append_output
        self.blank_dc = blank_dc
        self.kernels = kernels
        self.gpu_backend = gpu_backend
        self.precision = precision
        self.gpu_id = gpu_id

    def run_doppler_finder(self):

        clancy = DopplerFinder(self, self.filename, self.out_dir, self.source_name,
                            self.src_raj, self.src_dej, self.tstart, self.tsamp,
                            self.f_start, self.f_stop, self.coarse_chan,
                            self.n_coarse_chan, self.n_fine_chans, self.n_ints_in_file,
                            self.min_drift, self.max_drift, self.drift_rate_resolution,
                            self.snr, self.flagging, self.obs_info, self.append_output,
                            self.blank_dc, self.kernels, self.gpu_backend, self.precision,
                            self.gpu_id)

        clancy.find_ET()

#    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
#        for i in range(len(ninput_items_required)):
#            ninput_items_required[i] = noutput_items

#    def general_work(self, input_items, output_items):
#        output_items[0][:] = input_items[0]
#        consume(0, len(input_items[0]))        #self.consume_each(len(input_items[0]))
#        return len(output_items[0])
