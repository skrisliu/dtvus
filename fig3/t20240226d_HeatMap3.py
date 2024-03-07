# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 23:21:12 2022

@author: sjliu
"""

import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import copy

#%%
statecode = pd.read_csv('doc/us-state-ansi-fips.csv')

alldata = {}

# output['pop'] = np.array([dfx1['TOTAL'].sum(),dfx1['HISPANIC'].sum(),dfx1['WHITE'].sum(),dfx1['ASIAN'].sum(),dfx1['OTHER'].sum(),dfx1['COLOR'].sum()])
for _idx,_row in statecode.iterrows():
    _code = _row['st']
    _code = f"{_code:02}"
    _stname = _row['stname']
    
    with open('out1pkl_race/'+_code + '_' + _stname +'.pkl', 'rb') as handle:
        b = pickle.load(handle)
        alldata[_stname] = b
        

keys = list(alldata.keys())
        
mx1 = []
mx2 = []
mx3 = []
mx4 = []
mx5 = []
field = 'mean'
for each in alldata.keys():
    mx1.append(alldata[each][field]['WHITE'])
    mx2.append(alldata[each][field]['HISPANIC'])
    mx3.append(alldata[each][field]['BLACK'])
    mx4.append(alldata[each][field]['ASIAN'])
    mx5.append(alldata[each][field]['OTHER'])
    
#%
delta = np.mean(mx1,axis=-1)
mx1 = np.array(mx1)
mx2 = np.array(mx2)
mx3 = np.array(mx3)
mx4 = np.array(mx4)
mx5 = np.array(mx5)

# for i in range(mx1.shape[0]):
#     mx1[i,:] = mx1[i,:]/delta[i]
#     mx2[i,:] = mx2[i,:]/delta[i]
#     mx3[i,:] = mx3[i,:]/delta[i]
#     mx4[i,:] = mx4[i,:]/delta[i]
#     mx5[i,:] = mx5[i,:]/delta[i]


mxx = np.array([mx1,mx2,mx3,mx4,mx5])
diff = np.max(mxx,axis=0)-np.min(mxx,axis=0)
diff1 = copy.deepcopy(diff)


#%%
statecode = pd.read_csv('doc/us-state-ansi-fips.csv')

alldata = {}
keys2 = []

# output['pop'] = np.array([dfx1['TOTAL'].sum(),dfx1['LOW'].sum(),dfx1['MIDLOW'].sum(),dfx1['MID'].sum(),dfx1['MIDHIGH'].sum(),dfx1['HIGH'].sum()])
for _idx,_row in statecode.iterrows():
    _code = _row['st']
    _code = f"{_code:02}"
    _stname = _row['stname']
    keys2.append(_row['stusps'])
    
    with open('out1pkl_income/'+_code + '_' + _stname +'.pkl', 'rb') as handle:
        b = pickle.load(handle)
        alldata[_stname] = b
       
#%
keys = list(alldata.keys())
        
mx1 = []
mx2 = []
mx3 = []
mx4 = []
mx5 = []
mx6 = []
mx7 = []
pop1 = []
pop0 = []
field = 'mean'
for each in alldata.keys():
    mx1.append(alldata[each][field]['LOW'])
    mx2.append(alldata[each][field]['MIDLOW'])
    mx3.append(alldata[each][field]['MID'])
    mx4.append(alldata[each][field]['MIDHIGH'])
    mx5.append(alldata[each][field]['HIGH'])
    
#%
mx1 = np.array(mx1)
mx2 = np.array(mx2)
mx3 = np.array(mx3)
mx4 = np.array(mx4)
mx5 = np.array(mx5)

# for i in range(mx1.shape[0]):
#     mx1[i,:] = mx1[i,:]/delta[i]
#     mx2[i,:] = mx2[i,:]/delta[i]
#     mx3[i,:] = mx3[i,:]/delta[i]
#     mx4[i,:] = mx4[i,:]/delta[i]
#     mx5[i,:] = mx5[i,:]/delta[i]

mxx = np.array([mx1,mx2,mx3,mx4,mx5])
diff = np.max(mxx,axis=0)-np.min(mxx,axis=0)
diff2 = copy.deepcopy(diff)

dff2b = (np.mean(mx1,axis=1)+np.mean(mx2,axis=1))/2-(np.mean(mx5,axis=1)+np.mean(mx4,axis=1))/2

#%%
statecode = pd.read_csv('doc/us-state-ansi-fips.csv')

alldata = {}

# output['pop'] = np.array([dfx1['TOTAL'].sum(),dfx1['LOW'].sum(),dfx1['MIDLOW'].sum(),dfx1['MID'].sum(),dfx1['MIDHIGH'].sum(),dfx1['HIGH'].sum()])
for _idx,_row in statecode.iterrows():
    _code = _row['st']
    _code = f"{_code:02}"
    _stname = _row['stname']
    
    with open('out1pkl_age/'+_code + '_' + _stname +'.pkl', 'rb') as handle:
        b = pickle.load(handle)
        alldata[_stname] = b
       
#%
keys = list(alldata.keys())
        
mx1 = []
mx2 = []
mx3 = []
mx4 = []
mx5 = []
mx6 = []
mx7 = []
pop1 = []
pop0 = []
field = 'mean'
for each in alldata.keys():
    mx1.append(alldata[each][field]['LOW'])
    mx2.append(alldata[each][field]['MIDLOW'])
    mx3.append(alldata[each][field]['MID'])
    mx4.append(alldata[each][field]['MIDHIGH'])
    mx5.append(alldata[each][field]['HIGH'])
    
#%
mx1 = np.array(mx1)
mx2 = np.array(mx2)
mx3 = np.array(mx3)
mx4 = np.array(mx4)
mx5 = np.array(mx5)

# for i in range(mx1.shape[0]):
#     mx1[i,:] = mx1[i,:]/delta[i]
#     mx2[i,:] = mx2[i,:]/delta[i]
#     mx3[i,:] = mx3[i,:]/delta[i]
#     mx4[i,:] = mx4[i,:]/delta[i]
#     mx5[i,:] = mx5[i,:]/delta[i]

mxx = np.array([mx1,mx2,mx3,mx4,mx5])
diff = np.max(mxx,axis=0)-np.min(mxx,axis=0)
diff3 = copy.deepcopy(diff)

dff3b = np.mean(mx1,axis=1)-np.mean(mx5,axis=1)


#%% change order
# d = np.mean(diff1,axis=1)
# idx = np.argsort(-d)
idx = np.arange(0,51,1)


keys3 = []
for each in idx:
    keys3.append(keys2[each])

#%%
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.transforms as mtransforms


fmax = 5.4

month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

xx = np.arange(12)

# fig, ax = plt.subplots(1,3,figsize=(13,17.5),dpi=60)
fig, ax = plt.subplots(1,3,figsize=(13,17.5),dpi=60)

plt.sca(ax[0])
ax[0].imshow(diff1[idx],cmap='magma',vmin=0,vmax=fmax/1.8)
# ax[0].imshow(diff1[idx],cmap='magma',vmin=0,vmax=0.3)
plt.xticks(xx,month)
# plt.yticks(np.arange(51),keys)
plt.yticks(np.arange(51),keys3)
plt.title('By ethnicity')



plt.sca(ax[1])
ax[1].imshow(diff2[idx],cmap='magma',vmin=0,vmax=fmax/1.8)
# ax[1].imshow(diff2[idx],cmap='magma',vmin=0,vmax=0.3)
plt.xticks(xx,month)
plt.gca().set_yticks([])
plt.title('By income')


plt.sca(ax[2])
im = ax[2].imshow(diff3[idx],cmap='magma',vmin=0,vmax=fmax/1.8)
# im = ax[2].imshow(diff3[idx],cmap='magma',vmin=0,vmax=0.3)
plt.xticks(xx,month)
plt.gca().set_yticks([])
plt.title('By age')

# colorbar
#fig.subplots_adjust(right=1)
cbar_ax = fig.add_axes([0.25, 0.97, 0.5, 0.015])
clb = fig.colorbar(im, cax=cbar_ax, orientation="horizontal")
# clb.ax.set_title('$^{\circ}$C')


#% C to F
pos = clb.ax.get_position()
clb.ax.set_aspect('auto')
ax = plt.gca()
plt.text(1.035,-0.62,r'$^{\circ}$C',fontsize=12,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
plt.text(1.035,1.58,r'$^{\circ}$F',fontsize=12,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
ax2 = clb.ax.twiny()
ax2.set_xlim([0.0,fmax])
plt.subplots_adjust(wspace=0.3)

# pos0 = ax[0].get_position()
# pos1 = ax[1].get_position()
# pos2 = ax[2].get_position()
#


plt.subplots_adjust(left=0.03, bottom=0.02, right=0.99, top=0.94, wspace=0.03, hspace=0)
#plt.tight_layout(pad=1.08)

plt.savefig('fig20240226/allDTRmix3.svg')
plt.savefig('fig20240226/allDTRmix3.pdf')
plt.savefig('fig20240226/allDTRmix3.png')
plt.show()

#%%
if False:
    out0 = keys2
    out1 = diff1[idx]
    out2 = diff2[idx]
    out3 = diff3[idx]















