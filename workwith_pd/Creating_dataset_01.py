#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


data = {'Name': ["John", "Annal", "Peter", "Linda"],
'Location' : ["New York", "Paris", "Berlin", "London"],
'Age' : [24, 13, 53, 33],
}


# In[4]:


data_pandas = pd.DataFrame(data)


# In[5]:


data_pandas.head()


# In[4]:


display(data_pandas)


# In[5]:


# Select all rows that have an age column greater than 30
display(data_pandas[data_pandas.Age > 30])

