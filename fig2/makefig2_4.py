# -*- coding: utf-8 -*-
"""
Created on Tue May  9 18:14:35 2023

@author: sjliu
"""

import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.special import kl_div

apath = r'M:\MTL4\t20240224_USDTR_r1/'
statecode = pd.read_csv(apath + 'doc/us-state-ansi-fips_plotindex.csv')

statecode= pd.merge(left=statecode,right=pd.read_csv('doc/t20240224d_cdfs_wasserstein_bin500.csv'),left_on='stname',right_on='stname')


#%%
fig = plt.figure(figsize=(27.5,20),dpi=100)

#%
for idx,row in statecode.iterrows():
    count = row['st']
    _code = f"{count:02}"
    _stname = row['stname']
    _stshort = row['stusps']
    
    fp0 = 'plot1hist_data_mean/'
    # fp0 = 'plot6hist_data_May/'
    
    data1 = np.load(fp0+_code+_stname+'_white.npy')
    data2 = np.load(fp0+_code+_stname+'_color.npy')
    delta = np.load(fp0+_code+_stname+'_delta.npy')
    delta2 = delta*1.8
    
    plt.subplot(8,11,row['plot'])
    
    
    
    # plt.data1[data1[:,1].argmax()]
    ax = plt.gca()
    ax.set_facecolor('#F2F2F2')
    if row['ksvalue2race']>=0.1:
        ax.set_facecolor('#FEF2CD')
        _stshort = _stshort+'*'
    if row['ksvalue2race']>=0.2:
        ax.set_facecolor('#FCDE83')
        _stshort = _stshort+'*'
    if row['ksvalue2race']>=0.3:
        ax.set_facecolor('#F9C31F')
        _stshort = _stshort+'*'
        
    # if row['kstestRace']<0.05:
    #     ax.set_facecolor('#EBEDFA')
    #     _stshort = _stshort+'*'
    # if row['kstestRace']<0.01:
    #     ax.set_facecolor('#D6DBF5')
    #     _stshort = _stshort+'*'

    plt.vlines(x=data1[data1[:,1].argmax()][0], ymin=0,ymax=data1[:,1].max(), ls='-',alpha=1.0, color='gray', lw=1)
    plt.vlines(x=data1[data2[:,1].argmax()][0], ymin=0,ymax=data2[:,1].max(), ls='-',alpha=1.0, color='gray', lw=1)
    
    # plt.plot()
    # plt.plot(data1[:,0],data1[:,1],color='#1F2E7A', fill=True, alpha=0.8)
    # plt.plot(data1[:,0],data1[:,1],color='w', alpha=1)
    # plt.plot(data2[:,0],data2[:,1],color='#C91D42', fill=True, alpha=0.8)
    # plt.plot(data2[:,0],data2[:,1],color='w', alpha=1)
    
    plt.fill(data1[:,0],data1[:,1],color='#1F2E7A', alpha=0.8)
    plt.fill(data2[:,0],data2[:,1],color='#C91D42', alpha=0.6)
    
    plt.plot(data1[:,0],data1[:,1],color='#1F2E7A', alpha=1)
    plt.plot(data2[:,0],data2[:,1],color='#C91D42', alpha=1)
    

    
    ax = plt.gca()
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)
    xrange = [0.4,0.6,0.8,1.0,1.2,1.4,1.6]    
    # xrange = [0.6,1.0,1.4]    
    plt.xticks(xrange,xrange)
    yrange = [0,1,2,3,4,5,6]
    plt.yticks(yrange,yrange)
    plt.ylabel('')
    plt.ylim(0,6.2)
    # plt.xlim(0.33,1.67)
    # plt.text(0.32,4.58,_stshort,fontsize=22,horizontalalignment='left',verticalalignment='bottom')
    # plt.text(0.38,5.55,'scale='+"%.1f" % delta +'°C',fontsize=12,horizontalalignment='left',verticalalignment='bottom')
    plt.xlim(0.47,1.53)
    plt.text(0.46,4.58,_stshort,fontsize=22,horizontalalignment='left',verticalalignment='bottom')
    plt.text(0.50,5.55,'scale: '+"%.1f" % delta +'°C (' + "%.1f" %  delta2 +'°F)' ,fontsize=11,horizontalalignment='left',verticalalignment='bottom')
plt.tight_layout()
plt.savefig('fig20240224/statedtrc.svg') 
plt.savefig('fig20240224/statedtrc.pdf') 
plt.savefig('fig20240224/statedtrc.png') 
plt.show()