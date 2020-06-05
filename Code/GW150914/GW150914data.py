# data settings for the analysis of GW150914 signal
# times from run script in pycbc inference paper repo
hd_nm = 'LOSC_4_V2-1126257414-4096.gwf'
pst_nm = 'gw150914_posteriors_thinned.hdf'
psd_start_time = 1126258940
psd_end_time = 1126259980
data_start_time = 1126259452
data_end_time = 1126259468
pad_data = 8 # for the high pass filter
fhighpass = 15
psd_seg_len = 16
psd_seg_stride = 8
inverse_psd_len = 4
tc = 1126259462.39
cort = 1126259462.3891344
f_low = 35.
f_high = 350.	
sample_rate = 4096 # we'll just use the same as the LOSC data
basetime = 1126259462.3
timedl = 0.0069
tdlerr = 0.0005
ifos = ['H1','L1']
seg_len = data_end_time - data_start_time
filter_fmin = 20.
print ("segment length:", seg_len)
