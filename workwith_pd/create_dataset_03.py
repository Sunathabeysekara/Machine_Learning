#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

# Example data for multiple features
X1 = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1, 1)
X2 = np.array([1.5, 1.2, 0.9, 0.4, 0.6, 0.7, 2.3, 2.0, 2.4, 2.1, 1.9, 2.5]).reshape(-1, 1)
X3 = np.array([10, 20, 15, 5, 6, 7, 25, 30, 35, 28, 22, 27]).reshape(-1, 1)

y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])  # Target values

# Combine features into one array
X = np.hstack((X1, X2, X3))  # Combine X1, X2, and X3 horizontally

# Create a DataFrame from the combined feature array
df = pd.DataFrame(X, columns=['Feature_1', 'Feature_2', 'Feature_3'])  # Naming columns
df['Target'] = y  # Add target variable as a new column

# Display the DataFrame
print(df)


# In[2]:


print(df.loc[0])


# In[4]:


print(df.loc[[0, 1]])


# In[5]:


import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df2 = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df2) 


# In[ ]:


#pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)
#index-> label of the index
#columns-> label of columns

