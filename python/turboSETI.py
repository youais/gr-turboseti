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
import os
import h5py

from gnuradio import gr
from turbo_seti.find_doppler.find_doppler import FindDoppler
# from turbo_seti.find_event.find_event import make_table
from turbo_seti.find_event.find_event_pipeline import find_event_pipeline

class turboSETI(gr.sync_block):

    """

    docstring for block turboSETI

    Need to have blimpy and turboSETI installed in order to import.

    STEPS: (make def for each?)
    0. Want input to be filterbank file????
    1. Convert input data into .h5 file and store in some directory
    2. Define FindDoppler function on .h5 file
        (specifying max_drift, snr, & directory to place generated .dat files)
    3. Run FindDoppler(blahblahblah).search() --> this generates .dat file + stores in output_directory
    4. OPTIONAL - Create table using make_table(directory_path + 'dat_file_name.dat'), store table in output_directory
    5. Run find_event_pipeline to find potential events
    6. Output results of find_event_pipeline
        - Make compatible connection to QT GUI Sink to create realtime plots?
            - Convert hits into np.float/complex64/??? arrays?
        - QT GUI freq sink = floating point?
        - QT GUI waterfall sink = floating point?
    7. Make all the above repeatable (real-time)? while loop/threading?

    QUESTIONS:
    - Where to insert argparser/equivalent for user-specified parameters?
    - How to make script loop for continuous stream of real-time data?

    TEST:
    - Run first test using blimpy tutorial .h5 file as file source!
        - 'Voyager1.single_coarse.fine_res.h5'

    """

    def __init__(self, filesource, filepath, h5_filename, dataset_name, dat_filename,
        lst_filename, csv_filename, max_drift, snr, out_dir, filter_threshold,
        user_validation, saving): # args show up as parameters in GRC

        gr.sync_block.__init__(self,
            name="turboSETI", # shows up in GRC
            in_sig=[np.complex64], # figure out input dtype!
            out_sig=None) # figure out output dtype!

        # self.something = something_here --> do I need this?
        self.filesource = filesource # bool, default = False
        self.filepath = filepath # string
        self.h5_filename = h5_filename # string, e.g. 'data.h5'
        self.dataset_name = dataset_name # string
        self.dat_filename = dat_filename # string, 'data.dat'
        self.lst_filename = lst_filename # string, 'data.lst'
        self.csv_filename = csv_filename # string, 'data.csv'
        self.max_drift = max_drift # integer?
        self.snr = snr # integer?
        self.out_dir = out_dir # = filepath?
        self.filter_threshold = filter_threshold # integer?
        self.user_validation = user_validation # bool, default = False
        self.saving = saving # bool, default = True

    # From Embedded Python Block ex: If an attribute with the
    # same name as a parameter is found, a callback is registered
    # (properties work too) --> what the heck does this mean???

    def create_h5_file(self):
        # define input
        # convert input to .h5 file
        # write .h5 file to some directory
        # pass --> not sure if I need this
        h5_filepath = self.filepath + self.h5_filename

        if filesource == False:
            hf = h5py.File(h5_filepath, 'w') # argparse to specify filename?
            hf.create_dataset(self.dataset_name, data=in_sig)
            hf.close()
            print('Data written to', h5_filepath)

        else:
            print('Data from file source.')


    def run_find_doppler(self):

        doppler = FindDoppler(self.h5_filename,
                                self.max_drift,
                                self.snr,
                                self.out_dir)
        doppler.search() # creates the .dat file

        dat_filepath = self.file_path + self.dat_filename
        lst_filepath = self.file_path + self.lst_filename
        csv_filepath = self.file_path + self.csv_filename
        # df = make_table(dat_filepath) # Not rlly necessary since we don't need to see the table in GR
        dat_list = [dat_filepath] # Not necessary for only 1 .dat file?
        number_in_cadence = len(dat_list)

        # Writes .dat files into .lst file
        with open(lst_filepath, 'w') as f:
            for item in dat_list:
                f.write("%s\n" % item)

        find_event = find_event_pipeline(lst_filepath,
                                        self.filter_threshold,
                                        number_in_cadence,
                                        self.user_validation,
                                        self.saving,
                                        csv_name = self.csv_filename)
        print('Yay!')

        # output_items = find_event # convert to some kind of dtype stream

    #def work(self, input_items, output_items, max_drift, snr, out_dir): # come up w/ better name
        # in0 = input_items[0]
        # out = output_items[0]

        # <+signal processing here+>
        # out[:] = in0
        # return len(output_items[0]) #fingers crossed!
