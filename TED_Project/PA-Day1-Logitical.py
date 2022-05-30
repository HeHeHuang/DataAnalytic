#!/usr/bin/env python
# coding: utf-8

# ## PA Day1

# ### simple Linear Regression

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Multiple Linear Regression

# In[ ]:





# In[ ]:





# In[ ]:





# ### Logistic Regression for Binary classification

# ##### How to create the Logistic modle

# In[ ]:





# 如果要对**离散变量**进行预测，则要使用**分类模型**。分类模型与回归模型的区别在于其预测的变量不是连续的，而是离散的一些类别，例如，最常见的二分类模型可以预测一个人是否会违约、客户是否会流失.
# 本质上是个分类问题

# In[3]:


#Sigmoid函数 -》转换成 （0，1）
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-6,6)
#print(x)
y = 1.0/(1.0+np.exp(-x))
plt.plot(x,y)
plt.show()


#  逻辑回归模型本质就是将线性回归模型通过Sigmoid函数进行了一个非线性转换，得到一个介于0～1之间的概率值
#    数学公式推导？ 

# 了解了逻辑回归模型的基本原理后，在实际模型搭建中，就是要找到合适的系数ki和截距项k0，使预测的概率较为准确，在数学中使用极大似然估计法来确定合适的系数ki和截距项k0，从而得到相应的概率。

# In[9]:


#逻辑回归模型
#X1 = income， X2=历史违约次数 目标变量Y： 判断客户是否违约
X = [[1,0],[5,1],[6,4],[4,2],[3,2]]#此处为什么用这个list数据结构
Y= [0,1,1,0,0]

from sklearn.linear_model import LogisticRegression
model =LogisticRegression()
model.fit(X,Y)


# In[10]:


model.predict([[2,2]])


# In[11]:


model.predict([[2,0],[5,1],[4,2]])


# 逻辑回归模型的本质是预测概率，而不是直接预测具体类别（如属于0还是1

# In[18]:


y_pred_proba= model.predict_proba(X)
import pandas as pd
a = pd.DataFrame(y_pred_proba,columns=['0proba','1proba'])
print(a)


# In[19]:


print(model.coef_)  #k1, k2


# In[20]:


print(model.intercept_)  k0


# 用逻辑回归模型处理多分类问题

# ? 那么在二分类中， 怎么确定 大于0.5就归为哪一类，  都会用0.5么

# In[27]:


xel = [[1,0],[5,1],[6,4],[4,2],[3,2]]
yel = [1,0,-1,1,1] # three type of y variable
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(xel,yel)


# In[28]:


print(model.predict([[0,0]]))


# In[29]:


y_pred_proba = model.predict_proba([[0,0]])
y_pred_proba #? 这个colmun name 的排序是按照 y variable‘s ordering? 


# 每一笔交易的手续费汇总起来，数量便相当可观。这部分收入对于一些证券公司来说很重要，甚至可以占到营业总收入的50%以上，因此，证券公司对于客户（即交易者）的忠诚度和活跃度是很看重的
# y variable is 客户流失 or 不流失 

# In[30]:


import pandas as pd
df= pd.read_excel('E:\Desktop\DataSource\股票客户流失.xlsx')
df.head()


# In[31]:


xVar =df.drop(columns='是否流失')
yVar = df['是否流失'] #0表示未流失，1表示流失


# ####  1. split data to do train and test 

# ? 这个split size 有什么说法么？ 
#   - 大量数据 9：1
#   - 一般量 8：2

# In[32]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(xVar,yVar,test_size=0.2)
#random_state 每次划分的数据是一样的


# In[33]:


X_train.head()


# In[34]:


y_train.head()


# #### 2. create  logistic Regression model

# In[35]:


from sklearn.linear_model import LogisticRegression
Dmodel = LogisticRegression()
Dmodel.fit(X_train,y_train)


# #### 3. use model to predict outcome

# In[38]:


y_pred = Dmodel.predict(X_test)
type(y_pred)
y_pred[0:100]


# In[42]:


df_Diff =pd.DataFrame()
df_Diff['Prediction']= list(y_pred)
df_Diff['Actual']=list(y_test)
df_Diff.head(10)


# #####  test accuracy 

# In[48]:


#model score function to cal
Dmodel.score(X_test,y_test)


# In[50]:


#from sklearn
from sklearn.metrics import accuracy_score
score= accuracy_score(y_pred,y_test)
score


# #### 4. using model to cal the predict probability 

# In[ ]:


#### 5. evaluate the model: ROC 


# In[ ]:





# #### 5. evaluate the model: ROC 

# In[ ]:





# #### 6. evaluate the model: KS

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ##### How to evaluate the Logistic modle

# - confusion Matrix

# np.exp(-x)疑问？
# 

# In[ ]:





# 客户流失预警模型
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




