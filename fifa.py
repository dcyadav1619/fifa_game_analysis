#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the required libraries
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


fifa=pd.read_csv('players_20.csv')


# In[3]:


fifa.head()


# In[4]:


for col in fifa.columns: 
    print(col) 


# In[5]:


fifa.shape


# In[ ]:


18278*104


# In[ ]:


1667/18278


# In[6]:


fifa['nationality'].value_counts()


# In[7]:


fifa['nationality'].value_counts()[0:10]


# In[9]:


fifa['nationality'].value_counts()[0:5].keys()


# In[8]:


fifa['nationality'].value_counts()[0:5]


# In[10]:


plt.figure(figsize=(5,5))
plt.bar(list(fifa['nationality'].value_counts()[0:5].keys()),list(fifa['nationality'].value_counts()[0:5]),color="g")
plt.show()        


# In[11]:


player_salary = fifa[['short_name','wage_eur']]


# In[12]:


player_salary.head()


# In[14]:


player_salary=player_salary.sort_values(by=['wage_eur'],ascending=False)


# In[15]:


player_salary.head()


# In[16]:


plt.figure(figsize=(8,5))
plt.bar(list(player_salary['short_name'])[0:5],list(player_salary['wage_eur'])[0:5],color=["blue","green","red","pink","orange"])
plt.show()


# In[17]:


fifa['nationality']=='Germany'


# In[18]:


#Germany
Germany=fifa[fifa['nationality']=='Germany']
Germany.head(10)


# In[19]:


Germany.sort_values(by=['height_cm'],ascending=False).head()


# In[20]:


Germany.sort_values(by=['weight_kg'],ascending=False).head()


# In[21]:


Germany.sort_values(by=['wage_eur'],ascending=False).head()


# In[22]:


Germany[['short_name','wage_eur']].sort_values(by=['wage_eur'],ascending=False).head()


# In[ ]:


#Shooting


# In[ ]:





# In[23]:


player_shooting= fifa[['short_name','shooting']]


# In[24]:


player_shooting.sort_values(by=['shooting'],ascending=False).head()


# In[ ]:


#defending


# In[25]:


player_defending= fifa[['short_name','defending','nationality','club']]


# In[26]:


player_defending.sort_values(by=['defending'],ascending=False).head()


# In[27]:


real_madrid=fifa[fifa['club']=='Real Madrid']


# In[28]:


real_madrid.sort_values(by=['wage_eur'],ascending=False).head()


# In[29]:


real_madrid.sort_values(by=['shooting'],ascending=False).head()


# In[30]:


real_madrid.sort_values(by=['defending'],ascending=False).head()


# In[31]:


real_madrid['nationality'].value_counts()


# In[ ]:




