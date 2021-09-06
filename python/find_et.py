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

import logging #make sure this is here
import numpy as np
import multiprocessing as mp
from gnuradio import gr
from turboseti_stream.turboseti_stream import DopplerFinder

DEBUGGING = True

class find_et(gr.sync_block):

    """
    This is the script for the DopplerFinder block, which runs an adapted version of
    turboSETI on a numpy float32 data matrix stored in RAM.

    Yiwei Chai
    Last updated August 13, 2021

    """

    def __init__(self, filename, source_name, src_raj, src_dej, tstart, tsamp, f_start, f_stop, n_fine_chans, n_ints_in_file,
                    log_level_int, coarse_chan, n_coarse_chan, min_drift, max_drift, snr, out_dir,
                    flagging, obs_info, append_output, blank_dc,
                    kernels, gpu_backend, precision, gpu_id):

        # Define parameters which need to be passed into DopplerFinder class
        self.filename = filename
        self.source_name = source_name
        self.src_raj = src_raj
        self.src_dej = src_dej
        self.tstart = tstart
        self.tsamp = tsamp
        self.f_start = f_start
        self.f_stop = f_stop
        self.n_fine_chans = n_fine_chans
        self.n_ints_in_file = n_ints_in_file

        if log_level_int == 0:
            self.log_level_int = logging.DEBUG
        elif log_level_int == 1:
            self.log_level_int = logging.INFO
        elif log_level_int == 2:
            self.log_level_int = logging.WARN
        else:
            raise RuntimeError("Incorrect logging level (%i)"%log_level_int)

        self.coarse_chan = coarse_chan
        self.n_coarse_chan = n_coarse_chan
        self.min_drift = min_drift
        self.max_drift = max_drift
        self.snr = snr
        self.out_dir = out_dir
        self.flagging = flagging
        self.obs_info = obs_info
        self.append_output = append_output
        self.blank_dc = blank_dc
        self.kernels = kernels
        self.gpu_backend = gpu_backend
        self.precision = precision
        self.gpu_id = gpu_id

        gr.sync_block.__init__(self,
            name="DopplerFinder",
            in_sig=[(np.float32, (self.n_ints_in_file, self.n_fine_chans))], #this should be vector float32, specify size = 1e6?
            out_sig=None)


    def work(self, input_items, output_items):

        if DEBUGGING:
            print("input_items[0] shape:", input_items[0].shape) #Checks input is expected shape (60, 1e6)

        spectra = np.squeeze(input_items[0]) # Use with basic_block
        #spectra = input_items[0] # Use with interp_block
        if DEBUGGING:
            print("DEBUG Current spectra:", spectra)
            print("DEBUG Current spectra shape:", spectra.shape)

        print("Initialising Clancy...")
        clancy = DopplerFinder(self.filename, self.source_name, self.src_raj, self.src_dej,
                            self.tstart, self.tsamp, self.f_start, self.f_stop, self.n_fine_chans, self.n_ints_in_file,
                            self.log_level_int, self.coarse_chan, self.n_coarse_chan, self.min_drift, self.max_drift, self.snr,
                            self.out_dir, self.flagging, self.obs_info, self.append_output, self.blank_dc,
                            self.kernels, self.gpu_backend, self.precision, self.gpu_id)
        print("Clancy is looking for ET...")
        clancy.find_ET(spectra)
        print("Clancy is done.")

        return len(spectra)

    """

    GNU Radio block that runs yolo'd version of turboSETI that can directly
    analyse data stored in RAM, rather than a .fil/.h5 file. Outputs .dat and .log
    file into user-specified out_dir.

    Part of the ATA GNU Radio pipeline. See examples folder for use in flowgraph.

    Yolo'd source code @ https://github.com/youais/turboseti-stream/blob/patch-1/main.py



    def __init__(self, filename, source_name, src_raj, src_dej, tstart, tsamp, f_start, f_stop, n_fine_chans, n_ints_in_file,
                        log_level_int, coarse_chan, n_coarse_chan, min_drift, max_drift, snr, out_dir,
                        flagging, obs_info, append_output, blank_dc,
                        kernels, gpu_backend, precision, gpu_id, input_buffer_len):

        gr.basic_block.__init__(self,
                                name="Doppler Finder",
                                in_sig=[np.float32],
                                out_sig=None)

        self.filename = filename
        self.source_name = source_name
        self.src_raj = src_raj
        self.src_dej = src_dej
        self.tstart = tstart
        self.tsamp = tsamp
        self.f_start = f_start
        self.f_stop = f_stop
        self.n_fine_chans = n_fine_chans
        self.n_ints_in_file = n_ints_in_file

        if log_level_int == 0:
            self.log_level_int = logging.DEBUG
        elif log_level_int == 1:
            self.log_level_int = logging.INFO
        elif log_level_int == 2:
            self.log_level_int = logging.WARN
        else:
            raise RuntimeError("Incorrect logging level (%i)"%log_level_int)

        self.coarse_chan = coarse_chan
        self.n_coarse_chan = n_coarse_chan
        self.min_drift = min_drift
        self.max_drift = max_drift
        self.snr = snr
        self.out_dir = out_dir
        self.flagging = flagging
        self.obs_info = obs_info
        self.append_output = append_output
        self.blank_dc = blank_dc
        self.kernels = kernels
        self.gpu_backend = gpu_backend
        self.precision = precision
        self.gpu_id = gpu_id

        self.input_buffer_len = input_buffer_len

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        ninput_items_required[0] = self.input_buffer_len

    def general_work(self, input_items, output_items):

        #print("Initialising Clancy...")
        spectra = input_items[0] #[:len(output_items[0])]

        clancy = DopplerFinder(self.filename, self.source_name, self.src_raj, self.src_dej,
                            self.tstart, self.tsamp, self.f_start, self.f_stop, self.n_fine_chans, self.n_ints_in_file,
                            self.log_level_int, self.coarse_chan, self.n_coarse_chan, self.min_drift, self.max_drift, self.snr,
                            self.out_dir, self.flagging, self.obs_info, self.append_output, self.blank_dc,
                            self.kernels, self.gpu_backend, self.precision, self.gpu_id)

        #print("Clancy searching for ET...")
        clancy.find_ET(spectra)

        self.consume(len(self.input_buffer_len))

        return len(spectra)
        #print("Clancy searched! Clancy excellent! Check results?")

#    def general_work(self, input_items, output_items):
#        output_items[0][:] = input_items[0]
#        consume(0, len(input_items[0]))        #self.consume_each(len(input_items[0]))
#        return len(output_items[0])

    """
