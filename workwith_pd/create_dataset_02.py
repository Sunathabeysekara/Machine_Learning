#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd


# In[8]:


X=np.array([3.78,2.44,2.09,0.14,1.72,1.65,4.92,4.37,4.96,4.52,3.69,5.88]).reshape(-1,1)


# In[9]:


y=np.array([0,0,0,0,0,0,1,1,1,1,1,1])


# In[10]:


# Create a DataFrame from the numpy arrays
df = pd.DataFrame(X, columns=['Feature'])  # Create DataFrame for X
df['Target'] = y  # Add y as a new column in the DataFrame

# Display the DataFrame
print(df)


# In[11]:


print(X)


# In[12]:


print(y)

