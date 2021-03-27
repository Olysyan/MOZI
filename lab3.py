#!/bin/python3.8
#Шифр Виженера
import numpy as np
from collections import Counter
import math
def Vig(str,key,alf):
    dict_key=list(key)
    dict_alf = list(alf)
    dict_str=list(str)
    ll=len(dict_key)
    p=len(dict_alf)
    result=""
    j=0
    op={}
    for i in dict_str:
        #print(f"{dict_alf.index(i)}+{dict_alf.index(dict_key[j%ll])} = {(dict_alf.index(i)+dict_alf.index(dict_key[j%ll]))%p} (mod {p}) = {dict_alf[(dict_alf.index(i)+dict_alf.index(dict_key[j%ll]))%p]}")
        op[i]=dict_alf[(dict_alf.index(i)+dict_alf.index(dict_key[j%ll]))%p]
        result += dict_alf[(dict_alf.index(i)+dict_alf.index(dict_key[j%ll]))%p]
        j+=1
    #print(f"шифовка с ключем {key}: {result}")
    return result
#Расшифровка шифра Виженера
def DVig(str,key,alf):
    dict_key=list(key)
    dict_alf = list(alf)
    dict_str=list(str)
    ll=len(dict_key)
    p=len(dict_alf)
    result=""
    j=0
    for i in dict_str:
        #print(f"{dict_alf.index(i)}-{dict_alf.index(dict_key[j%ll])} = {(dict_alf.index(i)-dict_alf.index(dict_key[j%ll]))%p} (mod {p}) = {dict_alf[(dict_alf.index(i)-dict_alf.index(dict_key[j%ll]))%p]}")
        result += dict_alf[(dict_alf.index(i)-dict_alf.index(dict_key[j%ll]))%p]
        j+=1
    #print(f"расшифовка с ключем {key}: {result}")
    return result
#Шифр Виженера по открытому тексту
def OVig(str,key,alf):
    if len(key)!=1:
        print("Введите корректный ключ")
        return 0
    dict_alf = list(alf)
    dict_str=list(str)
    dict_key=[key]
    for i in dict_str[:-1]:
        dict_key.append(i)
    ll=len(dict_key)
    p=len(dict_alf)
    result=""
    j=0
    for i in dict_str:
        #print(f"{dict_alf.index(i)} +{dict_alf.index(dict_key[j%ll])} = {(dict_alf.index(i)+dict_alf.index(dict_key[j%ll]))%p} (mod {p})= {dict_alf[(dict_alf.index(i)+dict_alf.index(dict_key[j%ll]))%p]}")
        result += dict_alf[(dict_alf.index(i)+dict_alf.index(dict_key[j%ll]))%p]
        j+=1
    print(f"шифовка с начальным ключем {key}: {result}")
    return result
#Расшифровка шифра Виженера по открытому тексту
def DOVig(str,key,alf):
    dict_alf = list(alf)
    dict_str=list(str)
    dict_key=[key]
    p=len(dict_alf)
    result=""
    j=0
    for i in dict_str:
        if j ==0:
            result += dict_alf[(dict_alf.index(i)-dict_alf.index(dict_key[j]))%p]
            #print(f"{dict_alf.index(i)} - {dict_alf.index(dict_key[j])} = {(dict_alf.index(i)-dict_alf.index(dict_key[j]))%p} (mod {p})= {dict_alf[(dict_alf.index(i)-dict_alf.index(dict_key[j]))%p]}")
        else:
            #print(f"{dict_alf.index(i)} - {dict_alf.index(result[j-1:j])} = {(dict_alf.index(i)-dict_alf.index(result[j-1:j]))%p} (mod {p})= {dict_alf[(dict_alf.index(i)-dict_alf.index(result[j-1:j]))%p]}")
            result += dict_alf[(dict_alf.index(i)-dict_alf.index(result[j-1:j]))%p]
        j+=1
    #print(f"расшифовка с начальным ключем {key}: {result}")
    return result
#Шифр Виженера по шифротексту
def СVig(str,key,alf):
    if len(key)!=1:
        print("Введите корректный ключ")
        return 0
    dict_alf = list(alf)
    dict_str=list(str)
    dict_key=[key]
    p=len(dict_alf)
    result=""
    j=0
    dd=key
    for i in dict_str:
        #print(f"{dict_alf.index(i)} + {dict_alf.index(dict_key[j])} = {(dict_alf.index(i)+dict_alf.index(dict_key[j]))%p} (mod{p}) = {dict_alf[(dict_alf.index(i)+dict_alf.index(dict_key[j]))%p]}")
        o=dict_alf[(dict_alf.index(i)+dict_alf.index(dict_key[j]))%p]
        result += o
        dict_key.append(o)
        dd+=o
        j+=1
    #print(dd)
    print(f"шифовка с начальным ключем {key}: {result}")
    return result
#расшифровка шифра Виженера по шифротексту
def DCVig(str,key,alf):
    dict_alf = list(alf)
    dict_str= list(str)
    p=len(dict_alf)
    result=""
    j=0
    for i in dict_str:
        if j==0:
            o=dict_alf[(dict_alf.index(i)-dict_alf.index(key))%p]
            #print(f"{dict_alf.index(i)} - {dict_alf.index(key)} = {(dict_alf.index(i)-dict_alf.index(key))%p} (mod {p}) = {dict_alf[(dict_alf.index(i)-dict_alf.index(key))%p]}")
        else:
            o=dict_alf[(dict_alf.index(i)-dict_alf.index(dict_str[j-1]))%p]
            #print(f"{dict_alf.index(i)} - {dict_alf.index(dict_str[j-1])} = {(dict_alf.index(i)-dict_alf.index(dict_str[j-1]))%p} (mod {p}) = {dict_alf[(dict_alf.index(i)-dict_alf.index(dict_str[j-1]))%p]}")
        result+=o
        j+=1
    #print(f"расшифовка с начальным ключем {key}: {result}")
    return result
#индекс совпадения
def index(str):
    count = Counter(list(str))
    return sum(i*(i-1) for i in count.values())/(len(str)*(len(str) - 1))
#раскладывает число на множители
def N(num):
    n=[]
    for i in range(2,num//2+1):
        if (num/i)%1==0:
            n.append(i)
    n.append(num)
    return n

#частотный криптоанализ
def CA(str,auf):
    num=sorted([[i,index(str[::i])] for i in range(1, 10)],key=lambda a: a[1])[-2:]

    r=0
    if (num[0][1]-num[1][1])>0.009:
        nu=num[0][0]
        r=0.2
    elif (-num[0][1]+num[1][1])>0.009:
        nu=num[1][0]
        r=0.2
    else:
        nu=math.gcd(num[0][0],num[1][0])
    if nu == 1:
        nu=num[0][0]
        r=1
    n=[nu]
    return nu
def counter(text,alf):
    d={}
    k=0
    f=len(text)
    for i in alf:
        for j in text:
            if i==j:
                k+=1
                d[i]=k/f
        k=0
    return d
def CA2(str,text,key_size,alf):
    m=[]
    for i in range(key_size):
        m.append(counter(str[i::key_size],alf))
    rm=counter(text,alf)
    op=[]
    res=[]
    for i in m:
        new={}
        for j,h in i.items():
            for t,l in rm.items():
                aa=abs(l-h)
                if op ==[]:
                    op.append(aa)
                if op[0]>aa:
                    op[0]=aa
                    new[j]=t
            op=[]
        res.append(new)
    result=""
    for i in res:
        tt=[]
        for t,y in i.items():
            tt.append((alf.index(t)-alf.index(y))%(len(alf)))
        result+=alf[max(set(tt), key = tt.count)]
    return result
    
str=open('text.txt').read().lower().replace('\n','')
auf=open('text2.txt').read().lower().replace('\n','')
key ="zfrrt"
k="р"
alf="qwertyuiopasdfghjklzxcvbnm .,"
print(f"ключ для шифрования: {key}")
print(f"используемый алфавит {alf} \nмощность алфавита: {len(alf)}")
e = Vig(str,key,alf)
""" DVig(e,key,alf) 
r=OVig(str,k,alf)
DOVig(r,k,alf)
m=СVig(str,k,alf)
DCVig(m,k,alf)  """
c=CA(e,auf)
print(f"результат криптоанализа: {CA2(e,auf,c,alf)}")