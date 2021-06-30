#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle


# In[ ]:


favorite_load = pickle.load(open('./saves/favorite_save.pkl','rb'))
print(favorite_load)


# In[ ]:


type(favorite_load)


# In[ ]:


print(favorite_load['tiger'])


# 교육까지 끝난 상태에서 피클로 저장

# In[3]:


autompg_lr = pickle.load(open('./saves/autompg_lr.pkl','rb'))
print(autompg_lr)


# In[4]:


type(autompg_lr)


# In[5]:

# input from outside
a = 3504.0
b = 8
import numpy as np
pre = np.array([[a,b]])
print(autompg_lr.predict([[pre]]))
# 위 5줄과 동일
print(autompg_lr.predict([[3504.0,8]]))


# In[ ]:




