#!/bin/python3.8
#Шифр Веженера
def Vez(str,key,alf):
    dict_key=[i for i in key]
    dict_alf = [i for i in alf]
    dict_str=[i for i in str]
    ll=len(dict_key)
    p=len(dict_alf)
    result=""
    j=0
    for i in dict_str:
        result += dict_alf[(dict_alf.index(i)+dict_alf.index(dict_key[j%ll]))%p]
        j+=1
    print(result)
    return result
#Расшифровка шифра Веженера
def DVez(str,key,alf):
    dict_key=[i for i in key]
    dict_alf = [i for i in alf]
    dict_str=[i for i in str]
    ll=len(dict_key)
    p=len(dict_alf)
    result=""
    j=0
    for i in dict_str:
        result += dict_alf[(dict_alf.index(i)-dict_alf.index(dict_key[j%ll]))%p]
        j+=1
    print(result)
    return result
#Шифр Веженера по открытому тексту
def OVez(str,key,alf):
    if len(key)!=1:
        print("Введите корректный ключ")
        return 0
    dict_alf = [i for i in alf]
    dict_str=[i for i in str]
    dict_key=[key]
    for i in dict_str[:-1]:
        dict_key.append(i)
    ll=len(dict_key)
    p=len(dict_alf)
    result=""
    j=0
    for i in dict_str:
        result += dict_alf[(dict_alf.index(i)+dict_alf.index(dict_key[j%ll]))%p]
        j+=1
    print(result)
    return result
#Расшифровка шифра Веженера по открытому тексту
def DOVez(str,key,alf):
    dict_alf = [i for i in alf]
    dict_str=[i for i in str]
    dict_key=[key]
    p=len(dict_alf)
    result=""
    j=0
    for i in dict_str:
        if j ==0:
            result += dict_alf[(dict_alf.index(i)-dict_alf.index(dict_key[j]))%p]
        else:
            result += dict_alf[(dict_alf.index(i)-dict_alf.index(result[j-1:j]))%p]
        j+=1
    print(result)
    return result
#Шифр Веженера по шифротексту
def СVez(str,key,alf):
    if len(key)!=1:
        print("Введите корректный ключ")
        return 0
    dict_alf = [i for i in alf]
    dict_str=[i for i in str]
    dict_key=[key]
    p=len(dict_alf)
    result=""
    j=0
    for i in dict_str:
        o=dict_alf[(dict_alf.index(i)+dict_alf.index(dict_key[j]))%p]
        result += o
        dict_key.append(o)
        j+=1
    print(result)
    return result
#расшифровка шифра Веженера по шифротексту
def DCVez(str,key,alf):
    dict_alf = [i for i in alf]
    dict_str=[i for i in str]
    p=len(dict_alf)
    result=""
    j=0
    for i in dict_str:
        if j==0:
            o=dict_alf[(dict_alf.index(i)-dict_alf.index(key))%p]
        else:
            o=dict_alf[(dict_alf.index(i)-dict_alf.index(dict_str[j-1]))%p]
        result+=o
        j+=1
    print(result)
    return result
str="зашифрвал и расшифровал шифром веженера"
key ="мой шифр"
k="р"
alf= "йцукенгшщзхъфывапролджэюбьтимсчя. -"
e = Vez(str,key,alf)
DVez(e,key,alf)
r=OVez(str,k,alf)
DOVez(r,k,alf)
m=СVez(str,k,alf)
DCVez(m,k,alf)