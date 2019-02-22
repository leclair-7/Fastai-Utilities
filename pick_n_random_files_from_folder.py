#!/usr/bin/env python
# coding: utf-8

# In[16]:


import os, shutil
import numpy as np


# In[17]:



foldername = "test_images_v1"
files = os.listdir("./" + foldername)
for_dataset = np.random.permutation(files)[:100]


# In[19]:



def copy_n_random(folder_name, n):
    
    files = os.listdir("./" + foldername)
    assert len(files) >= n, "Not enough input data"
    for_dataset = np.random.permutation(files)[:n]
    
    for file in for_dataset:
        
        src = "./" + foldername + "/" + file
        dst = "./master_image_folder"
        shutil.copy(src,dst)
    
copy_n_random(foldername, 100)


# In[ ]:




