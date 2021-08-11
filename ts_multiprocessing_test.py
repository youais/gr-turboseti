import multiprocessing as mp
import numpy as np
import logging
from turboseti_stream.turboseti_stream import DopplerFinder

#def square(num):
#    result = num*num
#    return result

def apply_turboseti(spectra, filename, source_name, src_raj, src_dej,
                    tstart, tsamp, f_start, f_stop, n_fine_chans, n_ints_in_file,
                    log_level_int, coarse_chan, n_coarse_chan, min_drift, max_drift, snr,
                    out_dir, flagging, obs_info, append_output, blank_dc,
                    kernels, gpu_backend, precision, gpu_id):
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
out_dir = './'
flagging = False
obs_info = None
append_output = False
blank_dc = True
kernels = False
gpu_backend = False
precision = 1
gpu_id = 0

spectra = np.empty((0, n_fine_chans), dtype=np.float32, order='C')

input_items = np.random.rand(120, 1, 1000000)

i = 0

while True:
    if spectra.shape[0] < n_ints_in_file: # spectra rows < 60
        print("Buffer spectrum row #:", i, "/60")
        #print("Adding next vector to spectra...", input_items[0][i])
        #print("input_items[0][i] shape:", input_items[0][i].shape)
        print("input_items[0]", input_items[i])
        print("input_items[0] shape:", input_items[i].shape)
        print("spectra shape:", spectra.shape)
        # self.spectra[self.buffer_spectrum, :] = input_items.copy()
        #matrix[i] = input_items[0]
        spectra = np.append(spectra, input_items[i], axis=0)
        print("Done.")
        print("New spectra shape:", spectra.shape)
        #self.buffer_spectrum +=1
        i += 1
        print("Upcoming row #:", i, "/60") #self.buffer_spectrum)
    else:
        if __name__ == "__main__":
            print("Spectra:", spectra)
            print("Spectra shape:", spectra.shape)
            with mp.Pool(processes=1) as pool:
                print("Creating DopplerFinder process...")
                #dopplerfinder_process = pool.apply_async(func=square, args=(10,))
                dopplerfinder_process = pool.apply_async(func=apply_turboseti, args=(spectra, filename, source_name, src_raj, src_dej,
                                tstart, tsamp, f_start, f_stop, n_fine_chans, n_ints_in_file,
                                log_level_int, coarse_chan, n_coarse_chan, min_drift, max_drift, snr,
                                out_dir, flagging, obs_info, append_output, blank_dc,
                                kernels, gpu_backend, precision, gpu_id))
                #print("Starting DopplerFinder process...")
                #dopplerfinder_process.start()
                #dopplerfinder_process.join()
                print(dopplerfinder_process.get()) # if this is uncommented, the following lines won't run
                                                   # but the loop will restart from the if statement
                print("Process done.")
                spectra = np.empty((0, n_fine_chans), dtype=np.float32, order='C')
                print("Spectra rows:", spectra.shape[0])
                #i = 0
                print("New i:", i)
