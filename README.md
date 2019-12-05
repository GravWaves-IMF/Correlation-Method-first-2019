# Correlation-Method-first-2019-
**Alex B. Nielsen<sup>1</sup>, Felicia Frederiksson<sup>2</sup>, Paolo Marcoccia<sup>1</sup>, and Germano Nardini<sup>1</sup>**

<sub>1. University of Stavanger, Institutt for Matematikk og Fysikk, Kjølv Egelands hus, 5.etg, E-blokk, 4021 Stavanger, Norway </sub>  
<sub>2. University of Uppsala, Department of Physics and Astronomy,Ångströmlaboratoriet, Lägerhyddsvägen 1, 751 20 Uppsala, Sweden</sub>  

## Introduction ##

In the following, we use the Pearson cross-correlation statistic proposed by [Liu and Jackson](http://iopscience.iop.org/article/10.1088/1475-7516/2016/10/014/meta),
and employed by [Creswell et al.](http://iopscience.iop.org/article/10.1088/1475-7516/2017/08/013/meta), [Nielsen et al.](https://arxiv.org/abs/1811.04071) to look for statistically significant correlations between
the _LIGO_ Hanford and Livingston detectors at the time of the binary black hole mergers detected during _O1_.
Furthermore, the same analysis will be done for event _GW170104_, as problems concerning the residual correlation of the detectors were raised also for that particular event of _O2_ [Creswell et al.](http://iopscience.iop.org/article/10.1088/1475-7516/2017/08/013/meta).
The analysis will follow the same pipelines used in [GW150914_investigation](https://github.com/gwastro/gw150914_investigation), in particular, we will generate the residuals.hdf file for each event by subtracting the Maximum-Likelihood Waveforms generated by [Biwer et al.](https://github.com/gwastro/pycbc-inference-paper), while the raw strain data of the detectors at the time of the events will be obtained by [GWOSC](https://www.gw-openscience.org/catalog/GWTC-1-confident/).
However, we'll use whitened data of the events for the following analysis, and instead of estimating the cross-correlations among the two detectors at the coalescence time suggested by the posteriors, we'll run a new pipeline that will determine the correlations (with a fixed time shift, both for rough strain and residuals) in function of a _200ms_ wide GPS time around the event.
By doing so, we may both observe how the correlations evolve in function of physical time and find the best coalescence time for each event, in order to maximize the correlation value of the original data or the difference among original data and residuals after the subtraction.
The obtained values of the correlations, will then be evaluated from a statistical point of view, by comparing them with the cross-correlation obtained from both simulated Gaussian noise and data from the LIGO detectors, at times during which no detection of gravitational waves has been claimed.
For each event, as a different frequency range was used for the whitening, will be generated a whitened background both for simulated Gaussian noise and data from the LIGO detectors, in order to define the significance of the correlations by comparing with a custom-built environment.     
We find that after subtracting the maximum likelihood waveform, there are no statistically significant correlations between the residuals of the two detectors at the time of all the events reported above.

## Analysis Details ##

Details of the analaysis can be found in our [preprint paper](http://google.com/2r09324).

## Additional Material ##

In order to reproduce the results of our paper, an [Anaconda](https://www.anaconda.com/distribution/) environment with _python 2.7_ is needed.
The supplementary libraries needed, may be checked from the file [init_module.py](https://github.com/GravWaves-IMF/Correlation-Method-first-2019-/blob/master/Code/init_module.py).
In particular :

- The notebooks, require the installation of [PyCBC](https://pycbc.org/) v1.12.4 and [LALSuite](https://git.ligo.org/lscsoft/lalsuite) 6.49, which contains version 1.8.0 of the LALSimulation library used to generate the maximum likelihood waveform. Both of these libraries can be installed using [pip](https://pip.pypa.io/en/stable/) with the command:
```sh
pip install 'pycbc==1.12.4' 'lalsuite==6.49'
```
- Some function will require a _C_, _C++_ compiler in order to run, the [GCC](https://gcc.gnu.org/) compiler may be easily installed by running : 

```sh
sudo apt-get update
sudo apt-get install build-essential
```

- A new version of the file [res.py](https://github.com/GravWaves-IMF/Correlation-Method-first-2019-/blob/master/Code/res.py) is available in the code directory. The latter, need to be copied and pasted in the directory  
```sh
/home/*username*/anaconda2/lib/python2.7/site-packages
```
## How to run the Correlation Analysis ##

The Correlation Analysis, will be run for a single event at a time.
The steps to do in order to generate the results of our paper are :

1. Download the data of the two detectors *_H1_*,*_L1_* for the event you wish to analyze from [GWOSC](https://www.gw-openscience.org/catalog/GWTC-1-confident/), we used the  
