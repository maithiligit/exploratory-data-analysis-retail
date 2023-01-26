#!/usr/bin/env python
# coding: utf-8

# ![sparks.jpg](attachment:sparks.jpg)

# # Author: Pagare Maithili
# 
# ## The Sparks Foundation - Data Science and Business Analytics 
# 
# ### Task 3: Exploratory Data Analysis - Retail
# 
# Problem Statement: Perform ‘Exploratory Data Analysis’ on dataset ‘SampleSuperstore’ This task is about Exploratory Data Analysis - Retail where the task focuses on a business manager who will try to find out weak areas where he can work to make more profit.
# 
# Dataset: https://bit.ly/3i4rbWl

# #### Importing Libraries

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import warnings
warnings.filterwarnings('ignore')


# In[3]:


df = pd.read_csv('SampleSuperstore.csv') 
df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


df.describe()


# In[7]:


df.isnull().sum() 


# In[8]:


df.info()


# In[9]:


df.columns


# In[10]:


df.duplicated().sum()


# In[11]:


df.nunique()


# In[12]:


df['Postal Code'] = df['Postal Code'].astype('object')


# In[13]:


df.drop_duplicates(subset=None,keep='first',inplace=True)
df.duplicated().sum()


# In[14]:


corr = df.corr()
sns.heatmap(corr,annot=True,cmap='Reds')


# In[15]:


df = df.drop(['Postal Code'],axis = 1) 


# In[16]:


sns.pairplot(df, hue = 'Ship Mode')


# In[17]:


df['Ship Mode'].value_counts()


# In[18]:


sns.countplot(x=df['Ship Mode'])


# In[19]:


df['Segment'].value_counts()        


# In[20]:


sns.pairplot(df,hue = 'Segment')     


# In[21]:


sns.countplot(x = 'Segment',data = df, palette = 'rainbow')


# In[22]:


df['Category'].value_counts()


# In[23]:


sns.countplot(x='Category',data=df,palette='tab10')


# In[24]:


sns.pairplot(df,hue='Category')


# In[25]:


df['Sub-Category'].value_counts()


# In[26]:


plt.figure(figsize=(15,12))
df['Sub-Category'].value_counts().plot.pie(autopct='dark')
plt.show()


# # Observation 1
# 
#     Maximum are from Binders, Paper, furnishings, Phones, storage, art, accessories and minimum from copiers, machines, suppliers

# In[27]:


df['State'].value_counts()


# In[28]:


plt.figure(figsize=(15,12))
sns.countplot(x='State',data=df,palette='rocket_r',order=df['State'].value_counts().index)
plt.xticks(rotation=90)
plt.show()


# # Observation 2
# 
#     Highest number of buyers are from California and New York

# In[29]:


df.hist(figsize=(10,10),bins=50)
plt.show()


# # Observation 3
# 
#     -Most customers tends to buy quantity of 2 and 3
#     -Discount give maximum is 0 to 20 percent

# In[30]:


plt.figure(figsize=(10,8))
df['Region'].value_counts().plot.pie(autopct = '%1.1f%%')
plt.show()


# ## Profit vs Discount

# In[31]:


fig,ax=plt.subplots(figsize=(20,8))
ax.scatter(df['Sales'],df['Profit'])
ax.set_xlabel('Sales')
ax.set_ylabel('Profit')
plt.show()


# In[32]:


sns.lineplot(x='Discount',y='Profit',label='Profit',data=df)
plt.legend()
plt.show()


# # Observation 4
# 
#     -No correlation between profit and discount
# 
# 
# ## Profit vs Quantity
# 

# In[33]:


sns.lineplot(x='Quantity',y='Profit',label='Profit',data=df)
plt.legend()
plt.show()


# In[34]:


df.groupby('Segment')[['Profit','Sales']].sum().plot.bar(color=['pink','blue'],figsize=(8,5))
plt.ylabel('Profit/Loss and sales')
plt.show()


# # Observation 5
#     
#     -Profit and sales are maximum in consumer segment and minimum in Home Office segment

# In[35]:


plt.figure(figsize=(12,8))
plt.title('Segment wise Sales in each Region')
sns.barplot(x='Region',y='Sales',data=df,hue='Segment',order=df['Region'].value_counts().index,palette='rocket')
plt.xlabel('Region',fontsize=15)
plt.show()


# # Observation 6
# 
#     -Segment wise sales are almost same in every region

# In[36]:


df.groupby('Region')[['Profit','Sales']].sum().plot.bar(color=['blue','red'],figsize=(8,5))
plt.ylabel('Profit/Loss and sales')
plt.show()


# # Observation 7
#     
#     -Profit and sales are maximum in west region and minimum in south region

# In[41]:


ps = df.groupby('State')[['Sales','Profit']].sum().sort_values(by='Sales',ascending=False)
ps[:].plot.bar(color=['blue','orange'],figsize=(15,8))
plt.title('Profit/loss & Sales across states')
plt.xlabel('States')
plt.ylabel('Profit/loss & Sales')
plt.show()


# # Observation 8
# 
#     -high profit is for california, new york
#     -loss is for texas, pennsylvania, Ohio

# In[38]:


t_states = df['State'].value_counts().nlargest(10)
t_states


# In[39]:


df.groupby('Category')[['Profit','Sales']].sum().plot.bar(color=['yellow','purple'],alpha=0.9,figsize=(8,5))
plt.ylabel('Profit/Loss and sales')
plt.show()


# # Observation 9
# As a business manager, try to find out the weak areas where you can work to make more profit?
# 
#     -Technology and Office Supplies have high profit.
#     -Furniture have less profit

# In[40]:


ps = df.groupby('Sub-Category')[['Sales','Profit']].sum().sort_values(by='Sales',ascending=False)
ps[:].plot.bar(color=['red','lightblue'],figsize=(15,8))
plt.title('Profit/loss & Sales across states')
plt.xlabel('Sub-Category')
plt.ylabel('Profit/loss & Sales')
plt.show()


# # Observation 10
# Phones sub-category have high sales.
# chairs have high sales but less profit compared to phones
# Tables and Bookmarks sub-categories facing huge loss
# 
# 
# Thank You <3
