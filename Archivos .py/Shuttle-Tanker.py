#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
import openpyxl
import pandas as pd
from math import pi
from openpyxl import Workbook, load_workbook


# In[3]:


i=162;
while i <=188:
    x=33.375;
    print("Point(",i,")={",x,",y,z,cl1};")
    i=i+1


# In[4]:


df = pd.read_csv('shuttle9.csv', sep=';')
df


# In[5]:


##Station 1
st1=df["st1"]
st1s=df["st1s"]

i=1;  
a=0;
b=0;
while i <=13:
    x=-3.499;
    print("Point(",i,")={",x,",",st1[a],",",st1s[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[6]:


##Station 2
st2=df["st2"]
st2s=df["st2s"]

i=14;  
a=0;
b=0;
while i <=26:
    x=0;
    print("Point(",i,")={",x,",",st2[a],",",st2s[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[7]:


##Station 3
st3=df["st3"]
st3s=df["st3s"]

i=27;  
a=0;
b=0;
while i <=46:
    x=6.675;
    print("Point(",i,")={",x,",",st3[a],",",st3s[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[8]:


##Station 4
st4=df["st4"]
st4s=df["st4s"]

i=47;  
a=0;
b=0;
while i <=74:
    x=9.075;
    print("Point(",i,")={",x,",",st4[a],",",st4s[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[9]:


##Station 5
st5=df["st5"]
st5s=df["st5s"]

i=75;  
a=0;
b=0;
while i <=102:
    x=13.350;
    print("Point(",i,")={",x,",",st5[a],",",st5s[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[10]:


##Station 6
st6=df["st6"]
st6s=df["st6s"]

i=103;  
a=0;
b=0;
while i <=131:
    x=20.025;
    print("Point(",i,")={",x,",",st6[a],",",st6s[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[11]:


##Station 7
st7=df["st7"]
st7s=df["st7s"]

i=132;  
a=0;
b=0;
while i <=161:
    x=26.700;
    print("Point(",i,")={",x,",",st7[a],",",st7s[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[12]:


##Station 8
st8=df["st8"]
st8s=df["st8s"]

i=162;  
a=0;
b=0;
while i <=187:
    x=33.375;
    print("Point(",i,")={",x,",",st8[a],",",st8s[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[13]:


##Station 9
st9=df["st9"]
st91=df["st91"]

i=188;  
a=0;
b=0;
while i <=208:
    x=40.050;
    print("Point(",i,")={",x,",",st9[a],",",st91[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[14]:


##Station 10
st10=df["st10"]
st101=df["st101"]

i=209;
a=0;
b=0;
while i <=223:
    x=53.400;
    print("Point(",i,")={",x,",",st10[a],",",st101[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[15]:


##Station 11
st11=df["st11"]
st111=df["st111"]

i=224;
a=0;
b=0;
while i <=234:
    x=66.750;
    print("Point(",i,")={",x,",",st11[a],",",st111[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[16]:


##Station 12
st12=df["st12"]
st121=df["st121"]

i=235;
a=0;
b=0;
while i <=243:
    x=80.100;
    print("Point(",i,")={",x,",",st12[a],",",st121[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[17]:


##Station 13
st13=df["st13"]
st131=df["st131"]

i=244;
a=0;
b=0;
while i <=252:
    x=93.450;
    print("Point(",i,")={",x,",",st13[a],",",st131[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[18]:


##Station 14
st14=df["st14"]
st141=df["st141"]

i=253;
a=0;
b=0;
while i <=261:
    x=106.800;
    print("Point(",i,")={",x,",",st14[a],",",st141[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[19]:


##Station 15
st15=df["st15"]
st151=df["st151"]

i=262;
a=0;
b=0;
while i <=270:
    x=120.150;
    print("Point(",i,")={",x,",",st15[a],",",st151[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[20]:


##Station 16
st16=df["st16"]
st161=df["st161"]

i=271;
a=0;
b=0;
while i <=279:
    x=133.500;
    print("Point(",i,")={",x,",",st16[a],",",st161[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[21]:


##Station 17
st17=df["st17"]
st171=df["st171"]

i=280;
a=0;
b=0;
while i <=288:
    x=146.850;
    print("Point(",i,")={",x,",",st17[a],",",st171[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[22]:


##Station 18
st18=df["st18"]
st181=df["st181"]

i=289;
a=0;
b=0;
while i <=297:
    x=160.200;
    print("Point(",i,")={",x,",",st18[a],",",st181[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[23]:


##Station 19
st19=df["st19"]
st191=df["st191"]

i=298;
a=0;
b=0;
while i <=306:
    x=173.550;
    print("Point(",i,")={",x,",",st19[a],",",st191[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[24]:


##Station 20
st20=df["st20"]
st201=df["st201"]

i=307;
a=0;
b=0;
while i <=315:
    x=186.900;
    print("Point(",i,")={",x,",",st20[a],",",st201[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[25]:


##Station 21
st21=df["st21"]
st211=df["st211"]

i=316;
a=0;
b=0;
while i <=324:
    x=200.250;
    print("Point(",i,")={",x,",",st21[a],",",st211[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[26]:


##Station 22
st22=df["st22"]
st221=df["st221"]

i=325;
a=0;
b=0;
while i <=333:
    x=213.600;
    print("Point(",i,")={",x,",",st22[a],",",st221[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[27]:


##Station 23
st23=df["st23"]
st231=df["st231"]

i=334;
a=0;
b=0;
while i <=342:
    x=220.275;
    print("Point(",i,")={",x,",",st23[a],",",st231[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[28]:


##Station 24
st24=df["st24"]
st241=df["st241"]

i=343;
a=0;
b=0;
while i <=351:
    x=226.950;
    print("Point(",i,")={",x,",",st24[a],",",st241[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[29]:


##Station 25
st25=df["st25"]
st251=df["st251"]

i=352;
a=0;
b=0;
while i <=364:
    x=233.625;
    print("Point(",i,")={",x,",",st25[a],",",st251[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[30]:


##Station 26
st26=df["st26"]
st261=df["st261"]

i=365;
a=0;
b=0;
while i <=377:
    x=240.300;
    print("Point(",i,")={",x,",",st26[a],",",st261[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[31]:


##Station 27
st27=df["st27"]
st271=df["st271"]

i=378;
a=0;
b=0;
while i <=392:
    x=246.975;
    print("Point(",i,")={",x,",",st27[a],",",st271[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[32]:


##Station 28
st28=df["st28"]
st281=df["st281"]

i=393;
a=0;
b=0;
while i <=407:
    x=253.650;
    print("Point(",i,")={",x,",",st28[a],",",st281[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[33]:


##Station 29
st29=df["st29"]
st291=df["st291"]

i=408;
a=0;
b=0;
while i <=424:
    x=260.325;
    print("Point(",i,")={",x,",",st29[a],",",st291[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[34]:


##Station 30
st30=df["st30"]
st301=df["st301"]

i=425;
a=0;
b=0;
while i <=450:
    x=267.000;
    print("Point(",i,")={",x,",",st30[a],",",st301[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[35]:


##Station 31
st31=df["st31"]
st311=df["st311"]

i=451;
a=0;
b=0;
while i <=466:
    x=268.100;
    print("Point(",i,")={",x,",",st31[a],",",st311[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[36]:


##Station stc
stc=df["stc"]
stcc=df["stcc"]

i=467;
a=0;
b=0;
while i <=504:
    y=0;
    print("Point(",i,")={",stc[a],",",y,",",stcc[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[37]:


##SIMETRÍA

##Station 1
st1=df["st1"]
st1s=df["st1s"]

i=505;  
a=0;
b=0;
while i <=517:
    x=-3.499;
    print("Point(",i,")={",x,",",-st1[a],",",st1s[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1

##Station 2
st2=df["st2"]
st2s=df["st2s"]

i=14;  
a=0;
b=0;
while i <=26:
    x=0;
    print("Point(",i,")={",x,",",st2[a],",",-st2s[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1
    
##Station 3
st3=df["st3"]
st3s=df["st3s"]

i=27;  
a=0;
b=0;
while i <=46:
    x=6.675;
    print("Point(",i,")={",x,",",st3[a],",",-st3s[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1

##Station 4
st4=df["st4"]
st4s=df["st4s"]

i=47;  
a=0;
b=0;
while i <=74:
    x=9.075;
    print("Point(",i,")={",x,",",st4[a],",",-st4s[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1

##Station 5
st5=df["st5"]
st5s=df["st5s"]

i=75;  
a=0;
b=0;
while i <=102:
    x=13.350;
    print("Point(",i,")={",x,",",st5[a],",",-st5s[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1
    
##Station 6
st6=df["st6"]
st6s=df["st6s"]

i=103;  
a=0;
b=0;
while i <=131:
    x=20.025;
    print("Point(",i,")={",x,",",st6[a],",",-st6s[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1

##Station 7
st7=df["st7"]
st7s=df["st7s"]

i=132;  
a=0;
b=0;
while i <=161:
    x=26.700;
    print("Point(",i,")={",x,",",st7[a],",",-st7s[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1

##Station 8
st8=df["st8"]
st8s=df["st8s"]

i=162;  
a=0;
b=0;
while i <=187:
    x=33.375;
    print("Point(",i,")={",x,",",st8[a],",",-st8s[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1


# In[38]:


dc = pd.read_csv('columnas.csv', sep=';')
dc


# In[39]:


col1=dc["col1"]
col2=dc["col2"]
col3=dc["col3"]


# In[40]:


col1=dc["col1"]
col2=dc["col2"]
col3=dc["col3"]

i=505;
a=0;
b=0;
c=0;
while i <=930:
    if col2[b]==0:
        print ("//")
        i=i-1
    else:
        print("Point(",i,")={",col1[a],",",-col2[b],",",col3[c],",cl1};")
    a=a+1
    b=b+1
    c=c+1
    i=i+1


# In[41]:


##Líneas

##Station no. 1 - Station no. 15

t=1;
k=1;
h=13;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1
t=t;
print("Line(",t,")={1,505};")
t=t+1;
k=505;
h=516;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1


k=14;
h=26;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1    
t=t;
print("Line(",t,")={14,517};")
t=t+1;
k=517;
h=528;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1


k=27;
h=46;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
t=t;
print("Line(",t,")={27,529};")
t=t+1;
k=529;
h=544;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1


k=47;
h=74;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
t=t;
print("Line(",t,")={47,545};")
t=t+1;
k=545;
h=570;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1

    
k=75;
h=102;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
t=t;
print("Line(",t,")={75,571};")
t=t+1;
k=571;
h=597;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1

    
k=103;
h=131;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
t=t;
print("Line(",t,")={103,598};")
t=t+1;
k=598;
h=625;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1

    
k=132;
h=161;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
t=t;
print("Line(",t,")={132,626};")
t=t+1;
k=626;
h=654;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1

    
k=162;
h=187;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
t=t;
print("Line(",t,")={162,655};")
t=t+1;
k=654;
h=679;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1

   
k=188;
h=208;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
t=t;
print("Line(",t,")={188,679};")
t=t+1;
k=679;
h=699;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1

    
k=209;
h=223;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
t=t;
print("Line(",t,")={209,700};")
t=t+1;
k=700;
h=713;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1

    
k=224;
h=234;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
t=t;
print("Line(",t,")={224,714};")
t=t+1;
k=714;
h=723;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1

    
k=235;
h=243;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
t=t;
print("Line(",t,")={235,724};")
t=t+1;
k=724;
h=731;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1

    
k=244;
h=252;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
t=t;
print("Line(",t,")={244,732};")
t=t+1;
k=732;
h=739;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1

    
k=253;
h=261;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
t=t;
print("Line(",t,")={253,740};")
t=t+1;
k=740;
h=747;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1

    
k=262;
h=270;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
t=t;
print("Line(",t,")={262,748};")
t=t+1;
k=748;
h=755;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1

    


# In[42]:


##Station no. 16-31

k=271;
h=279;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
    
k=280;
h=288;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
    
k=289;
h=297;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
    
k=298;
h=306;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
    
k=307;
h=315;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
    
k=316;
h=324;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
    
k=325;
h=333;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
    
k=334;
h=342;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
    
k=343;
h=351;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
    
k=352;
h=364;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
    
k=365;
h=377;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
    
k=378;
h=392;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
    
k=393;
h=407;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
    
k=408;
h=424;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
    
k=425;
h=450;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
    
k=451;
h=466;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1 
    


# In[43]:


t=1;
k=1;
h=13;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1
t=t;
print("Line(",t,")={1,505};")
t=t+1;
k=505;
h=516;
while k+1!=h+1:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1


# In[44]:


lf = pd.read_csv('flotacion.csv', sep=';')
lf


# In[45]:


##Puntos Línea flotación (ST)

posx=lf["posx"]
posy=lf["posy"]
posz=lf["posz"]

i=931;  
a=0;
b=0;
c=0;
while i <=961:
    x=-3.499;
    print("Point(",i,")={",posx[a],",",posy[b],",",posz[c],",cl1};")
    a=a+1
    b=b+1
    c=c+1
    i=i+1


# In[46]:


##Puntos Línea flotación (P)

posx=lf["posx"]
posy=lf["posy"]
posz=lf["posz"]

i=962;  
a=0;
b=0;
c=0;
while i <=992:
    x=-3.499;
    print("Point(",i,")={",posx[a],",",-posy[b],",",posz[c],",cl1};")
    a=a+1
    b=b+1
    c=c+1
    i=i+1


# In[47]:


##Línea flotación (ST)

t=1;
k=931;
while t<=30:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1


# In[48]:


##Línea flotación (ST)

t=31;
k=962;
while t<=60:
    print("Line(",t,")={",k,",",k+1,"};")
    t=t+1
    k=k+1


# In[49]:


##Station 8
st8=df["st8"]
st8s=df["st8s"]

i=321;  
a=0;
b=0;
while a <= 25:
    x=33.375;
    print("Point(",i,")={",x,",",st8[a],",",st8s[b],",cl1};")
    a=a+1
    b=b+1
    i=i+1

col1=dc["col1"]
col2=dc["col2"]
col3=dc["col3"]

a=162;
b=162;
c=162;
while a<=187:
    if col2[b]==0:
        print ("//")
        i=i-1
    else:
        print("Point(",i,")={",col1[a],",",-col2[b],",",col3[c],",cl1};")
    a=a+1
    b=b+1
    c=c+1
    i=i+1


# In[ ]:





# In[ ]:





# In[ ]:




