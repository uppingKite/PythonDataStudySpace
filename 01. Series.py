#!/usr/bin/env python
# coding: utf-8

# # Pandas
# 
# 파이썬에서 사용하는 데이터 분석 라이브러리
# 

# In[1]:


import pandas as pd


# # 1. Series
# 1차원 데이터 (정수, 실수, 문자열 등)

# ## Series 객체 생성
# 예) 1월부터 4월까지 평균 온도 데이터 (-20, -10, 10, 20)

# In[3]:


temp = pd.Series([-20,-10,10,20])
temp


# In[4]:


temp[0] # index 0 에 해당하는 데이터 출력


# In[5]:


temp[2] # index 2 에 해당하는 데이터 출력


# ## Series 객체 생성 (Index 지정)

# In[8]:


temp = pd.Series([-20,-10,10,20], index=['Jan','Feb','Mar','Apr'])
temp


# In[9]:


temp['Jan'] # index Jan 에 해당하는 데이터 출력


# In[10]:


temp['Apr'] # index Apr 에 해당하는 데이터 출력


# In[12]:


# temp['Jun'] # 존재하는 인덱스 불러올 시 에러


# In[ ]:




