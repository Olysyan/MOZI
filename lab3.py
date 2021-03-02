#!/bin/python3.8
#Шифр Виженера
from collections import Counter
def Vig(str,key,alf):
    dict_key=list(key)
    dict_alf = list(alf)
    dict_str=list(str)
    ll=len(dict_key)
    p=len(dict_alf)
    result=""
    j=0
    for i in dict_str:
        #print(f"{dict_alf.index(i)}+{dict_alf.index(dict_key[j%ll])} = {(dict_alf.index(i)+dict_alf.index(dict_key[j%ll]))%p} (mod {p}) = {dict_alf[(dict_alf.index(i)+dict_alf.index(dict_key[j%ll]))%p]}")
        result += dict_alf[(dict_alf.index(i)+dict_alf.index(dict_key[j%ll]))%p]
        j+=1
    print(f"шифовка с ключем {key}: {result}")
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
    print(f"расшифовка с ключем {key}: {result}")
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
    print(f"расшифовка с начальным ключем {key}: {result}")
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
    print(f"расшифовка с начальным ключем {key}: {result}")
    return result
#индекс встречаемости символов
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
def CA(str):
    num=max([[i,index(str[::i])] for i in range(1, len(str)//3)],key=lambda a: a[1])[0]
    n=N(num)
    print(f"Предполагаемые длины блоков: {n}")
    count=[]
    res={}
    for i in n:
        count.append([str[j::i] for j in range(i)])
    result=[]
    r=[]
    for i in count:
        for k in i:
            alf=set(k)
            c=0
            for l in alf:
                for j in k:
                    if j==l:
                        c+=1
                res[l]=c
                c=0
            result.append(res)
        r.append(result)
        result=[]
    print(f"подсчет частот встречаемости для выбранных разбиений: {r}")
    return r
#проверка
def mapping(str,key,ca,str_1,alf1):
    res={}
    result=[]
    count=[]
    end={}
    ss=""
    count.append([str[j::key] for j in range(key)])
    for i in count:
        for k in i:
            alf=set(k)
            c=0
            for l in alf:
                for j in k:
                    if j==l:
                        c+=1
                res[l]=c
                c=0
            result.append(res)
    try:
        for lm in range(len(ca)):
            for i in result:
                for f,p in i.items():
                    for mn in ca[lm]:
                        for t,y in mn.items():
                            if y==p:
                                end[f]=t
        for i in str_1:
            for f,p in end.items():
                if i ==p:
                    ss+=f
        r=""
        rr=[]
        kk=1
        dict_alf1=list(alf1)
        po=len(dict_alf1)
        print(ss,"\n",str_1)
        ty=0
        for ko in str_1:
            try:
                r+= dict_alf1[(dict_alf1.index(str_1[ty])-dict_alf1.index(ss[ty]))%po]
                ty+=1
                if kk==key:
                    rr.append(r)
                    r=""
                    kk=0
                kk+=1
            except:
                e=0
    except:
        e=0
    return rr
str="шифр    шифромзашифрован"
print(f"текст для зашифровки: {str}")
#str="зашифровал"
key ="шифр"
k="р"
alf=" ё.,!йцукенгшщзхъфывапролджэячстмиьбю"
print(f"используемый алфавит {alf} \nмощность алфавита: {len(alf)}")
e = Vig(str,key,alf)
""" DVig(e,key,alf) 
r=OVig(str,k,alf)
DOVig(r,k,alf)
m=СVig(str,k,alf)
DCVig(m,k,alf)  """
c=CA(e)
print("сопоставление")
h = mapping(str,len(key),c,e,alf)
print(f"возможные ключи: {h}")
for i in h:
    print("\n")
    print(f"расшифровка для ключа {i}: ")
    DVig(e,i,alf)
