#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Astrocyte_data = pd.read_csv('https://github.com/HackBio-Internship/public_datasets/raw/main/R/datasets/astrocyte_data', delimiter = '\t')
Astrocyte_data
#check  for missing dataset
Astrocyte_data.isnull().sum() #no missing data
#check for correlation between different values
sns.heatmap(Astrocyte_data.corr(), cbar = True, annot = True, cmap = 'Blues')

#scatter plots
plt.scatter(x='MFN1_1', y='MFN1_2', data=Astrocyte_data)
plt.xlabel('MFN1_1')
plt.ylabel('MFN1_2')
plt.title("MFN1_2 BY MFN1_1")
plt.savefig('mfn1_2.png', dpi=100)

plt.scatter(x='MFN1', y='MFN1_2', data=Astrocyte_data)
plt.xlabel('MFN1')
plt.ylabel('MFN1_2')
plt.title("MFN1_2 BY MFN1")
plt.savefig('mfn1_3.png', dpi=100)

plt.scatter(x='MFN1_1', y='MFN1_4', data=Astrocyte_data)
plt.xlabel('MFN1_1')
plt.ylabel('MFN1_4')
plt.title("MFN1_4 BY MFN1_1")
plt.savefig('mfn1_4.png', dpi=100)

plt.scatter(x='MFN1_2', y='MFN1_4', data=Astrocyte_data)
plt.xlabel('MFN1_2')
plt.ylabel('MFN1_4')
plt.title("MFN1_4 BY MFN1_2")
plt.savefig('mfn1_5.png', dpi=100)

plt.scatter(x='WT_1', y='WT_3', data=Astrocyte_data)
plt.xlabel('WT_1')
plt.ylabel('WT_3')
plt.title("WT_3 BY WT_1")
plt.savefig('mfn1_6.png', dpi=100)

plt.scatter(x='WT_1', y='WT_4', data=Astrocyte_data)
plt.xlabel('WT_1')
plt.ylabel('WT_4')
plt.title("WT_4 BY WT_1")
plt.savefig('mfn1_7.png', dpi=100)

plt.scatter(x='WT_3', y='WT_4', data=Astrocyte_data)
plt.xlabel('WT_3')
plt.ylabel('WT_4')
plt.title("WT_4 BY WT_3")
plt.savefig('mfn1_8.png', dpi=100)

plt.scatter(x='MFN1', y='WT', data=Astrocyte_data)
plt.xlabel('MFN1')
plt.ylabel('WT')
plt.title("WT BY MFN1")
plt.savefig('mfn1_9.png', dpi=100)

