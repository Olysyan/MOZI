#!/bin/python3.8
from crypto import evkl
#шифр простой замены
def SRC(string,kkk):
    alf=",- !?./йцукенгшщзхъфывапролджэячстмиьбюЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ"
    dict_alf =[i for i in alf]
    p =len(alf)
    crypt=""
    for i in string:
        if i in dict_alf:
            crypt += dict_alf[(dict_alf.index(i) + kkk)%p]
    print(f"используемый алфавит: {alf}\n")
    print(f"строка для шифрования: {string}\n")
    print(f"результат шифрования с параметром {kkk}: {crypt}\n")
    return crypt
#Расшифровка
def DSRC(string,kkk):
    alf=",- !?./йцукенгшщзхъфывапролджэячстмиьбюЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ"
    dict_alf =[i for i in alf]
    encrypt=""
    p =len(alf)
    for i in string:
        if i in dict_alf:
            encrypt += dict_alf[(dict_alf.index(i) - kkk)%p]
    print(f"результат расшифрования с параметром {kkk}: {encrypt}\n")
    return encrypt
#частотный анализ шифра простой замены
def FCA(string):
    dict = {i for i in string}
    k = 0
    l = len(string)
    d = {}
    for i in dict:
        for j in string:
            if i == j:
                k+=1
        d[i]=f"{k*100/l}%"
        k =0
    res={k:v for k,v in sorted(d.items(),key = lambda i:i[1])}
    print(f"Результат частотного криптоанализа для входящей последователности: {res}\n")
    return res
#аффинный шифр
def AC(string,a,b):
    alf=",- !?./йцукенгшщзхъфывапролджэячстмиьбюЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ"
    dict =[i for i in alf]
    res=""
    p = len(dict)
    d=[i for i in dict]
    for i in string:    
        for j in d:
            if i ==j:
                res+= d[((a*d.index(j)+b)%p)]
    print(f"Зашифрованно аффинным шифром с параметрами {a,b} : {res}\n")
    return res
#расшифрование аффинного шифра
def DAC(string,a,b):
    alf=",- !?./йцукенгшщзхъфывапролджэячстмиьбюЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ"
    d =[i for i in alf]
    res=""
    p = len(d)
    for i in string:    
        for j in d:
            if i ==j:
                res+= d[(evkl(a,p)[0]*(d.index(j)-b))%p]
    print(f"Результат расшифровки с параметрами {a,b} : {res}\n")
    return res
#сопоставление частот встречаемости зашифрованного и исходного текстов для проверки достоверности криптоанализа
def mapping(p,k):
    j={}
    for q,i in k.items():
        for g,v in p.items():
            if v==i:
                j[q]=g
    print(f"сопоставление частот встречаемости зашифрованного и исходного текстов: {j}\n")
    return j
#аффинный рекуррентный шифр
def ARC(string,a,b,c,d):
    alf=",- !?./йцукенгшщзхъфывапролджэячстмиьбюЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ"
    dict =[i for i in alf]
    res=""
    p = len(dict)
    for i in string:    
        for j in dict:
            if i ==j:
                y = a*c%p
                x = (b + d)%p
                res+= dict[((y*dict.index(j)+x)%p)]
                a,c,b,d=c,y,d,x
    print(f"Зашифрованно аффинным рекуррентным шифром с параметрами {a,b,c,d} : {res}\n")
    return res
#расшивровка аффинного рекуррентного шифра
def DARC(string,a,b,c,d):
    alf=",- !?./йцукенгшщзхъфывапролджэячстмиьбюЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ"
    dict =[i for i in alf]
    res=""
    p = len(dict)
    for i in string:    
        for j in dict:
            if i ==j:
                y = a*c%p
                x = (b + d)%p
                res+= dict[(evkl(y,p)[0]*(dict.index(j)-x))%p]
                a,c,b,d = c,y,d,x
    print(f"Результат расшифровки с параметрами {a,b,c,d} : {res}\n")
    return res
#пример работы
string = "шуе ппш ппш шуе"
ff =SRC(string,5)#зашифровываем сообщеие методом простой замены
DSRC(ff,5) #расшифровываем это сообщение
mapping(FCA(ff),FCA(string))#сопоставляем частотные анализы
a = AC(string,5,7)#зашифровываем аффинным шифром
DAC(a,5,7)#расшифровываем
mapping(FCA(a),FCA(string))#сопоставляем частотные анализы
m = ARC(string,5,7,2,3)#зашифровываем Аффинным рекуррентным шифром
DARC(m,5,7,2,3)#расшифровываем