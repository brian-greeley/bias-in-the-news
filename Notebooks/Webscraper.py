#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


def getSource(url):
    req = requests.get(url)
    return req.text

