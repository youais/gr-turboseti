import numpy as np
import multiprocessing as mp
import time

"""
Issues:
    - Will output hi_square() if spectra.shape[0] >= 5 without the while loop
    - Once the while loop is added, it won't log anything after line 36 

"""

spectra = np.empty((0, 1000000), dtype=np.float32, order='C')
input_items = np.random.rand(121, 1, 1000000)

def hi_square(spectra, num):
    print("Hello world!")
    print("Spectra shape:", spectra.shape)
    print(num, "squared:", num*num)

i = 0

while True:
    if spectra.shape[0] < 5: # spectra rows < 60
        print("Buffer spectrum row #:", i, "/5")
        print("input_items[0]", input_items[i])
        print("input_items[0] shape:", input_items[i].shape)
        print("spectra shape:", spectra.shape)
        spectra = np.append(spectra, input_items[i], axis=0)
        print("Done.")
        print("New spectra shape:", spectra.shape)
        i += 1
        print("Upcoming row #:", i, "/60")
    else:
        if __name__ == "__main__":
            print("Spectra:", spectra)
            print("Spectra shape:", spectra.shape)
            with mp.Pool(processes=1) as pool:         # start 1 worker processes
                result = pool.apply_async(hi_square, (spectra, 10)) # evaluates hi_square(spectra, 10) asynchronously in a single process
                print(result.get()) # should print "Hello world!", "Spectra shape: (5, 1000000)", and "10 squared: 100"
