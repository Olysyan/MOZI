#!/bin/python3.8
#
def Vez(str,key,alf):
    dict_key=[i for i in key]
    dict_alf = [i for i in alf]
    dict_str=[i for i in str]
    lstr=len(dict_str)
    ll=len(dict_key)
    p=len(dict_alf)
    result=""
    while lstr!=len(result):
        j=0
        for i in dict_str:
            result += dict_alf[(dict_alf.index(i)+dict_alf.index(dict_key[j%ll]))%p]
            j+=1
    print(result)
    return result
def DVez(str,key,alf):
    dict_key=[i for i in key]
    dict_alf = [i for i in alf]
    dict_str=[i for i in str]
    lstr=len(dict_str)
    ll=len(dict_key)
    p=len(dict_alf)
    result=""
    while lstr!=len(result):
        j=0
        for i in dict_str:
            result += dict_alf[(dict_alf.index(i)-dict_alf.index(dict_key[j%ll]))%p]
            j+=1
    print(result)
    return result
str="asdsdsdf"
key ="dskfgkjf"
alf= "qwertyuiopasdfghjklzxcvbnm"
e = Vez(str,key,alf)
DVez(e,key,alf)