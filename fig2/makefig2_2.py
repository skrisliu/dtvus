# -*- coding: utf-8 -*-
"""
Released 20240307

@author: skrisliu
skrisliu@gmail.com

# INPUT
    -- "us-state-ansi-fips.csv": state code
    -- the individual files within saved1a_individual_race, generated from makefig2_1.py

# CREATE:
    -- folder "plot1hist_data_mean": to save KDE estimation
    
# OUTPUT
    -- files within folder "plot1hist_data_mean": distributions estimated from KDE, each state

# WARNING: this script will take ~30 mins to run
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


'''
# change here if you want only the exposure in May
'''
MODE = 'MEAN'  # "May"
# MODE = 'MAY'  

apath = r'M:\MTL4\t20240224_USDTR_r1\release20240307/'  # change apath to the folder

months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

#%%
es = ['HISPANIC','WHITE','BLACK','ASIAN','OTHER']
ms = []
for count in range(1,13):
    name = f"{count:02}"
    ms.append(name)
statecode = pd.read_csv(apath + 'doc/us-state-ansi-fips.csv')

#%%
SKIP = 0
for idx,row in statecode.iterrows():
    # SKIP+=1  # this process can take ~30 minutes. Created this in case the need of start half-way
    # if SKIP<8:
        # continue
    
    #%% For debug purpose to show individual state
    # _code = '09'
    # _stname = 'Connecticut'
    
    _stname = row['stname']
    count = row['st']
    _code = f"{count:02}"
    
    data = {}
    for each in es:
        data[each] = []
    for each in es:
        for m in ms:
            x = np.load('saved1a_individual_race/'+_code+'_'+_stname+'_'+m+'_'+each+'.npy')   # output from makefig2_1.py
            data[each].append(x)
    #%%
    xx = {}
    for each in es:
        if MODE=='MEAN':
            xx[each] = np.mean(data[each],axis=0)
        if MODE=='MAY':
            xx[each] = data[each][4]
    xx['COLOR'] = np.concatenate([xx['HISPANIC'],xx['BLACK'],xx['ASIAN'],xx['OTHER']])
    
    delta = np.nanmean(xx['WHITE'])
    np.save('plot1hist_data_mean/'+_code+_stname+'_delta.npy',delta) # save White's exposure as the scale factor
    
    #%%
    es2 = ['HISPANIC','WHITE','BLACK','ASIAN','OTHER','COLOR']
    
    xx2 = {}
    xx3 = {}
    for each in es2:
        xx2[each] = xx[each][~np.isnan(xx[each])]-delta
        xx3[each] = xx[each][~np.isnan(xx[each])]/delta
    

    
    #%%
    fig = plt.figure(figsize=(4,3),dpi=100)
    plt.axvline(x=1.0, ymin=0,ymax=4, ls='--',alpha=1.0, color='gray', lw=1)
    sns.kdeplot(xx3[es2[1]], bw=0.5, color='#1F2E7A', fill=True, alpha=0.8)
    sns.kdeplot(xx3[es2[-1]], bw=0.5, color='#C91D42', fill=True, alpha=0.8)
    sns.kdeplot(xx3[es2[1]], bw=0.5, color='w', alpha=1)
    sns.kdeplot(xx3[es2[-1]], bw=0.5, color='w', alpha=1)
    ax = plt.gca()
    a1 = ax.lines[1].get_xydata()
    a2 = ax.lines[2].get_xydata()
    np.save('plot1hist_data_mean/'+_code+_stname+'_white.npy',a1)  # save KED estimation of white
    np.save('plot1hist_data_mean/'+_code+_stname+'_color.npy',a2)  # save KED estimation of non-white
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(True)
    xrange = [0.4,0.6,0.8,1.0,1.2,1.4,1.6]
    plt.xticks(xrange,xrange)
    # yrange = [0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0]
    yrange = [0,1,2,3,4,5,6]
    plt.yticks(yrange,yrange)
    plt.ylabel('')
    plt.ylim(0,6.2)
    plt.xlim(0.33,1.67)
    # plt.xlabel('Relative Daily Temperature Variation',fontsize=10)
    plt.text(0.38,5.4,_stname,fontsize=10,horizontalalignment='left',verticalalignment='bottom')
    plt.text(0.38,4.9,'Scale='+"%.2f" % delta +'°C',fontsize=10,horizontalalignment='left',verticalalignment='bottom')
    plt.tight_layout()
    # plt.savefig('plot1hist_data_mean_fig/'+_code+_stname+'.pdf') # these figures will be made together in the later stage. Uncomment to see them individually now
    # plt.savefig('plot1hist_data_mean_fig/'+_code+_stname+'.svg')
    # plt.savefig('plot1hist_data_mean_fig/'+_code+_stname+'.png')
    plt.show()



































































