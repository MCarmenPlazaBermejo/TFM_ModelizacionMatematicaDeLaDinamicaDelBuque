#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import*
import numpy as np
import math
from math import pi


# In[2]:


cl1=0.1
i=1
x=0.02


# In[3]:


##zona curvatura

cl1=0.1
i=1
for x in np.arange(0.004,0.02,0.004):
    theta=10
    while theta <=360:
        y=5*0.15*math.cos(theta*pi/180)*(0.2969*sqrt(x)-0.1260*x-0.3516*x**2+0.2843*x**3-0.1015*x**4)
        z=5*0.15*math.sin(theta*pi/180)*(0.2969*sqrt(x)-0.1260*x-0.3516*x**2+0.2843*x**3-0.1015*x**4)
        print("Point(",i,")={",x,",",y,",",z,",",cl1,"};")
        theta=theta+10
        i=i+1


# In[4]:


##zona central

cl1=0.1
i=145
for x in np.arange(0.02,1,0.02):
    theta=10
    while theta <=360:
        y=5*0.15*math.cos(theta*pi/180)*(0.2969*sqrt(x)-0.1260*x-0.3516*x**2+0.2843*x**3-0.1015*x**4)
        z=5*0.15*math.sin(theta*pi/180)*(0.2969*sqrt(x)-0.1260*x-0.3516*x**2+0.2843*x**3-0.1015*x**4)
        print("Point(",i,")={",x,",",y,",",z,",",cl1,"};")
        theta=theta+10
        i=i+1


# In[5]:


##zona punta

cl1=0.1
i=1909
for x in np.arange(0.984,0.996,0.004):
    theta=10
    while theta <=360:
        y=5*0.15*math.cos(theta*pi/180)*(0.2969*sqrt(x)-0.1260*x-0.3516*x**2+0.2843*x**3-0.1015*x**4)
        z=5*0.15*math.sin(theta*pi/180)*(0.2969*sqrt(x)-0.1260*x-0.3516*x**2+0.2843*x**3-0.1015*x**4)
        print("Point(",i,")={",x,",",y,",",z,",",cl1,"};")
        theta=theta+10
        i=i+1


# In[6]:


print("Point(2053)={1,0,0,0.1};")
print("Point(2054)={0,0,0,0.1};")


# In[7]:


##Circunferencias (TODAS)

for t in np.arange(1,2052,1):
    k=t-35
    h=t+1
    x = range(60)
    a = t/36
    if a in x:
        print("Line(",t,")={",t,",",k,"};")
    else:
        print("Line(",t,")={",t,",",h,"};")


# In[8]:


##Rectas (unión curvatura-circunferencia 1)

z=1
e=2054
t=2052
while z <=36:
    print("Line(",t,")={",e,",",z,"};")
    z=z+1
    t=t+1


# In[9]:


##Rectas (Unión circunferencias unas con otras)

z=37
e=1
t=2088
while z <=2052:
    print("Line(",t,")={",e,",",z,"};")
    z=z+1
    e=e+1
    t=t+1


# In[10]:


##Rectas (última circunferencia-punta)

z=2053
e=2017
t=4104
while e <=2052:
    print("Line(",t,")={",e,",",z,"};")
    e=e+1
    t=t+1


# In[11]:


##superficies curvatura

i=1
b=2052
d=2053
while i<=36:
    x = range(100)
    a = i/36
    if a in x:
        print("Curve Loop(",i,")={",b,",",i,",",-(b-35),"}; Plane Surface(",i,")={",i,"};")
    else:
        print("Curve Loop(",i,")={",b,",",i,",",-d,"}; Plane Surface(",i,")={",i,"};")
    b=b+1
    i=i+1
    d=d+1


# In[12]:


##Superficies parte central

i=37
b=2089
c=37
d=2088
e=1
while i<=2051:
    x = range(200)
    a = i/36
    if a in x:
        print("Curve Loop(",i,")={",e,",",d-35,",",-c,",",-d,"}; Plane Surface(",i,")={",i,"};")
    else:
        print("Curve Loop(",i,")={",e,",",b,",",-c,",",-(b-1),"}; Plane Surface(",i,")={",i,"};")
    b=b+1
    c=c+1
    i=i+1
    d=d+1
    e=e+1


# In[13]:


##superficies punta

i=2052
e=4105
b=2017
while i<=2087:
    x = range(100)
    a = e/36
    if a in x:
        print("Curve Loop(",i,")={",b,",",e,",",-(b-35),"}; Plane Surface(",i,")={",i,"};")
    else:
        print("Curve Loop(",i,")={",b,",",e,",",-(e-1),"}; Plane Surface(",i,")={",i,"};")
    b=b+1
    i=i+1
    e=e+1


# In[ ]:




