#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


def getSource(url):
    req = requests.get(url)
    return req.text


# In[3]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


# In[4]:


def getArticles(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
    driver = webdriver.Chrome(options=chrome_options,executable_path='C:\Windows\Drivers\chromedriver')
    driver.get(url)
    articles = WebDriverWait(driver, timeout=20).until(lambda d: d.find_elements_by_tag_name('article'))
    driver.close()
    return articles

