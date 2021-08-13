import multiprocessing as mp
import numpy as np
import logging
from main import DopplerFinder

"""

This is an example of the intended output of the DopplerFinder Sink GNU Radio block.

Issues:
- Certain aspects not transferable to GNU Radio
    - __name__ == "__main__" cannot be called in class, must be placed outside work()
    - Pool() should be defined in __init__ so as to be preserved across all calls to work()

"""

def apply_turboseti(spectra, filename, source_name, src_raj, src_dej,
                    tstart, tsamp, f_start, f_stop, n_fine_chans, n_ints_in_file,
                    log_level_int, coarse_chan, n_coarse_chan, min_drift, max_drift, snr,
                    out_dir, flagging, obs_info, append_output, blank_dc,
                    kernels, gpu_backend, precision, gpu_id):
    print("I'm in apply_turboseti")
    clancy = DopplerFinder(filename, source_name, src_raj, src_dej,
                        tstart, tsamp, f_start, f_stop, n_fine_chans, n_ints_in_file,
                        log_level_int, coarse_chan, n_coarse_chan, min_drift, max_drift, snr,
                        out_dir, flagging, obs_info, append_output, blank_dc,
                        kernels, gpu_backend, precision, gpu_id)
    clancy.find_ET(spectra)
    return print("apply_turboseti function done")

filename = 'fake_luyten_CH0'
source_name = 'fake luyten'
src_raj = 40.1
src_dej = 52.0
tstart = 1234.5678
tsamp = 1
f_start = 450
f_stop = 500
n_fine_chans = 1000000
n_ints_in_file = 60
log_level_int = logging.INFO
coarse_chan = 0
n_coarse_chan = 1
min_drift = 0.00001
max_drift = 4.0
snr = 25.0
out_dir = '/Users/mychai/turboseti-stream/'
flagging = False
obs_info = None
append_output = False
blank_dc = True
kernels = False
gpu_backend = False
precision = 1
gpu_id = 0

spectra = np.empty((0, n_fine_chans), dtype=np.float32, order='C')

input_items = np.random.rand(181, 1, 1000000)

i = 0

if __name__ == "__main__":
    with mp.Pool(processes=1) as pool:
        while True:
            if spectra.shape[0] < n_ints_in_file: # spectra rows < 60
                print("Buffer spectrum row #:", i, "/60")
                print("input_items[0]", input_items[i])
                print("input_items[0] shape:", input_items[i].shape)
                print("spectra shape:", spectra.shape)
                spectra = np.append(spectra, input_items[i], axis=0)
                print("Done.")
                print("New spectra shape:", spectra.shape)
                i += 1
                print("Upcoming row #:", i, "/60")
            else:
                print("Spectra:", spectra)
                print("Spectra shape:", spectra.shape)
                print("Creating DopplerFinder process...")
                dopplerfinder_process = pool.apply_async(func=apply_turboseti, args=(spectra, filename, source_name, src_raj, src_dej,
                                tstart, tsamp, f_start, f_stop, n_fine_chans, n_ints_in_file,
                                log_level_int, coarse_chan, n_coarse_chan, min_drift, max_drift, snr,
                                out_dir, flagging, obs_info, append_output, blank_dc,
                                kernels, gpu_backend, precision, gpu_id))
                print("Starting DopplerFinder process...")
                print(dopplerfinder_process.get())
                print("Process done.")
                spectra = np.empty((0, n_fine_chans), dtype=np.float32, order='C')
                print("Spectra rows:", spectra.shape[0])
                #i = 0
                print("New i:", i)
