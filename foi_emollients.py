#!/usr/bin/env python
# coding: utf-8

# # Reports of fires or burns relating to emollients, both paraffin-based and paraffin-free, reported to the UK's MHRA Yellow Card Scheme 

# #### This notebook visualises data obtained via a Freedom of Information (FOI) request made [here](https://www.whatdotheyknow.com/request/deaths_and_adverse_events_from_f) which represents data from 01/01/2010 to 27/10/2020

# In[1]:


# import libraries required for analysis 
import numpy as np 
import pandas as pd
from pylab import savefig
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# import data 
df = pd.read_csv("data.csv",thousands=',')


# In[3]:


df.head()


# In[4]:


df.describe()


# In[7]:


df.dtypes


# In[10]:


# plotting the number of deaths overtime using seaborn

plt.figure(figsize=(12,8))
ax = sns.barplot(data=df, x="year", y="fatal", color="navy")
plt.xlabel(' ')
plt.ylabel('No. of deaths', fontsize=15)

plt.savefig("fig1_deaths.png", dpi=600)


# In[ ]:




