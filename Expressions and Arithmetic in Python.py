#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Expressions

num1=int(input("Enter a number:"))
num2=int(input("Enter another number:"))
sum=num1+num2
print(num1, '+',num2,'=',sum)


# In[2]:


x=10                           #Arithmetic
y=5
print(x+y)                 #added if x and y are numbers and concatinated if they are strings
print(x-y)                 #subtraction
print(x*y)                 #Product
print(x/y)                 #division
print(x//y)                #Floor of x divided by y
print(x%y)                 #Remainder of x divided by y
print(x**y)                #x raised to the power y


# In[5]:


#precedence and associativity
#Multiplication and division is done before addition and subtraction
print(2+3*6)
print(2-5-4)           #left associative (binary operators)
print(-3+4)            #unary operators are right associative
print(-(67+5))


# In[6]:


x=2
y=6
print(3*(x+7)+9/(y-3))


# In[ ]:




