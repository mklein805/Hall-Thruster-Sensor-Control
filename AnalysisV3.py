#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 08:10:00 2022

@author: marissaklein
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import datetime

plt.rcParams['figure.dpi'] = 700
plt.rcParams['savefig.dpi'] = 700


path = os.getcwd()
Odir_list = os.listdir(path)
dir_list = []

for x in Odir_list:
    if x.endswith(".csv"):
        dir_list.append(x)
        
dir_list = sorted(dir_list)
print(dir_list)

#%%
#ForceThermoValues42022271453.csv
file = dir_list[0]
print(file)
df = pd.read_csv(file,on_bad_lines='skip')
path = file + 'plots'
if os.path.isdir(path) == False:
    os.mkdir(path)


unixTime, timeStamp, secStamp, force, thermocoupleOne, thermocoupleTwo = [], [], [], [], [], []

for x in range(len(df)):
    unixTime.append(df['Unix Time'][x])
    force.append(df['Actual Force'][x])
    thermocoupleOne.append(df['Thermocouple Value One'][x])
    thermocoupleTwo.append(df['Thermocouple Value Two'][x])
    
for x in range(len(thermocoupleOne)):
    val = thermocoupleOne[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleOne[x] = np.nan
    
        
for x in range(len(thermocoupleTwo)):
    val = thermocoupleTwo[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleTwo[x] = np.nan
        
for x in unixTime:
    dt = datetime.datetime.fromtimestamp(x)
    dt = dt.time()
    timeStamp.append(dt)

'''    
leng = len(timeStamp)
t1 = timeStamp[0]
t2 = timeStamp[leng - 1]
c = t2 - t1
t_elapsed = c.total_seconds()
'''        
       
fig1 = plt.figure('Force vs. Time',figsize=(15,7))
plt.plot(unixTime,force)
plt.title('Force Vs. Time')
plt.xlabel("UTC")
plt.ylabel('Force (N)')
plt.savefig(path+'//'+file+'Force.png')

fig2 = plt.figure('Thermocouple 1 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleOne,c='red')
plt.title('Thermocouple 1 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T1.png')


fig3 = plt.figure('Thermocouple 2 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleTwo,c='green')
plt.title('Thermocouple 2 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T2.png')
#%%
file = dir_list[1]
print(file)
df = pd.read_csv(file,on_bad_lines='skip')
path = file + 'plots'
if os.path.isdir(path) == False:
    os.mkdir(path)


unixTime, force, thermocoupleOne, thermocoupleTwo = [], [], [], []

for x in range(len(df)):
    unixTime.append(df['Unix Time'][x])
    force.append(df['Actual Force'][x])
    thermocoupleOne.append(df['Thermocouple Value One'][x])
    thermocoupleTwo.append(df['Thermocouple Value Two'][x])
    
for x in range(len(thermocoupleOne)):
    val = thermocoupleOne[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleOne[x] = np.nan
    
        
for x in range(len(thermocoupleTwo)):
    val = thermocoupleTwo[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleTwo[x] = np.nan
        
       
fig4 = plt.figure('Force vs. Time',figsize=(15,7))
plt.plot(unixTime,force)
plt.title('Force Vs. Time')
plt.xlabel("UTC")
plt.ylabel('Force (N)')
plt.savefig(path+'//'+file+'Force.png')

fig5 = plt.figure('Thermocouple 1 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleOne,c='red')
plt.title('Thermocouple 1 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T1.png')


fig6 = plt.figure('Thermocouple 2 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleTwo,c='green')
plt.title('Thermocouple 2 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T2.png')
#%%
file = dir_list[2]
print(file)
df = pd.read_csv(file,on_bad_lines='skip')
path = file + 'plots'
if os.path.isdir(path) == False:
    os.mkdir(path)


unixTime, force, thermocoupleOne, thermocoupleTwo = [], [], [], []

for x in range(len(df)):
    unixTime.append(df['Unix Time'][x])
    force.append(df['Actual Force'][x])
    thermocoupleOne.append(df['Thermocouple Value One'][x])
    thermocoupleTwo.append(df['Thermocouple Value Two'][x])
    
for x in range(len(thermocoupleOne)):
    val = thermocoupleOne[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleOne[x] = np.nan
    
        
for x in range(len(thermocoupleTwo)):
    val = thermocoupleTwo[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleTwo[x] = np.nan
        
       
fig4 = plt.figure('Force vs. Time',figsize=(15,7))
plt.plot(unixTime,force)
plt.title('Force Vs. Time')
plt.xlabel("UTC")
plt.ylabel('Force (N)')
plt.savefig(path+'//'+file+'Force.png')

fig5 = plt.figure('Thermocouple 1 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleOne,c='red')
plt.title('Thermocouple 1 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T1.png')


fig6 = plt.figure('Thermocouple 2 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleTwo,c='green')
plt.title('Thermocouple 2 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T2.png')
#%%
file = dir_list[3]
print(file)
df = pd.read_csv(file,on_bad_lines='skip')
path = file + 'plots'
if os.path.isdir(path) == False:
    os.mkdir(path)


unixTime, force, thermocoupleOne, thermocoupleTwo = [], [], [], []

for x in range(len(df)):
    unixTime.append(df['Unix Time'][x])
    force.append(df['Actual Force'][x])
    thermocoupleOne.append(df['Thermocouple Value One'][x])
    thermocoupleTwo.append(df['Thermocouple Value Two'][x])
    
for x in range(len(thermocoupleOne)):
    val = thermocoupleOne[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleOne[x] = np.nan
        
for x in range(len(thermocoupleTwo)):
    val = thermocoupleTwo[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleTwo[x] = np.nan
        
       
fig4 = plt.figure('Force vs. Time',figsize=(15,7))
plt.plot(unixTime,force)
plt.title('Force Vs. Time')
plt.xlabel("UTC")
plt.ylabel('Force (N)')
plt.savefig(path+'//'+file+'Force.png')

fig5 = plt.figure('Thermocouple 1 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleOne,c='red')
plt.title('Thermocouple 1 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T1.png')


fig6 = plt.figure('Thermocouple 2 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleTwo,c='green')
plt.title('Thermocouple 2 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T2.png')
#%%
file = dir_list[4]
print(file)
df = pd.read_csv(file,on_bad_lines='skip')
path = file + 'plots'
if os.path.isdir(path) == False:
    os.mkdir(path)


unixTime, force, thermocoupleOne, thermocoupleTwo = [], [], [], []

for x in range(len(df)):
    unixTime.append(df['Unix Time'][x])
    force.append(df['Actual Force'][x])
    thermocoupleOne.append(df['Thermocouple Value One'][x])
    thermocoupleTwo.append(df['Thermocouple Value Two'][x])
    
   
for x in range(len(thermocoupleOne)):
    val = thermocoupleOne[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleOne[x] = np.nan
    
        
for x in range(len(thermocoupleTwo)):
    val = thermocoupleTwo[x]
    val = val[1:]
    val = val[:-2]
    if val == "Something wrong with thermocouple!":
        val = np.nan
    if val != np.nan:
        val = float(val)
    thermocoupleTwo[x] = val
      
fig4 = plt.figure('Force vs. Time',figsize=(15,7))
plt.plot(unixTime,force)
plt.title('Force Vs. Time')
plt.xlabel("UTC")
plt.ylabel('Force (N)')
plt.savefig(path+'//'+file+'Force.png')

fig5 = plt.figure('Thermocouple 1 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleOne,c='red')
plt.title('Thermocouple 1 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T1.png')


fig6 = plt.figure('Thermocouple 2 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleTwo,c='green')
plt.title('Thermocouple 2 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T2.png')  
#%%
file = dir_list[5]
print(file)
df = pd.read_csv(file,on_bad_lines='skip')
path = file + 'plots'
if os.path.isdir(path) == False:
    os.mkdir(path)


unixTime, force, thermocoupleOne, thermocoupleTwo = [], [], [], []

for x in range(len(df)):
    unixTime.append(df['Unix Time'][x])
    force.append(df['Actual Force'][x])
    thermocoupleOne.append(df['Thermocouple Value One'][x])
    thermocoupleTwo.append(df['Thermocouple Value Two'][x])
    
for x in range(len(thermocoupleOne)):
    val = thermocoupleOne[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleOne[x] = np.nan
    
        
for x in range(len(thermocoupleTwo)):
    val = thermocoupleTwo[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleTwo[x] = np.nan
        
       
fig4 = plt.figure('Force vs. Time',figsize=(15,7))
plt.plot(unixTime,force)
plt.title('Force Vs. Time')
plt.xlabel("UTC")
plt.ylabel('Force (N)')
plt.savefig(path+'//'+file+'Force.png')

fig5 = plt.figure('Thermocouple 1 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleOne,c='red')
plt.title('Thermocouple 1 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T1.png')


fig6 = plt.figure('Thermocouple 2 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleTwo,c='green')
plt.title('Thermocouple 2 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T2.png')
#%%
file = dir_list[6]
print(file)
df = pd.read_csv(file,on_bad_lines='skip')
path = file + 'plots'
if os.path.isdir(path) == False:
    os.mkdir(path)


unixTime, force, thermocoupleOne, thermocoupleTwo = [], [], [], []

for x in range(len(df)):
    unixTime.append(df['Unix Time'][x])
    force.append(df['Actual Force'][x])
    thermocoupleOne.append(df['Thermocouple Value One'][x])
    thermocoupleTwo.append(df['Thermocouple Value Two'][x])
    
for x in range(len(thermocoupleOne)):
    val = thermocoupleOne[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleOne[x] = np.nan
    if type(val) == 'string':
        thermocoupleOne[x] = np.nan
    
        
for x in range(len(thermocoupleTwo)):
    val = thermocoupleTwo[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleTwo[x] = np.nan
    if type(val) == 'string':
        thermocoupleTwo[x] = np.nan
        
       
fig4 = plt.figure('Force vs. Time',figsize=(15,7))
plt.plot(unixTime,force)
plt.title('Force Vs. Time')
plt.xlabel("UTC")
plt.ylabel('Force (N)')
plt.savefig(path+'//'+file+'Force.png')

fig5 = plt.figure('Thermocouple 1 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleOne,c='red')
plt.title('Thermocouple 1 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T1.png')


fig6 = plt.figure('Thermocouple 2 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleTwo,c='green')
plt.title('Thermocouple 2 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T2.png')
#%%
file = dir_list[7]
print(file)
df = pd.read_csv(file,on_bad_lines='skip')
path = file + 'plots'
if os.path.isdir(path) == False:
    os.mkdir(path)


unixTime, force, thermocoupleOne, thermocoupleTwo = [], [], [], []

for x in range(len(df)):
    unixTime.append(df['Unix Time'][x])
    force.append(df['Actual Force'][x])
    thermocoupleOne.append(df['Thermocouple Value One'][x])
    thermocoupleTwo.append(df['Thermocouple Value Two'][x])
    
for x in range(len(thermocoupleOne)):
    val = thermocoupleOne[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleOne[x] = np.nan
    
        
for x in range(len(thermocoupleTwo)):
    val = thermocoupleTwo[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleTwo[x] = np.nan
        
       
fig4 = plt.figure('Force vs. Time',figsize=(15,7))
plt.plot(unixTime,force)
plt.title('Force Vs. Time')
plt.xlabel("UTC")
plt.ylabel('Force (N)')
plt.savefig(path+'//'+file+'Force.png')

fig5 = plt.figure('Thermocouple 1 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleOne,c='red')
plt.title('Thermocouple 1 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T1.png')


fig6 = plt.figure('Thermocouple 2 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleTwo,c='green')
plt.title('Thermocouple 2 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T2.png')
#%%
file = dir_list[8]
print(file)
df = pd.read_csv(file,on_bad_lines='skip')
path = file + 'plots'
if os.path.isdir(path) == False:
    os.mkdir(path)


unixTime, force, thermocoupleOne, thermocoupleTwo = [], [], [], []

for x in range(len(df)):
    unixTime.append(df['Unix Time'][x])
    force.append(df['Actual Force'][x])
    thermocoupleOne.append(df['Thermocouple Value One'][x])
    thermocoupleTwo.append(df['Thermocouple Value Two'][x])
    
for x in range(len(thermocoupleOne)):
    val = thermocoupleOne[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleOne[x] = np.nan
    
        
for x in range(len(thermocoupleTwo)):
    val = thermocoupleTwo[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleTwo[x] = np.nan
        
       
fig4 = plt.figure('Force vs. Time',figsize=(15,7))
plt.plot(unixTime,force)
plt.title('Force Vs. Time')
plt.xlabel("UTC")
plt.ylabel('Force (N)')
plt.savefig(path+'//'+file+'Force.png')

fig5 = plt.figure('Thermocouple 1 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleOne,c='red')
plt.title('Thermocouple 1 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T1.png')


fig6 = plt.figure('Thermocouple 2 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleTwo,c='green')
plt.title('Thermocouple 2 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T2.png')
#%%
file = dir_list[9]
print(file)
df = pd.read_csv(file,on_bad_lines='skip')
path = file + 'plots'
if os.path.isdir(path) == False:
    os.mkdir(path)


unixTime, force, thermocoupleOne, thermocoupleTwo = [], [], [], []

for x in range(len(df)):
    unixTime.append(df['Unix Time'][x])
    force.append(df['Actual Force'][x])
    thermocoupleOne.append(df['Thermocouple Value One'][x])
    thermocoupleTwo.append(df['Thermocouple Value Two'][x])
    
for x in range(len(thermocoupleOne)):
    val = thermocoupleOne[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleOne[x] = np.nan
    
        
for x in range(len(thermocoupleTwo)):
    val = thermocoupleTwo[x]
    val = val[1:]
    val = val[:-2]
    if val == "Something wrong with thermocouple!":
        val = np.nan
    if val != np.nan:
        val = float(val)
    thermocoupleTwo[x] = val
        
       
fig4 = plt.figure('Force vs. Time',figsize=(15,7))
plt.plot(unixTime,force)
plt.title('Force Vs. Time')
plt.xlabel("UTC")
plt.ylabel('Force (N)')
plt.savefig(path+'//'+file+'Force.png')

fig5 = plt.figure('Thermocouple 1 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleOne,c='red')
plt.title('Thermocouple 1 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T1.png')


fig6 = plt.figure('Thermocouple 2 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleTwo,c='green')
plt.title('Thermocouple 2 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T2.png')
#%%
#TODO PROBLEM CHILD
file = dir_list[10]
print(file)
df = pd.read_csv(file)
path = file + 'plots'
if os.path.isdir(path) == False:
    os.mkdir(path)

pd.set_option('display.max_columns', None)
print(df)

'''
unixTime, force, thermocoupleOne, thermocoupleTwo = [], [], [], []

for x in range(len(df)):
    unixTime.append(df['Unix Time'][x])
    force.append(df['Actual Force'][x])
    thermocoupleOne.append(df['Thermocouple Value One'][x])
    thermocoupleTwo.append(df['Thermocouple Value Two'][x])
 
for x in range(len(thermocoupleOne)):
    val = thermocoupleOne[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleOne[x] = np.nan
    if type(val) == 'string':
        thermocoupleOne[x] = np.nan
    
        
for x in range(len(thermocoupleTwo)):
    val = thermocoupleTwo[x]
    if val == " Something wrong with thermocouple!":
        thermocoupleTwo[x] = np.nan
    if type(val) == 'string':
        thermocoupleTwo[x] = np.nan
        
       
fig4 = plt.figure('Force vs. Time',figsize=(15,7))
plt.plot(unixTime,force)
plt.title('Force Vs. Time')
plt.xlabel("UTC")
plt.ylabel('Force (N)')
plt.savefig(path+'//'+file+'Force.png')

fig5 = plt.figure('Thermocouple 1 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleOne,c='red')
plt.title('Thermocouple 1 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T1.png')


fig6 = plt.figure('Thermocouple 2 vs. Time',figsize=(15,7))
plt.plot(unixTime,thermocoupleTwo,c='green')
plt.title('Thermocouple 2 vs. Time')
plt.xlabel('UTC')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.savefig(path+'//'+file+'T2.png')
'''   
