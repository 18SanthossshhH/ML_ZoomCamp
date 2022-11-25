#!/usr/bin/env python
# coding: utf-8

# In[14]:


get_ipython().run_line_magic('autosave', '0')


# In[9]:


import requests


# In[10]:


url = 'http://localhost:9696/predict'


# In[11]:


customer = {
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 1,
    "monthlycharges": 29.85,
    "totalcharges": 29.85
}


# In[12]:


response = requests.post(url, json=customer).json()
response


# In[13]:


customer_xyz = 'xyz-123'
if response['churn'] == True :
    print(F'Sending Promo Email to {customer_xyz}')


# In[ ]:




