# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:23:56 2023

@author: sjliu
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# import geopandas as gpd
# from simpledbf import Dbf5
import pickle

MODE = 'DTR' # DAY, NIGHT, DTR

apath = r'M:\MTL4\t20240224_USDTR_r1/'
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

dfm = pd.read_pickle('savedtable/dfmtable_t20230509.pkl')

#%%
df0 = dfm[['OBJECTID', 'STATE_ABBR', 'STATE_FIPS', 'COUNTY_FIP', 'STCOFIPS',
       'TRACT_FIPS', 'FIPS', 'POPULATION', 'POP_SQMI', 'SQMI', 'Shape_Leng',
       'Shape_Area', 'xid', 'm01day', 'm01nig', 'm02day', 'm02nig', 'm03day',
       'm03nig', 'm04day', 'm04nig', 'm05day', 'm05nig', 'm06day', 'm06nig',
       'm07day', 'm07nig', 'm08day', 'm08nig', 'm09day', 'm09nig', 'm10day',
       'm10nig', 'm11day', 'm11nig', 'm12day', 'm12nig']]

#%% acs population
pops = pd.read_csv(apath+'acstable/ACSDP5Y2017.DP05-Data_clean.csv') # 74001

total = 'DP05_0001E' #Estimate!!SEX AND AGE!!Total population
latinx = 'DP05_0071E' #Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)
white = 'DP05_0077E' #Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!White alone
black = 'DP05_0078E' # Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Black or African American alone
asian = 'DP05_0080E' # Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Asian alone

other1 = 'DP05_0079E' # Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!American Indian and Alaska Native alone
other2 = 'DP05_0081E' # Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Native Hawaiian and Other Pacific Islander alone
other3 = 'DP05_0082E' # Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Some other race alone
other4 = 'DP05_0083E' # Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Two or more races

#%% 
geoids = []
states = []
cntys = []
tracts = []
pop1 = []
pop2 = []
pop3 = []
pop4 = []
pop5 = []
pop6 = []
for idx,row in pops.iterrows():
    state = row['GEO_ID'][9:11]
    cnty = row['GEO_ID'][11:14]
    tract = row['GEO_ID'][14:20]
    states.append(state)
    cntys.append(cnty)
    tracts.append(tract)
    pop1.append(row[total])
    pop2.append(row[latinx])
    pop3.append(row[white])
    pop4.append(row[black])
    pop5.append(row[asian])
    pop6.append(row[other1]+row[other2]+row[other3]+row[other4])
    
#%%
dfx = pd.DataFrame({'GEO_ID': pops['GEO_ID'], 'STATE': states, 'CNTY': cntys, 'TRACTS': tracts, 
                    'TOTAL': pop1, 'HISPANIC': pop2, 'WHITE': pop3, 'BLACK': pop4, 'ASIAN': pop5, 'OTHER': pop6})
    
    

#%% test on California
statecode = pd.read_csv(apath + 'doc/us-state-ansi-fips.csv')
_code = '06'
_stname = 'California'
diffs = []
for _idx,_row in statecode.iterrows():
    _code = _row['st']
    _code = f"{_code:02}"
    _stname = _row['stname']
    
    dfx1 = dfx[dfx['STATE']==_code] # CA: 8057->6863
    dfx1['FIPS'] = dfx1['STATE']+dfx1['CNTY']+dfx['TRACTS']
    dfx1 = dfx1.merge(df0,left_on='FIPS',right_on='FIPS')
    
    
    #% get exposure, for 12 months
    es = ['HISPANIC','WHITE','BLACK','ASIAN','OTHER']
    # expsweighted = {}
    std = {}
    q75 = {}
    q25 = {}
    q50 = {}
    means = {}
    for each in es:
        # expsweighted[each] = []
        std[each] = []
        q75[each] = []
        q25[each] = []
        q50[each] = []
        means[each] = []
    for count in range(1,13):
        name = f"{count:02}"
        exps = {}
        for each in es:
            exps[each] = [] 
        for idx,row in dfx1.iterrows():
            for each in es:
                exps[each].append(np.ones([row[each],])*(row['m'+name+'day']-row['m'+name+'nig']))

        for each in es:
            a2 = np.concatenate(exps[each])*0.02
            np.save('saved1a_individual_race/'+_code+'_'+_stname+'_'+name+'_'+each,a2)
            means[each].append(np.mean(a2))
            std[each].append(np.std(a2))
            q25[each].append(np.quantile(a2,0.25))
            q50[each].append(np.quantile(a2,0.5))
            q75[each].append(np.quantile(a2,0.75))
    
    output = {}
    output['mean'] = means
    output['std'] = std
    output['q25'] = q25
    output['q50'] = q50
    output['q75'] = q75
    expsweighted = means
    