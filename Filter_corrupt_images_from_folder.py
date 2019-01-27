

from os import listdir
from PIL import Image
import os

# In[12]:

def delete_corrupt_images():
    for filename in listdir('./'):
        if filename.endswith(".jpg"):
            try:
                fn = "./" + filename
                img = Image.open(fn)
                img.verify()
            except (IOError, SyntaxError) as e:
                os.remove(fn)

# os.walk does (dirpath, dirnames, filenames)
l = next(os.walk('.'))[1]
#print("l=", l)
path = os.getcwd()
for i in l:
    os.chdir(os.path.join(path , i ))
    print(os.getcwd())
    #next(os.walk('.'))[2]
    delete_corrupt_images()
    os.chdir("..")
