#!/bin/python3.8
import numpy
from crypto import nod,evkl
from os import system
import itertools
#конструктор матрицы
def matrixconst(matrixwords,dict_alf):
    matrixkey=[i for i in matrixwords]
    p = len(matrixkey)
    p_dict=len(dict_alf)
    g=p**(1/2)
    while nod(p,p_dict)!=1 or g%1!=0:
        matrixkey.append(" ")
        p+=1
        g=p**(1/2)
    g = int(g)
    j,f=0,0
    for i in matrixkey:
        if i in dict_alf:
            matrixkey[j]=dict_alf.index(i)
            j+=1
    newmatrix=[[0]*g for i in range(g)]
    for i in range(p):
        if i%g==0 and i!=0:
            f+=1
            newmatrix[f][i%g]=matrixkey[i]
        else: 
            newmatrix[f][i%g]=matrixkey[i]
    return newmatrix
#разбиение строки на блоки
def mult(str,block,dict_alf):
    str_dict = [i for i in str]
    f,j,k=0,0,0
    for i in str_dict:
        if i in dict_alf:
            str_dict[j]=dict_alf.index(i)
            j+=1
    matrix_block=[[0]*block for i in range(len(str_dict)//block)]
    for i in str_dict:
        if k%block==0 and k!=0:
            f+=1
            matrix_block[f][k%block]=i
            k+=1
        else: 
            matrix_block[f][k%block]=i
            k+=1
    return matrix_block
#Шифр Хилла
def Hill(str,matrixkey,alf):
    print(f"входная строка для шифрования шифром Хилла: {str}")
    res =""
    dict_alf =[i for i in alf]
    p =len(alf)
    matrix_key = matrixconst(matrixkey,dict_alf)
    print(matrix_key[0])
    block = int(len(matrix_key[0]))
    print(len(str),block)
    while len(str)%block!=0:
        str+=" "
    det = round(numpy.linalg.det(matrix_key)%p)
    if nod(det,p)!=1 or det==0:
        return "введите другое ключ-слово"
    str_mass = mult(str,block,dict_alf)
    print(str_mass)
    result = str_mass
    for i in range(len(str_mass)):
        result[i]= numpy.dot(matrix_key,str_mass[i])%p
    for i in range(len(str_mass)):
        for j in result[i]:
            res+= dict_alf[j]
    print(f"зашифровано шифром Хилла с параметрами матрицы {matrix_key}: {res} ")
    return [res,matrix_key]
#алгебраич дополн
def algebr(matrix,len_alf):
    l=len(matrix)
    f=numpy.array(matrix)
    r=numpy.zeros((l,l))
    for i in range(l):
        for j in range(l):
            if l==2:
                r[i,j]=((-1)**(i+j)*numpy.delete(numpy.delete(f,i,0),j,1))%len_alf
            else:
                r[i,j]=((-1)**(i+j)*round(numpy.linalg.det(numpy.delete(numpy.delete(f,i,0),j,1))))%len_alf
    return r.astype(int)
#расшифрование Хилла
def DHill(str,matrixkey,alf):
    res =""
    dict_alf =[i for i in alf]
    p =len(alf)
    matrix_key = matrixconst(matrixkey,dict_alf)
    block = int(len(matrix_key[0]))
    matrix_key = numpy.transpose(matrix_key)
    det = round(numpy.linalg.det(matrix_key)%p)
    matrix_key=algebr(matrix_key,p)
    matrix_key = (evkl(det,p)[0]*matrix_key)%p
    str_mass = mult(str,block,dict_alf)
    result = str_mass
    for i in range(len(str_mass)):
        result[i]= numpy.dot(matrix_key,str_mass[i])%p
    for i in range(len(str_mass)):
        for j in result[i]:
            res+= dict_alf[j]
    print(f"шифр Хилла расшифрован: {res}")
    return res
#Рекуррентный шифр Хилла
def RHill(str,matrixkey1,matrixkey2,alf):
    print(f"входная строка для шифрования рекуррентным шифром Хилла: {str}")
    l1=[i for i in matrixkey1]
    l2=[i for i in matrixkey2]
    if len(l1)!=len(l2):
        return "Ключ-слова должны быть равной длины"
    res =""
    dict_alf =[i for i in alf]
    p =len(alf)
    matrix_key1 = matrixconst(matrixkey1,dict_alf)
    matrix_key2 = matrixconst(matrixkey2,dict_alf)
    block = int(len(matrix_key1[0]))
    str_mass = mult(str,block,dict_alf)
    result = str_mass
    i=0
    while i!= len(str_mass):
        matrix_key = numpy.dot(matrix_key1,matrix_key2)%p
        result[i]= numpy.dot(matrix_key,str_mass[i])%p
        matrix_key1, matrix_key2= matrix_key2, matrix_key
        i+=1
    for i in range(len(str_mass)):
        for j in result[i]:
            res+= dict_alf[j]
    print(f"зашифровано рекуррентным шифром Хилла: {res}")
    return res
#Расшифрование рекуррентого шифра Хилла
def DRHill(str,matrixkey1,matrixkey2,alf):
    res =""
    dict_alf =[i for i in alf]
    p =len(alf)
    matrix_key1 = matrixconst(matrixkey1,dict_alf)
    matrix_key2 = matrixconst(matrixkey2,dict_alf)
    block = int(len(matrix_key1[0]))
    str_mass = mult(str,block,dict_alf)
    result = str_mass
    for i in range(len(str_mass)):
        matrix_key = numpy.dot(matrix_key1,matrix_key2)%p
        matrix_mul = matrix_key
        det = round(numpy.linalg.det(matrix_key)%p)
        matrix_key=(evkl(det,p)[0]*numpy.transpose(algebr(matrix_key,p)))%p
        result[i]= numpy.dot(matrix_key,str_mass[i])%p
        matrix_key1, matrix_key2=  matrix_key2,matrix_mul
    for i in range(len(str_mass)):
        for j in result[i]:
            res+= dict_alf[j]
    print(f"реккурентный шифр Хилла расшифрован: {res}")
    return res
#криптоанализ атакой подбора на ключ-матрицу
def CA(str,len_key,alf):
    dict_alf=[i for i in alf]
    newstr=str[0:2*len_key]
    key_test1=""
    f=""
    system("echo начало >  brute.txt")
    for comb in itertools.product(dict_alf,repeat=len_key):
        key_test1= comb[0]+comb[1]+comb[2]+comb[3]
        try:
            m = DHill(newstr,key_test1,alf)
            system(f"echo '{key_test1}\n {m}\n' >>  brute.txt")
        except:                
            key_test1=""
        key_test1=""
    return 0
#Частотный криптоанализ блоков шифротекста
def CA2(str,len_key):
    k = 0
    l = len(str)/len_key
    d = {}
    di=[]
    ss=""
    for i in str:
        ss+=i
        if len(ss)==len_key and (ss  not in di):
            di.append(ss)
            ss=""
        elif ss  in di:
            ss=""
    str_mass=[str[i:i + len_key] for i in range(0, len(str) - (len(str) % len_key), len_key)]
    print(di,"\n",str_mass)
    for i in di:
        for j in str_mass:
            if j==i:
                k+=1
        d[i]=k/l
        k =0
    res={k:v for k,v in sorted(d.items(),key = lambda i:i[1])}
    return res
str = "шифрую шифр зашифрованный шифровальщиком"
alf=",- !?./йцукенгшщзхъфывапролджэячстмиьбю"
matrixkey1="шифровкам"
matrixkey2="мой!"
newstr=Hill(str,matrixkey1,alf)
print(f"1 ключ-слово: {matrixkey1} \n2 ключ-слово: {matrixkey2}")
DHill(newstr[0],matrixkey1,alf)
""" rhill=RHill(str,matrixkey1,matrixkey2,alf)
DRHill(rhill,matrixkey1,matrixkey2,alf)   """
""" print("Частотный криптоанализ для зашифрованного текста: ")
CA2(newstr[0],len(newstr[1]))
print("Частотный криптоанализ для входного текста: ")
CA2(str,len(newstr[1])) """