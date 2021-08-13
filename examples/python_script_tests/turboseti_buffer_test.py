"""
Yiwei Chai, August 12 2021

This is test script for find_et_buffer.py

"""

import numpy as np
import logging

DEBUGGING = True

n_fine_chans = 1000000
n_ints_in_file = 60

# spectra = np.empty((0, n_fine_chans), dtype=np.float32, order='C')

input_items = np.random.rand(181, 1, 1000000)



"""
i = 0
j = 0

while True:
    if spectra.shape[0] < n_ints_in_file: # spectra rows < 60
        if DEBUGGING:
            print("DEBUG Buffer spectra row #:", i,"/60")
            print("DEBUG Incoming vector #:", j)
            print("DEBUG Incoming vector, i.e. 'input_items[0]':", input_items[i])
            print("DEBUG Incoming vector shape:", input_items[i].shape)
            print("DEBUG Initial spectra shape:", spectra.shape)
        spectra = np.append(spectra, input_items[i], axis=0)
        if DEBUGGING:
            print("DEBUG New row appended. New spectra shape:", spectra.shape)
        i += 1
        j += 1
        if DEBUGGING:
            print("DEBUG Next spectrum row #:", i,"/60")
            print("DEBUG Next vector #:", j)
        #return len(input_items[0])
    else:
        if DEBUGGING:
            print("DEBUG Current spectra:", spectra)
            print("DEBUG Current spectra shape:", spectra.shape)
        #output_items = []
        output_items = spectra
        #consume(0, len(output_items[0]))
        print(output_items)
        print(output_items.shape)
        spectra = np.empty((0, n_fine_chans), dtype=np.float32, order='C')
        #print("Spectra rows:", spectra.shape[0])
        #i = 0
        #print("New i:", i)
        print(len(output_items[0]))
"""
