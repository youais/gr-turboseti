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

class find_et_sync(gr.sync_block):

    """
    find_et_sync contains the necessary functions for the DopplerFinder Sink
    block. DopplerFinder Sink is part of the gr-turboseti GNU Radio OOT module,
    and can be used with gr-ata to perform near-synchronous turboSETI analysis
    on 60 second packets of ATA antenna data stored in RAM.

    For an example of usage, refer to flowgraph in examples folder of the GitHub
    repo.

    """

    def __init__(self, filename, source_name, src_raj, src_dej, tstart, tsamp, f_start, f_stop, n_fine_chans, n_ints_in_file,
                    log_level_int, coarse_chan, n_coarse_chan, min_drift, max_drift, snr, out_dir,
                    flagging, obs_info, append_output, blank_dc,
                    kernels, gpu_backend, precision, gpu_id):

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

        # Create empty matrix with correct shape
        self.spectra = np.empty((0, self.n_fine_chans), dtype=np.float32, order='C')

        self.get_context_pool = mp.get_context("spawn").Pool(processes=1)
        #self.pool = mp.Pool(processes=1)

        gr.sync_block.__init__(self,
            name="DopplerFinder Sink",
            in_sig=[(np.float32, self.n_fine_chans)], #this should be vector float32, specify size = 1e6?
            out_sig=None)

    def apply_turboseti(self):
        print("Initialising Clancy...")
        clancy = DopplerFinder(self.filename, self.source_name, self.src_raj, self.src_dej,
                            self.tstart, self.tsamp, self.f_start, self.f_stop, self.n_fine_chans, self.n_ints_in_file,
                            self.log_level_int, self.coarse_chan, self.n_coarse_chan, self.min_drift, self.max_drift, self.snr,
                            self.out_dir, self.flagging, self.obs_info, self.append_output, self.blank_dc,
                            self.kernels, self.gpu_backend, self.precision, self.gpu_id)
        print("Clancy is looking for ET...")
        clancy.find_ET(self.spectra)
        print("Clancy is done.")

    #def multiprocessing_buffer(self, input_items):
    def __getstate__(self):
        self_dict = self.__dict__.copy()
        del self_dict['pool']
        return self_dict

    def __setstate__(self, state):
        self.__dict__.update(state)

    def work(self, input_items, output_items):
        i = 0
        j = 0
        with self.get_context_pool as pool:
            while True:
                if self.spectra.shape[0] < self.n_ints_in_file: # spectra rows < 60
                    if DEBUGGING:
                        print("DEBUG Buffer spectra row #:", i,"/60")
                        print("DEBUG Incoming vector #:", j)
                        print("DEBUG Incoming vector, i.e. 'input_items[0]':", input_items[0])
                        print("DEBUG Incoming vector shape:", input_items[0].shape)
                        print("DEBUG Initial spectra shape:", self.spectra.shape)
                    self.spectra = np.append(self.spectra, input_items[0], axis=0)
                    if DEBUGGING:
                        print("DEBUG New row appended. New spectra shape:", self.spectra.shape)
                    i += 1
                    j += 1
                    if DEBUGGING:
                        print("DEBUG Next spectrum row #:", i,"/60")
                        print("DEBUG Next vector #:", j)
                    #return len(input_items[0])
                else:
                    if DEBUGGING:
                        print("DEBUG Current spectra:", self.spectra)
                        print("DEBUG Current spectra shape:", self.spectra.shape)
                    print("Creating DopplerFinder process...")
                    dopplerfinder_process = pool.apply_async(func=self.apply_turboseti, args=(self,))
                    print("Starting DopplerFinder process...")
                    print(dopplerfinder_process.get())
                    print("Process done.")
                    self.spectra = np.empty((0, self.n_fine_chans), dtype=np.float32, order='C')
                    i = 0
                    if DEBUGGING:
                        print("DEBUG Reset spectra shape:", self.spectra.shape[0])
                        #i = 0
                        print("DEBUG Next spectra row:", i,"/60")
                        print("DEBUG Next vector #:", j)
        print("Pls let this work. If this prints, then it's working (probs??)")
        return len(input_items[0])

if __name__ == "__main__":
    find_et_sync().run()
