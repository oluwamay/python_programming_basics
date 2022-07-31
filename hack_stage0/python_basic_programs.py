#!/usr/bin/env python
# coding: utf-8

# In[ ]:


31 * 78 #multiply int values
697 / 41 #divide int values
56765 - 23 #subtract int values
#variable assignment
x = 39
y = 14
z = x - y

#math function
import math
a = math.sqrt(2345)
print(a)
b = math.log2(a)
print(b)

#Lists
vec1 = [2, 5, 8, 12, 16]
vec2 = list(range(2, 300, 3))
print(len(vec2))
print(vec2[4], vec2[9], vec2[14], vec2[19])
print(vec2[9:29])

#import libraries for data science
import numpy as np
import pandas as pd
#Creating numpy arrays
mouse_colour = np.array(['purple','red','yellow','brown'])
mouse_weight = np.array([23, 21, 18, 16])

#merge two arrays to give a matrix
mouse_inf = np.vstack([mouse_colour, mouse_weight])
mouse_inf

#convert numpy to pandas dataframe
mouse_info = pd.DataFrame({'colour': mouse_inf[0,:], 'weight': mouse_inf[1,:]})
mouse_info

#Read files
small_file = pd.read_csv('https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/small_file.txt', delimiter = '\t')
small_file
child_variant = pd.read_csv('https://github.com/HackBio-Internship/public_datasets/blob/main/R/Child_Variants.csv?raw=true')
child_variant
print(child_variant.head())

#mean of values in column MutantReadPercent of child_variant
print(child_variant['MutantReadPercent'].mean())

#filter data
filtered_MRP = child_variant.loc[child_variant['MutantReadPercent'] >= 70]
filtered_MRP

#import the famous irish dataframe
irish_df = pd.read_csv('https://datahub.io/machine-learning/iris/r/iris.csv')
irish_df

print(irish_df.loc[irish_df['class'] == 'Iris-virginica']) #prints dataframe for iris-virginica

#libraries for plots
import matplotlib.pyplot as plt
import seaborn as sns

#resize plot
plt.figure(figsize=(9,6))

#rearrange irish_df
irish_dff = pd.melt(irish_df, id_vars="class")
irish_dff
#plot group barchat
sns.barplot(x = 'class', y = 'value',  data = irish_dff, hue = 'variable')
plt.xlabel("Class")
plt.ylabel("Values")
plt.title("IRISH FLOWER BAR PLOT") 
plt.savefig('irish plot.png', dpi=200)
plt.show()


# In[ ]:




