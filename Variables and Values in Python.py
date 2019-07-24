#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Integer and string values

x=54                             #integer
y=78
z='xyz'                          #string
w='abc'
print("The result of addition of two integers is another integer. Here, x+y=",x+y)
print("When two strings are added, it gets concatinaned. Here, w+z=",w+z)

#When an integer and string is added, an error is obtained


# In[7]:


a=type(x)             #returns the datatype of x
b=type(w)
print(a)
print(b)


# In[8]:


a='5'+'80'               #when inserted in '', integers become string and they are concatinated 
print(a)


# In[12]:


a=23.34                                      #float
b=45.97
c=type(a)
print(a+b)
print(c)
print(round(a))                     #rounds off to the closest integer value
x=346732.8634795
print(round(x,2))                 #rounds floating-point expression n to the 10^-r decimal digit
print(round(x,-3))


# In[16]:


num1 = float(input("Enter number 1:"))
num2 = float(input("Enter number 2:"))
print("The sum of the two numbers is",num1+num2)


# In[19]:


#We use ('''xyz''' )triple quotes to write multi line strings

x= '''Hello dear friend
We're learning Python
Hope you are enjoying '''
print(x)

