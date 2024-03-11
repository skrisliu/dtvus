# -*- coding: utf-8 -*-
"""
Released 20240307

Racial and Ethnic Minorities Disproportionately Exposed to Extreme Daily Temperature Variation in the United States

@author: skrisliu
skrisliu@gmail.com

Create the Big Figure 2 in race/ethnicity

# INPUT
    -- "us-state-ansi-fips_plotindex.csv": plot index, to control plot location for each state
    -- "ksTable_race.csv": KS distance statistics for each state
    -- files within folder "plot1hist_data_mean"

"""

import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.special import kl_div

apath = r'M:\MTL4\t20240224_USDTR_r1\release20240307/'
statecode = pd.read_csv(apath + 'doc/us-state-ansi-fips_plotindex.csv')

statecode= pd.merge(left=statecode,right=pd.read_csv(apath + 'doc/ksTable_race.csv'),left_on='stname',right_on='stname')


#%%
fig = plt.figure(figsize=(27.5,20),dpi=100)

#%
for idx,row in statecode.iterrows():
    count = row['st']
    _code = f"{count:02}"
    _stname = row['stname']
    _stshort = row['stusps']
    
    fp0 = 'plot1hist_data_mean/'
    
    data1 = np.load(fp0+_code+_stname+'_white.npy')
    data2 = np.load(fp0+_code+_stname+'_color.npy')
    delta = np.load(fp0+_code+_stname+'_delta.npy')
    delta2 = delta*1.8
    
    plt.subplot(8,11,row['plot'])


    ax = plt.gca()
    ax.set_facecolor('#F2F2F2')
    if row['KS_Race_stats0']>=0.1:
        ax.set_facecolor('#FEF2CD')
        _stshort = _stshort+'*'
    if row['KS_Race_stats0']>=0.2:
        ax.set_facecolor('#FCDE83')
        _stshort = _stshort+'*'
    if row['KS_Race_stats0']>=0.3:
        ax.set_facecolor('#F9C31F')
        _stshort = _stshort+'*'
        

    plt.vlines(x=data1[data1[:,1].argmax()][0], ymin=0,ymax=data1[:,1].max(), ls='-',alpha=1.0, color='gray', lw=1)
    plt.vlines(x=data1[data2[:,1].argmax()][0], ymin=0,ymax=data2[:,1].max(), ls='-',alpha=1.0, color='gray', lw=1)
    
    
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
    plt.xlim(0.47,1.53)
    plt.text(0.46,4.58,_stshort,fontsize=22,horizontalalignment='left',verticalalignment='bottom')
    plt.text(0.50,5.55,'scale: '+"%.1f" % delta +'°C (' + "%.1f" %  delta2 +'°F)' ,fontsize=11,horizontalalignment='left',verticalalignment='bottom')
plt.tight_layout()
plt.savefig('Figure2_race.svg') 
plt.savefig('Figure2_race.pdf') 
plt.savefig('Figure2_race.png') 
plt.show()