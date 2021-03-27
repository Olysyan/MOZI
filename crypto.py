#!/bin/python3.8
#функция округления квадратного корня
import math
import random
def nround(num):
    j = num**(1/2)
    if (j-0.5)//1 == (j-1)//1:
        return int(j//1)
    else:
        return int(j//1+1) 
#НОД
def nod(x,y):
    while y!=0:
        y,x = x%y, y
    return x
#расширенный алгоритм Евклида, вычисление a^-1 (mod b)
def evkl(a,b):
    if nod(a,b)>1:
        print("Нет обратного элемента")
        return False
    else:
        t=1
        y=0.5
        while y%1!=0:
            y=((1-t*b)/a)%b
            t+=1
        t=t-1
        if y>b/2:
            y=int(y-b)
        if t>b/2:
            t=int(t-b)
        return [int(y),t]
#вычисление дискретного логарифма:
#log a b, в поле [Z/p]
def logarifm(a,b,p):
    j=nround(p)
    e=evkl(a,p)[0]
    ev= pow(e,j,p)
    power_a={}
    res=0
    for i in range(0,j):
        power_a[i]=pow(a,i,p)
    for k in range(0,j):
        q =(b*pow(ev,k,p))%p
        for key, val in power_a.items():
            if q == val:
                res = k*j+key
                return res
#решение систем сравнений вида:
#x==2(mod4)
#x==3(mod5)
#x==2(mod7)
#.... 
def Soe(*args):
    N=1
    for a,p in args:
        N*=p
    x=0
    for a,p in args:
        x+=a*evkl(N/p,p)[0]*N/p
    return x%N
#вычисление символа лежандра: Критерий Эйлера, Критерий Гаусса, Квадратичный закон взаимности
def Euler(a,p):
    eul=pow(a,int((p-1)/2),p)
    if eul == 1:
        return 1
    if eul == p-1:
        return -1
    return eul
def Gauss(a,p):
    j=0
    l=[]
    for i in range(0,int((p-1)/2)):
        g= (i*a)%p
        l.append(g)
        if g>=round(p/2):
            j+=1
    return (-1)**j
def loqr(a,p):
    l=a%p
    while l!=1 and l!=p-1:
        a,p=p,a
        l=a%p
    if l == p-1:
        return -1
    return 1
#вычисление квадратного корня по модулю простого числа
def dsqrt(a,p):
    if Euler(a,p) == -1:
        print("квадратных корней нет")
        return False
    for b in range(2,p):
        if Euler(b,p) == -1:
            break
    t=p-1
    s=0
    while t%2==0:
        t=t//2
        s+=1 
    c=int(pow(b,t,p))
    r=int(pow(a,(t+1)//2,p))
    result=[]
    if s ==1:
        s=2
    for i in range(1,s):
        d = ((r**2*evkl(a,p)[0])*2**(s-i-1))%p
        if d == -1:
            r =(c*r)%p
        c=c**2
        result.append(r)
        result.append(-r)
    return result
#разложение составного числа на простые
def simpnum(num):
    a={1}
    for i in range(2,int(num/2)+1):
        while num%i==0:
            a.add(i)
            num = int(num/i)
    if a=={1}:
        a.add(num)
    return list(a)

def Pnum(set_p):
    r=1
    for i in set_p:
        r*=i
    return int(r)
#Pollard быстрее алгоритма simpnum на несколько порядков, не работает с числами меньше трех знаков
def Pollard(num,p={1}):
    a=2
    b=2
    d=1
    num=int(num)
    while num/Pnum(p)!=1:
        a=(a**2+1)%num
        b=(b**2+1)%num
        b=(b**2+1)%num
        d=int(math.gcd(a-b,num))
        if d == num:
            p.add(int(d))
            return list(p)
        if 1<d<num:
            Pollard(num/d)
            p.add(int(d))
    return list(p)
#вычисление квадратного корня по модулю составного числа, вида n=pq, где  p и q - простые числа 
def comparison(a,b):
    mass_p=Pollard(b)
    mass_sqrt=[]
    res=[]
    if mass_p[0]==b:
        return dsqrt(a,b)
    for p in mass_p:
        mass_sqrt.append(dsqrt(a,p))
    ev=evkl(mass_p[0],mass_p[1])
    #print(f"({mass_sqrt[0][0]}*{ev[1]}*{mass_p[1]} +{mass_sqrt[1][0]}*{ev[0]}*{mass_p[0]})%{b}")
    #print(f"({mass_sqrt[0][0]}*{ev[1]}*{mass_p[1]} -{mass_sqrt[1][0]}*{ev[0]}*{mass_p[0]})%{b}")
    x=(mass_sqrt[0][0]*ev[1]*mass_p[1] +mass_sqrt[1][0]*ev[0]*mass_p[0])%b
    y=(mass_sqrt[0][0]*ev[1]*mass_p[1] -mass_sqrt[1][0]*ev[0]*mass_p[0])%b
    if x>b/2:
        x=int(x-b)
    if y>b/2:
        y=int(y-b)
    res.append(x)
    res.append(-x)
    res.append(-y)
    res.append(y)
    return res
#
class Point:
    b = 7
    def __init__(self, x=float('inf'), y=float('inf')):
        self.x = x
        self.y = y
 
    def copy(self):
        return Point(self.x, self.y)
 
    def is_zero(self):
        return self.x > 1e20 or self.x < -1e20
 
    def neg(self):
        return Point(self.x, -self.y)
 
    def dbl(self):
        if self.is_zero():
            return self.copy()
        try:
            L = (3 * self.x * self.x) / (2 * self.y)
        except ZeroDivisionError:
            return Point()
        x = L * L - 2 * self.x
        return Point(x, L * (self.x - x) - self.y)
 
    def add(self, q):
        if self.x == q.x and self.y == q.y:
            return self.dbl()
        if self.is_zero():
            return q.copy()
        if q.is_zero():
            return self.copy()
        try:
            L = (q.y - self.y) / (q.x - self.x)
        except ZeroDivisionError:
            return Point()
        x = L * L - self.x - q.x
        return Point(x, L * (self.x - x) - self.y)
 
    def mul(self, n):
        p = self.copy()
        r = Point()
        i = 1
        while i <= n:
            if i&n:
                r = r.add(p)
            p = p.dbl()
            i <<= 1
        return r
 
    def __str__(self):
        return "({:.3f}, {:.3f})".format(self.x, self.y)
 
def show(s, p):
    print(s, "Zero" if p.is_zero() else p)
 
def from_y(y):
    n = y * y - Point.b
    x = n**(1./3) if n>=0 else -((-n)**(1./3))
    return Point(x, y)
 
# demonstrate
a = from_y(1)
b = from_y(2)
show("a =", a)
show("b =", b)
c = a.add(b)
show("c = a + b =", c)
d = c.neg()
show("d = -c =", d)
show("c + d =", c.add(d))
show("a + b + d =", a.add(b.add(d)))
show("a * 12345 =", a.mul(12345))
""" def Lenstr(n):
    a=random.randint(1,n)
    x1=random.randint(1,n)
    y1=random.randint(1,n)
    b=(y1**2-x1**2-a*x1)%n

    d=nod(-4*a**3-27*b**2,n)
    while d==n:
        a=random.randint(1,n)
        b=(y1**2-x1**2-a*x1)%n
        d=nod(-4*a**3-27*b**2,n)
    if 1<d<n:
        return d
     """