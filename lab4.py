#!/bin/python3.8
from crypto import nod,evkl
import math
#Проверка простого числа
def TestFerma(p)->bool:
    for i in range(2,p):
        if pow(i,(p-1),p)!=1:
            return False
    return True
#Генерация ключей
def RSA_keys(q,p):
    if ((not TestFerma(q)) or (not TestFerma(p))):
        return "Введите простые числа"
    n=q*p
    f=(q-1)*(p-1)
    e=0
    for i in range(f//2,f-1):
        if nod(i,f)==1:
            e=i
    d=evkl(e,f)[0]
    return [(e,n),(d,n)]
#Зашифровка
def RSA_encrypt(str,open_key):
    result=""
    res=list(map(lambda x:  bin(pow(ord(x),open_key[0],open_key[1])),str))
    print(res)
    for i in res:
        result+=i
    return result
#Расшифровка
def RSA_decrypt(str,close_key):
    r=""
    str_blocks=[]
    str=str+"0b"
    for i in str:
        f=0
        r+=i
        if len(r)>3 and r[-2:]=="0b" and f==0:
            str_blocks.append(r[:-2])   
            r=""
            f=1
        elif len(r)>3 and r[-2:]=="0b" and f==1:
            str_blocks.append(f"0b{r[:-2]}")
            r=""
    print(str_blocks)
    res=list(map(lambda x:  chr(pow(int(x,2),close_key[0],close_key[1])),str_blocks))
    result=""
    for i in res:
        result+=i
    return result
key=RSA_keys(29,157)
a=RSA_encrypt("hello this is my message",key[0])
print(a)
print(RSA_decrypt(a,key[1]))