#!/bin/python3.8
from crypto import evkl,nod
#шифр простой замены
def SRC(string,kkk,alf):
    dict_alf =[i for i in alf]
    p =len(alf)
    while nod(kkk,p)!=1:
        print(f"Введите подходящие параметры для алфавита мощностью {p}: ")
        kkk= int(input("a: "))
    crypt=""
    for i in string:
        if i in dict_alf:
            crypt += dict_alf[(dict_alf.index(i) + kkk)%p]
    print(f"используемый алфавит: {alf}\n")
    print(f"строка для шифрования: {string}\n")
    print(f"результат шифрования с параметром {kkk}: {crypt}\n")
    return [crypt,kkk]
#Расшифровка
def DSRC(string,kkk,alf):
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
def AC(string,a,b,alf):
    dict =[i for i in alf]
    res=""
    p = len(dict)
    d=[i for i in dict]
    while nod(a,p)!=1 or nod(b,p)!=1 or a==b:
        print(f"Введите подходящие параметры для алфавита мощностью {p}: ")
        a= int(input("a: "))
        b= int(input("b: "))
    for i in string:    
        for j in d:
            if i ==j: 
                res+= d[((a*d.index(j)+b)%p)]
    print(f"Зашифровано аффинным шифром с параметрами {a,b} : {res}\n")
    return [res,a,b]
#расшифрование аффинного шифра
def DAC(string,a,b,alf):
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
                if g in j.values():
                    for y,u in k.items():
                        for o,r in p.items():   
                            if g!=o and r==i==u==v:
                                j[q]=g+"/"+o
                else:
                    j[q]=g
    print(f"сопоставление частот встречаемости зашифрованного и исходного текстов: {j}\n")
    return j
#аффинный рекуррентный шифр
def ARC(string,a,b,c,d,alf):
    dict =[i for i in alf]
    res=""
    p = len(dict)
    while nod(a,p)!=1 or nod(b,p)!=1 or nod(c,p)!=1 or nod(d,p)!=1 or a==c or b==d or d== c or a==d or b==a or c==b:
        print(f"Введите подходящие параметры для алфавита мощностью {p}: ")
        a= int(input("a: "))
        b= int(input("b: "))
        c= int(input("c: "))
        d= int(input("d: "))
    a1=a
    b1=b
    c1=c
    d1=d
    for i in string:    
        for j in dict:
            if i ==j:
                y = a*c%p
                x = (b + d)%p
                res+= dict[((y*dict.index(j)+x)%p)]
                a,c,b,d=c,y,d,x
    print(f"Зашифровано аффинным рекуррентным шифром с параметрами {a1,b1,c1,d1} : {res}\n")
    return [res,a1,b1,c1,d1]
#расшивровка аффинного рекуррентного шифра
def DARC(string,a,b,c,d,alf):
    dict =[i for i in alf]
    res=""
    p = len(dict)
    a1=a
    b1=b
    c1=c
    d1=d
    for i in string:    
        for j in dict:
            if i ==j:
                y = a*c%p
                x = (b + d)%p
                res+= dict[(evkl(y,p)[0]*(dict.index(j)-x))%p]
                a,c,b,d = c,y,d,x
    print(f"Результат расшифровки с параметрами {a1,b1,c1,d1} : {res}\n")
    return res
#пример работы
string = "зашифровал."
alf=",- !?./йцукенгшщзхъфывапролджэячстмиьбюЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ"
ff =SRC(string,5,alf)#зашифровываем сообщение методом простой замены
DSRC(ff[0],ff[1],alf) #расшифровываем это сообщение
mapping(FCA(ff[0]),FCA(string))#сопоставляем частотные анализы
a = AC(string,2,7,alf)#зашифровываем аффинным шифром
DAC(a[0],a[1],a[2],alf)#расшифровываем
mapping(FCA(a[0]),FCA(string))#сопоставляем частотные анализы
m = ARC(string,2,3,5,7,alf)#зашифровываем Аффинным рекуррентным шифром
DARC(m[0],m[1],m[2],m[3],m[4],alf)#расшифровываем