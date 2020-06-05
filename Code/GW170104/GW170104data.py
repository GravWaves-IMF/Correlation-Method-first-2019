# data settings for the analysis of GW150914 signal
# times from run script in pycbc inference paper repo
hd_nm = 'GWOSC_4KHZ_R1-1167557889-4096.gwf'
pst_nm = 'gw170104_posteriors_thinned.hdf'
psd_start_time = 1167559416.0
psd_end_time = 1167560456.0
data_start_time = 1167559928.0
data_end_time = 1167559944.0
basetime = 1167559936.5
tc = 	1167559936.6
cort = 1167559936.5731215
timedl = -0.003
tdlerr = 0.0005
ifos = ['H1','L1']
pad_data = 8 # for the high pass filter
f_low = 50.
f_high = 230.
fhighpass = 15.
filter_fmin = 20.
psd_seg_len = 16
psd_seg_stride = 8
inverse_psd_len = 4
sample_rate = 4096 # we'll just use the same as the LOSC data
seg_len = data_end_time - data_start_time
print "segment length:", seg_len
