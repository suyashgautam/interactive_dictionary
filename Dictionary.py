
# coding: utf-8

# In[31]:


import json
from difflib import *
data = json.load(open("data.json","r+"))


# In[43]:


def mean(w):
    w=w.lower()
    if w in data:
        return(data[w])
    elif len(get_close_matches(a,data.keys(),3,0.8))>0:
        yn=input("Did you mean %s instead?\nEnter Y for yes and N for no "%get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "The word doesnt exist. Please double check it."
        else:
            return "We didnt understand your query."
    else:
        return "Word not found\n";
            


# In[46]:


a=str(input("Enter a word "))
out = mean(a)
if type(out) == list:
    for i in out:
        print(i)

