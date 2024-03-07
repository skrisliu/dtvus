# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 05:30:36 2023

@author: sjliu
"""

from scipy.stats import kstest,entropy,binned_statistic,ks_2samp
from scipy.stats import wasserstein_distance
# Kolmogorov-Smirnov test
import numpy as np
import pickle
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import ttest_ind
import numpy_indexed as npi
from scipy.integrate import simpson

apath = r'M:\MTL4\t20240224_USDTR_r1/'
statecode = pd.read_csv(apath + 'doc/us-state-ansi-fips.csv')

months = ['01','02','03','04','05','06','07','08','09','10','11','12']
es1 = ['HISPANIC','WHITE','BLACK','ASIAN','OTHER']
es2 = ['LOW','MIDLOW','MID','MIDHIGH','HIGH']
es3 = ['LOW','MIDLOW','MID','MIDHIGH','HIGH']

datas1 = {} # race
datas2 = {} # income
datas3 = {} # age

#%%
def getCDF2(x1,x2):
    x0 = np.concatenate([x1,x2])
    bins = []
    for i in range(1,201):
        bins.append(np.percentile(x0,i/2))
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

def getCDF(x1, x2):
    x0 = np.concatenate([x1,x2])
    bins = []
    for i in range(1,101):
        bins.append(np.percentile(x0,i))
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


#%%
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
dfx7 = []
dfx8 = []

dfx9 = []
dfx10 = []
dfx11 = []

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
    res1 = kstest(cdf1a,cdf1b)
    res1b = wasserstein_distance(cdf1a,cdf1b)
    
    if False:
        fig = plt.figure(figsize=(5,4),dpi=80)
        plt.plot(bins,cdf1a,label='COLOR')
        plt.plot(bins,cdf1b,label='WHITE')
        plt.legend()
        plt.tight_layout()
        plt.show()
    
    
    #%% income
    each = 'LOW'
    for each in es2:
        datas = []
        for m in months:
            fp = 'saved1b_individual_income/'+_code+'_'+_stname+'_'+m+'_'+each+'.npy'
            data = np.load(fp)
            datas.append(data)
        data = np.array(datas)
        data = np.mean(data,axis=0)
        datas2[each] = data
    
    idx1 = np.isnan(datas2['LOW'])
    idx2 = np.isnan(datas2['HIGH'])
    x1 = datas2['LOW'][~idx1]
    x2 = datas2['HIGH'][~idx2]
    
    bins, cdf2a, cdf2b = getCDF(x1, x2)
    res2 = kstest(cdf2a,cdf2b)  
    res2b = wasserstein_distance(cdf2a,cdf2b)
    
    if False:
        fig = plt.figure(figsize=(5,4),dpi=80)
        plt.plot(bins,cdf2a,label='LOW')
        plt.plot(bins,cdf2b,label='HIGH')
        plt.legend()
        plt.tight_layout()
        plt.show()
    
    #%% age
    each = 'LOW'
    for each in es2:
        datas = []
        for m in months:
            fp = 'saved1c_individual_age/'+_code+'_'+_stname+'_'+m+'_'+each+'.npy'
            data = np.load(fp)
            datas.append(data)
        data = np.array(datas)
        data = np.mean(data,axis=0)
        datas2[each] = data
    
    idx1 = np.isnan(datas2['LOW'])
    idx2 = np.isnan(datas2['HIGH'])
    x1 = datas2['LOW'][~idx1]
    x2 = datas2['HIGH'][~idx2]
    
    bins, cdf3a, cdf3b = getCDF(x1, x2)
    res3 = kstest(cdf3a,cdf3b)  
    res3b = wasserstein_distance(cdf3a,cdf3b)
    
    if False:
        fig = plt.figure(figsize=(5,4),dpi=80)
        plt.plot(bins,cdf2a,label='LOW')
        plt.plot(bins,cdf2b,label='HIGH')
        plt.legend()
        plt.tight_layout()
        plt.show()

#%%
    dfx1.append(_code)
    dfx2.append(_stname)
    dfx3.append(res1.pvalue) # race
    dfx4.append(res2.pvalue) # income
    dfx5.append(res3.pvalue) # age
    
    dfx6.append(res1.statistic)
    dfx7.append(res2.statistic)
    dfx8.append(res3.statistic)
    
    dfx9.append(res1.statistic)
    dfx10.append(res2.statistic)
    dfx11.append(res3.statistic)
    
    cdfs = np.array([cdf1a,cdf1b,cdf2a,cdf2b,cdf3a,cdf3b])
    np.save('t20240224b_cdfs/cdfs-'+_code+'-'+_stname+'.npy', cdfs)
    
    
    
#%%
dfx = pd.DataFrame({'stcode': dfx1, 'stname': dfx2, 'kstestRace': dfx3, 
                    'kstestIncome': dfx4, 'kstestAge': dfx5, 'kstestRaceValue': dfx6, 
                    'kstestIncomeValue': dfx7, 'kstestAgeValue': dfx8,
                    'wasserstein_distanceRace': dfx9, 'wasserstein_distanceIncome': dfx10,
                    'wasserstein_distanceAge': dfx11})
# dfx.to_csv('doc/t20240224b_cdfs_wasserstein.csv')
    # 
    
    
    
    
    
    
    
    
    
    
    
    
    
    










