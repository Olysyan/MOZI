#!/bin/python3.8
from crypto import nod,evkl,Pollard
#Проверка простого числа
def TestFerma(p)->bool:
    for i in range(2,p):
        if pow(i,(p-1),p)!=1:
            return False
    return True
#Генерация ключей
def RSA_keys(q,p):
    """ if ((not TestFerma(q)) or (not TestFerma(p))):
        return "Введите простые числа" """
    n=q*p
    f=(q-1)*(p-1)
    e=0
    for i in range(f//3,f-1):
        if nod(i,f)==1:
            e=i
            break
    d=evkl(e,f)[0]
    return [(e,n),(d,n)]
#Зашифровка
def RSA_encrypt(str,open_key):
    result=""
    res=list(map(lambda x:  bin(pow(ord(x),open_key[0],open_key[1])),str))
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
#криптоанализ
def CA(str,open_key):
    mass=Pollard(open_key[1])
    mass.remove(1)
    f=(int(mass[0])-1)*(int(mass[1])-1)
    close_key=[evkl(open_key[0],f)[0],open_key[1]]
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
    print(result)
    return result
key=RSA_keys(3571,1571)
print(f"open_key{key[0]} close_key{key[1]}")
a=RSA_encrypt("hello this is my message",key[0])
print(a)
print(RSA_decrypt(a,key[1]))
CA(a,key[0])