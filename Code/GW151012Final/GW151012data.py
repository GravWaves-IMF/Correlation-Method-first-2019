# data settings for the analysis of GW150914 signal
# times from run script in pycbc inference paper repo
hd_nm = 'GWOSC_4KHZ_R1-1128676853-4096.gwf'
pst_nm = 'lvt151012_posteriors_thinned.hdf'
psd_start_time = 1128678378
psd_end_time = 1128679418
data_start_time = 1128678890
data_end_time = 1128678906
basetime = 1128678900.33
tc = 1128678900.4
cort = 1128678900.418144
timedl = -0.0006
tdlerr = 0.0006
ifos = ['H1','L1']
pad_data = 8 # for the high pass filter
f_low = 50.
f_high = 230.
psd_seg_len = 16
psd_seg_stride = 8
inverse_psd_len = 4
fhighpass = 15.
filter_fmin = 20.
sample_rate = 4096 # we'll just use the same as the LOSC data
seg_len = data_end_time - data_start_time
print "segment length:", seg_len
