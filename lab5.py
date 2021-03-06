#!/bin/python3.8
import random
#генерация ключей
def ELGAM_keys(p):
    g=(p-5)//2
    x=(p-17)//2
    h = pow(g,x,p)
    return [(h,p),(x,p)]
#зашифровка
def ELGAM_encrypt(str,open_key):
    result=""
    g=(open_key[1]-5)//2
    k=(open_key[1]-9)//2
    res=list(map(lambda x:  bin(ord(x)*pow(open_key[0],k,open_key[1])),str))
    c1=pow(g,k,open_key[1])
    for i in res:   
        result+=i
    return [result,c1]
#расшифровка
def ELGAM_decrypt(str,close_key):
    r=""
    str_blocks=[]
    str_1=str[0]+"0b"
    for i in str_1:
        f=0
        r+=i
        if len(r)>3 and r[-2:]=="0b" and f==0:
            str_blocks.append(r[:-2])   
            r=""
            f=1
        elif len(r)>3 and r[-2:]=="0b" and f==1:
            str_blocks.append(f"0b{r[:-2]}")
            r=""
    res=list(map(lambda x:  chr(int(x,2)//pow(str[1],close_key[0],close_key[1])),str_blocks))
    result=""
    for i in res:
        result+=i
    return result
#пример работы
key=ELGAM_keys(3571)
a=ELGAM_encrypt("hello this is my message!",key[0])
print(ELGAM_decrypt(a,key[1]))