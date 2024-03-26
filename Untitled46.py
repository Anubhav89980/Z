#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = [4, 8, 15, 16, 23, 42]
series = pd.Series(data)
print(series)


# In[2]:


import pandas as pd

data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
series_from_list = pd.Series(data_list)
print(series_from_list)


# In[3]:


import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
print(df)


# In[4]:


# DataFrame example
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)

# Series example
series = pd.Series([1, 2, 3, 4, 5])
print(series)


# In[5]:


import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Print the first few rows of the DataFrame
print(df.head())



# In[6]:


import pandas as pd

# Create multiple Series
names = pd.Series(['Alice', 'Bob', 'Charlie'])
ages = pd.Series([25, 30, 35])
cities = pd.Series(['New York', 'Los Angeles', 'Chicago'])

# Create a DataFrame using the Series
df = pd.DataFrame({'Name': names, 'Age': ages, 'City': cities})
print(df)


# In[ ]:




