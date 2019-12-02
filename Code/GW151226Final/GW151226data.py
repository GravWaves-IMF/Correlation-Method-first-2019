# data settings for the analysis of GW150914 signal
# times from run script in pycbc inference paper repo
hd_nm = 'GWOSC_4KHZ_R1-1135134303-4096.gwf'
pst_nm = 'gw151226_posteriors_thinned.hdf'
psd_start_time = 1135136250
psd_end_time = 1135136868
data_start_time = 1135136340
data_end_time = 1135136356
tc = 	1135136350.6
cort =  1135136350.6196449
basetime = 1135136350.53
timedl = 0.0011
tdlerr = 0.0003
ifos = ['H1','L1']
pad_data = 8 # for the high pass filter
f_low = 50.
f_high = 460.
psd_seg_len = 16
psd_seg_stride = 8
inverse_psd_len = 4
fhighpass = 15.
filter_fmin = 20.
sample_rate = 4096 # we'll just use the same as the LOSC data
seg_len = data_end_time - data_start_time
print "segment length:", seg_len
