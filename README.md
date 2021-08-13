# A turboSETI block for GNU Radio

This is a GNU Radio Out of Tree (OOT) Module for the DopplerFinder Sink block. The aim of DopplerFinder Sink is to perform turboSETI analysis on a `numpy.float32` data matrix stored in RAM. 

This code has been tested on Linux.

### Dependencies

- [turboseti-stream](https://github.com/luigifcruz/turboseti-stream)
- [turboSETI]
- [blimpy]
- [GNU Radio version 3.8]

### Background

This project was undertaken as part of the Berkeley SETI Research Center 2021 summer REU. My mentors were Dr. Wael Farah (SETI Institute), and Dr. Steve Croft (Breakthrough Listen, UC Berkeley).

The aim of my project is to develop a SETI data processing pipeline for the Allen Telescope Array (ATA), using GNU Radio. The ATA is a radio interferometer operated by the SETI Institute at the Hat Creek Radio Observatory in California, and consists of 42 fully-steerable antennae, each 6.1m in diameter. Its main science goal is to perform searches for technosignatures, which appear as narrowband signals 'drifting' in frequency. 

Currently, the existing data-processing pipeline for the ATA uses custom hardware unavailable to those not on-site. GNU Radio is a free open-source software for developing signal-processing routines, and is used by a large community of amateur radio astronomers and enthusiasts. The implementation of a GNU Radio SETI pipeline will make the search for extraterrestrial intelligence more accesible to smaller radio observatories and citizen scientists.

### Pipeline Details

The GNU Radio SETI pipeline is outlined as follows:
1. Radio telescope data from the ATA streams in through a USRP source;
2. The data is 'channelised' through a polyphase filterbank, followed by a Fast Fourier Transform (FFT). This creates a high-spectral resolution product on the order of ~1MHz;
3. This product accumulates in DopplerFinder Sink's internal buffer for ~60s, to create a data matrix of shape (60, 1e6);
4. An adapted version of turboSETI (i.e. turboseti_stream) analyses this data matrix for potential technosignatures.

Example flowgraph (.grc file in examples folder):
(insert screenshot of flowgraph here)

### Next Steps

1. Integrate DopplerFinder Sink block into GNU Radio (current issue: `TypeError: cannot pickle 'SwigPyObject' object`)
2. (Optional:) Automate plotting of dynamic spectra of hits
3. Observe known technosignature source (e.g. Chang'e 5) using the GNU Radio SETI pipeline
4. Begin ATA observations of interesting stars using the GNU Radio SETI pipeline

I plan to continue working on this project into the academic year.

### Acknowledgements

Richard Elkins and Luigi Cruz did a significant amount of work on developing turboseti_stream. Luigi also helped a lot with   the structure of the flowgraph, particularly the polyphase filterbank and FFT components. Daniel Estévez and Derek Kozel answered many, many questions about GNU Radio and using Python multiprocessing. Lastly, Wael Farah was very patient and helped me wade through a hordes upon hordes of bugs.

Thank you all!

This project was made possible by funding from Breakthrough Listen.

### References

(insert here)
