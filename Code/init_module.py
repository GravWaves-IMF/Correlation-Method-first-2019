# This program, simply import all the modules needed to run the 
# Pycbc simulation for a GW event

import matplotlib
import seaborn
from matplotlib import pyplot as plt 
plt.style.use('seaborn-whitegrid')
import h5py
import numpy as np
import pandas as pd
import os
import res
import warnings
warnings.simplefilter(action = 'ignore', category=FutureWarning)
import pylab

from multiprocessing import Process, Queue, Pool
from pycbc.types import TimeSeries, zeros
import pycbc.noise.reproduceable as noise
from pycbc.io.inference_hdf import InferenceFile
from pycbc.waveform.generator import FDomainCBCGenerator, FDomainDetFrameGenerator
from pycbc import psd as pypsd
from pycbc import filter
from pycbc.filter import resample_to_delta_t
from pycbc import frame
from pycbc import waveform
from scipy.stats import ks_2samp
