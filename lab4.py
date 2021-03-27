#!/bin/python3.8
from crypto import nod,evkl,Pollard
from  Crypto.Util import number
import math
#Проверка простого числа
def TestFerma(p)->bool:
    for i in range(2,p):
        if pow(i,(p-1),p)!=1:
            return False
    return True
#Генерация ключей
def RSA_keys(q,p,e: int=None):
    """ if ((not TestFerma(q)) or (not TestFerma(p))):
        return "Введите простые числа" """
    n=q*p
    f=(q-1)*(p-1)
    print(f)
    if e is None:
        for i in range(3,f//3):
            if nod(i,f)==1:
                e=i
                break 
    d=pow(int(e),-1,f)
    return [(e,n),(d,n)]
#Зашифровка
def RSA_encrypt(str,open_key):
    num=256
    f=math.floor(math.log(open_key[1],num))
    #print(f"log{open_key[1]} {num} = {f}")
    numblocks = math.ceil(len(str)/f)
    blocks = [0]*numblocks
    for j in range(numblocks):
        for i in range(f):
            if j*f+i < len(str):
                blocks[j] += str[j*f+i]*(num**i)
                #print(f"asd{blocks[j] }_{str[j*f+i]}_{i}_{j}")
    #print(blocks)
    new=list(map(lambda i: pow(i,open_key[0],open_key[1]), blocks))
    #print(new)
    mass = []
    for b in new:
        for i in range(f+1):
            mass.append(b % num)
            b //= num
    #print(mass)
    return bytes(mass)
#Расшифровка
def RSA_decrypt(str,close_key):
    num=256
    f=math.ceil(math.log(close_key[1],num))
    numblocks = math.ceil(len(str)/f)
    #print(f,numblocks)
    blocks = [0]*numblocks
    for j in range(numblocks):
        for i in range(f):
            if j*f+i < len(str):
                blocks[j] += str[j*f+i]*(num**i)
    new=list(map(lambda x: pow(x,close_key[0],close_key[1]), blocks))
    mass = []
    for b in new:
        for i in range(math.floor(math.log(close_key[1],num))):
            mass.append(b % num)
            b //= num
    return bytes(mass)
 
#криптоанализ
def CA(str,open_key):
    #mass=Pollard(open_key[1])
    mass=Lenstr(open_key[1])
    mass.remove(1)
    f=(int(mass[0])-1)*(int(mass[1])-1)
    close_key=[pow(open_key[0],-1,f),open_key[1]]
    return RSA_decrypt(str,close_key)
    
if __name__=="__main__":
    str=input("Введите строку для шифрования: ").encode('utf-8')
    a,b=number.getPrime(256),number.getPrime(256)
    print(a,b)
    key=RSA_keys(a,b)
    print(f"open key ={key[0]}\nclose key={key[1]}")
    enc=RSA_encrypt(str,key[0])
    dec=RSA_decrypt(enc,key[1])
    print(f"{enc=}\n{dec[:len(str)]}")
    print(f"Cryptanalysis result: {CA(enc,key[0])[:len(str)]}")
    """ num=1488
    print(key)
    enc=pow(num,key[0][0],key[0][1])
    dec=pow(enc,key[1][0],key[1][1])
    print(f'{num=}\n{enc=}\n{dec=}') """