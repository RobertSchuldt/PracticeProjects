#!/usr/bin/env python
# coding: utf-8

# In[170]:


import pandas as pd
import numpy as np


# In[171]:


import requests
import json


# In[172]:


###Now I must create url to request the data pull
url = "https://usafactsstatic.blob.core.windows.net/public/2020/coronavirus-timeline/allData.json"


# In[173]:


response = requests.get(url)


# In[174]:



if response.status_code == 200:
    print("Sucessfull Connection to API")
elif response.status_code == 404:
    print("Not Found")


# In[175]:


JSONContent = response.json()


# In[176]:


print(JSONContent[0])


# In[177]:


###Now I am going to dump this into a pandas data frame
dataset= pd.read_json(url, orient ='values')
dataset


# In[178]:


dataset.dtypes


# In[179]:


clean = dataset[['deaths', 'confirmed']]


# In[180]:


#what does the data look like. I have alists within a variable. Will need to extract out to columns
clean.head()


# In[181]:


clean.to_numpy()
clean2 = pd.DataFrame(clean.deaths.values.tolist(), index= clean.index)


# In[182]:


clean2


# In[183]:


#assigns a better name to the columns so I can tell what the time frame is. Will repeat for the confirmed

clean2.columns = ['entry_'+str(col)+'_death' for col in clean2.columns]


# In[184]:


clean2


# In[185]:


clean = dataset[['confirmed']]
clean.to_numpy()
clean3 = pd.DataFrame(clean.confirmed.values.tolist(), index= clean.index)
clean3.columns = ['entry_'+str(col)+'_confirmed' for col in clean3.columns]


# In[186]:


clean3


# In[187]:


clean4 = dataset[['popul','countyFIPS', 'county' , 'stateAbbr' , 'stateFIPS']]


# In[ ]:





# In[188]:


covid_set = clean4.join(clean2, how ='outer')
covid_set = covid_set.join(clean3, how = 'outer')


# In[189]:


covid_set


# In[190]:


covid_set.to_csv('covid_set.csv', header=True, index=True)
print("Sucessful file write")
### These numbers reflect cumulative totals in January 22nd, 2020.. Last updated April 13 


# In[ ]:




