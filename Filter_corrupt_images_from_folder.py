#!/usr/bin/env python
# coding: utf-8

# In[10]:


from os import listdir
from PIL import Image


# In[12]:


for filename in listdir('./'):
    if filename.endswith(".jpg"):
        try:
            fn = "./" + filename
            img = Image.open(fn)
            img.verify()
        except (IOError, SyntaxError) as e:
            os.remove(fn)


# In[ ]:




