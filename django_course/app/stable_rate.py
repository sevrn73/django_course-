import math as m
from scipy import special

def Pt11 (N, T, k, por, mu, Ct, Bo, rw, re, h, Po, q):
    #     ''''''
#     'Вычисляет значение забойного давления от времени, все переменные размерности[Си], выполняя обратное
#     'преобразование Лапласа и переводя P(s)-->P(t)
#     'T - значение времени в секундах
#     'N - точность
#     'Условие постоянного давления на границе пласта
#     ''''''
    Summ = 0
    for j in range(1, N):
        si = (m.log(2)/T)*j
        fi = Ps11(k, por, mu, Ct, Bo, rw, re, h, Po, q, si)
        Vi = special.mathieu_even_coef(j, N) # binom ??? Coef(N, j)
        #print(Vi)
        #Vi = [-0.2]
        r = (m.log(2)/T)*Vi[0]*fi
        Summ += r
        
    return Summ

def Ps11(k, por, mu, Ct, Bo, rw, re, h, Po, q, s):
#     ''''''''''''
#     'Решение для одного пласта с постоянным давлением на границе
#     'Вычисляет давление в пространстве Лапласа p(s)
#     'z - коэффициент пьезопроводности
#     'ZNAM - знаменатель
#     'MULT - множитель
#     'CHISL - числитель
#     ''''''''''''
    z = k/ (por*mu*Ct)
    xe = (s/z)**0.5*re
    xw = (s/z)**0.5*rw
    ZNAM = special.j0(xe)*special.kn(1, xw)+special.j1(xw)*special.kn(0, xe)
    MULT = ((z**0.5)/(s**1.5))*((mu*Bo*q)/(2*3.14*k*h*rw))
    CHISL = special.kn(0, xe)*special.j0(xw)-special.j0(xe)*special.kn(0, xw)
    p = MULT*(CHISL/ZNAM)
#     chisl = special.kn(0, xw)*special.j1(xe)+special.j0(xw)*special.kn(1, xe)
#     #znam = special.kn(1, xw)*special.j1(xe)-special.j1(xw)*special.kn(1, xe)
#     znam = special.j1(xe)*special.kn(1, xw)
    #p = ((mu*Bo*q)/(2*3.14*k*h*rw)*(z/s)**0.5)*(CHISL/ZNAM)
    
    return p

def Pt(k, por, mu, Ct, Bo, rw, re, h, Po, q, s):
#     ''''''''''''
#     'Решение для одного пласта с постоянным давлением на границе
#     'Вычисляет давление в пространстве Лапласа p(s)
#     'z - коэффициент пьезопроводности
#     'ZNAM - знаменатель
#     'MULT - множитель
#     'CHISL - числитель
#     ''''''''''''
    z = k/ (por*mu*Ct)
    xe = (s/z)**0.5*re
    xw = (s/z)**0.5*rw
    ZNAM = special.j1(xe)
    #ZNAM = special.kn(1, xw)*special.j1(xe)-special.j1(xw)*special.kn(1, xe)
    MULT = ((mu*Bo*q)/(2*3.14*k*h))#*rw)*(z/s)**0.5)
    CHISL = special.kn(0, xw)*special.j1(xe)+special.kn(1, xe)
    #CHISL = special.kn(0, xw)*special.j1(xe)+special.j0(xw)*special.kn(1, xe)
    p = MULT*(CHISL/ZNAM)
    
    return p