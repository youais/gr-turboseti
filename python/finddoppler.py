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

"""

Plan:
1. Block inputs metadata + data
    - Metadata generated at ATA block (user specifies target, freq, etc)
    - Data comes from ATA block, processed through PFB + FFT, in matrix form
2. Run Luigi's backend on data matrix
3. Run

Parameters
----------
From ATA block:

    centre_freq : [dtype]
    antenna_list : list(str)
        Example - blah
    coord_type : string
        Example - blah

    source_id : string
    ra : [dtype]
    dec : [dtype]
    az : [dtype]
    el : [dtype]

Data Processing?

    max_drift : float
        Max drift rate in Hz/second
        default=4.0
    min_drift : float
        Min drift rate in Hz/second
        default=1e-5
    snr : float
        Signal to Noise Ratio (a ratio bigger than 1 to 1 has more signal than noise)
        default=25.0
    pfb_bandwidth : [dtype]
        Specfied at PFB block.
    fft_length : [dtype]
        Specified at FFT block.

"""


import numpy
# import os

from gnuradio import gr
from turboseti_stream import main

class ETWhereRU(gr.basic_block):

    def __init__(self, filename, out_dir):
        gr.basic_block.__init__(self,
            name="finddoppler",
            in_sig=[float32],
            out_sig=None)

        self.filename = filename
        self.out_dir = out_dir

    def run_doppler_finder(self):
        clancy = DopplerFinder(filename="test1", )
        clancy.find_ET()

#def __init__(self, filename, f_start, f_stop,
#                 tsteps, tsteps_valid, tdwidth, fftlen, shoulder_size, drift_rate_resolution,
#                 max_drift=4.0, min_drift=0.00001, snr=25.0, out_dir='./', obs_info=None, flagging=False,
#                 n_coarse_chan=1, append_output=False, blank_dc=True, gpu_id=0, precision=1, kernels=None,
#                 gpu_backend=False, log_level_int=logging.INFO):

    # Data Object Header
#        self.header = Map({
#            "coarse_chan": 1,
#            "obs_length": 0,
#            "DELTAF": 0,
#            "NAXIS1": 0,
#            "FCNTR": 0,
#            "baryv": 0,
#            "SOURCE": 0,
#            "MJD": 0,
#            "RA": 0,
#            "DEC": 0,
#            "DELTAT": 0,
#            "max_drift_rate": max_drift,
#        })

# FindDoppler(filename, f_start, f_stop, tsteps, )

find_doppler = FindDoppler("CH0_TIMESTAMP", 0.0, 1.0, 256, 1, 1, 1, 1, 1);
find_doppler.search(np.zeros((256)))




'''class finddoppler(gr.basic_block):

    """

    Runs FindDoppler on 6 .h5 files (needed for find_event ON/OFF cadence)

    returns: 6 .dat files --- contains all of turboSETI's hits
             6 .log files --- logged output of search algorithm

    """

    def __init__(self, datadir, max_drift, snr):
        gr.basic_block.__init__(self,
            name="finddoppler",
            in_sig=None,
            out_sig=None)

        self.datadir = datadir # string, directory where .fil or .h5 files are stored
        self.max_drift = max_drift # int
        self.snr = snr # int

    def run_find_doppler(self):

        """
        1. Make list of x number of .h5 files (min 2), read in list?
        2. Iterate FindDoppler function for each .h5 file in list
        """
        for x_file in sorted(os.listdir(datadir)):
            x_type = x_file.split('.')[-1]
            if x_type != 'h5':
                doppler = FindDoppler(self.datadir + x_file,
                                      self.max_drift,
                                      self.snr,
                                      self.out_dir)
                doppler.search()'''

        #for file in h5_file_list:
            #doppler = FindDoppler(self.datadir + file, self.max_drift, self.snr, self.out_dir)
            #doppler.search()




    #def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        #for i in range(len(ninput_items_required)):
            #ninput_items_required[i] = noutput_items

    #def general_work(self, input_items, output_items):
        #output_items[0][:] = input_items[0]
        #consume(0, len(input_items[0]))        #self.consume_each(len(input_items[0]))
        #return len(output_items[0])
