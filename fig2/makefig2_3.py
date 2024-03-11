# -*- coding: utf-8 -*-
"""
Released 20240307

@author: skrisliu
skrisliu@gmail.com 

# INPUT
    -- files within folder "plot1hist_data_mean", generated from makefig2_2.py
    -- "us-state-ansi-fips.csv": state code

# OUTPUT
    -- "doc/kstable_race.csv": table including the KS-test result, of race/ethnicity, each state
    
# WARNING: this script will take ~10 mins to run
"""

from scipy.stats import kstest
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

###
apath = r'M:\MTL4\t20240224_USDTR_r1\release20240307/'  # change apath to the folder
statecode = pd.read_csv(apath + 'doc/us-state-ansi-fips.csv')

months = ['01','02','03','04','05','06','07','08','09','10','11','12']

# only race/ethnicity will be used
es1 = ['HISPANIC','WHITE','BLACK','ASIAN','OTHER']
es2 = ['LOW','MIDLOW','MID','MIDHIGH','HIGH']
es3 = ['LOW','MIDLOW','MID','MIDHIGH','HIGH']

datas1 = {} # race

#%% function to get CDF
def getCDF(x1, x2):
    x0 = np.concatenate([x1,x2])
    bins = []
    n = 200   # control bins here, we tested 200/500. This value only matters for guessing a p-value
    step = n/100
    for i in range(1,n+1):
        bins.append(np.percentile(x0,i/step))
    bins = np.array(bins)
    
    tmp1 = np.digitize(x1, bins)
    tmp1b = []
    for i in range(bins.shape[0]):
        tmp1b.append(np.sum(tmp1==i))
    tmp1b = np.array(tmp1b)
    tmp1b = tmp1b/tmp1b.sum()
    tmp1c = []
    for i in range(bins.shape[0]):
        tmp1c.append(np.sum(tmp1b[:i]))
    
    tmp2 = np.digitize(x2, bins)
    tmp2b = []
    for i in range(bins.shape[0]):
        tmp2b.append(np.sum(tmp2==i))
    tmp2b = np.array(tmp2b)
    tmp2b = tmp2b/tmp2b.sum()
    tmp2c = []
    for i in range(bins.shape[0]):
        tmp2c.append(np.sum(tmp2b[:i]))
    
    tmp1c = np.array(tmp1c)
    tmp2c = np.array(tmp2c)
    return bins, tmp1c, tmp2c

#%% Get KS statistics, each state
_code = '44'
_stname = 'Rhode Island'

_code = '35'
_stname = 'New Mexico'

m = '05'
each = 'HISPANIC'

dfx1 = []
dfx2 = []
dfx3 = []
dfx4 = []
dfx5 = []
dfx6 = []


for idx,row in statecode.iterrows():
    _code = str(row['st']).zfill(2)
    _stname = row['stname']
    print(_stname)

    for each in es1:
        datas = []
        for m in months:
            fp = 'saved1a_individual_race/'+_code+'_'+_stname+'_'+m+'_'+each+'.npy'
            data = np.load(fp)
            datas.append(data)
        data = np.array(datas)
        data = np.mean(data,axis=0)
        datas1[each] = data
    
    datas1['COLOR'] = np.concatenate([datas1['HISPANIC'],datas1['BLACK'],datas1['ASIAN']])
    
    idx1 = np.isnan(datas1['COLOR'])
    idx2 = np.isnan(datas1['WHITE'])
    x1 = datas1['COLOR'][~idx1]
    x2 = datas1['WHITE'][~idx2]
    
    bins, cdf1a, cdf1b = getCDF(x1, x2)
    res1b = kstest(cdf1a,cdf1b) # on bin data
    res1 = kstest(x1,x2)  # on original data
    
    if False:
        fig = plt.figure(figsize=(5,4),dpi=80)
        plt.plot(bins,cdf1a,label='COLOR')
        plt.plot(bins,cdf1b,label='WHITE')
        plt.legend()
        plt.tight_layout()
        plt.show()
    
#%% 
    dfx1.append(_code)
    dfx2.append(_stname)
    dfx3.append(res1.pvalue) # original, p-value
    dfx4.append(res1.statistic) # original, stats value
    dfx5.append(res1b.statistic) # bin data, stats value
    dfx6.append(res1b.pvalue) # bin data, p-value

    
#%%
dfx = pd.DataFrame({'stcode': dfx1, 'stname': dfx2, 'KS_Race_pvalue0': dfx3,
                    'KS_Race_stats0': dfx4, 'KS_Race_stats_bin200': dfx5, 
                    'KS_Race_pvaluebin200': dfx6}) 
dfx.to_csv(apath + 'doc/ksTable_race.csv')
    
    
    
    
    
    
    
    
    
    
    
    
    










