#!/usr/bin/env python
# coding: utf-8

# In[1]:


def preprocessHomepage(url, rawData):
    if url == "https://www.cnn.com/":
        return "CNN Homepage Preprocessed"
    elif url == "https://www.foxnews.com/":
        return "Fox Homepage Preprocessed"
    elif url == "https://www.usatoday.com/":
        return "USA Today Homepage Preprocessed"
    elif url == "https://abcnews.go.com/":
        return "ABC Homepage Preprocessed"
    elif url == "https://www.cbsnews.com/":
        return "CBS Homepage Preprocessed"
    else:
        raise ValueError("The url passed in: "+url+" does not correspond to a known Homepage.")


# In[3]:


def preprocessArticle(url, rawData):
    if "https://www.cnn.com/" in url:
        return "CNN Article Preprocessed"
    elif "https://www.foxnews.com/" in url:
        return "Fox Article Preprocessed"
    elif "https://www.usatoday.com/" in url:
        return "USA Today Article Preprocessed"
    elif "https://abcnews.go.com/" in url:
        return "ABC Article Preprocessed"
    elif "https://www.cbsnews.com/" in url:
        return "CBS Article Preprocessed"
    else:
        return "Used the default Article Preprocessor"


# In[ ]:




