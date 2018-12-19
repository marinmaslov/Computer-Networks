'''
    Code in Python (v.3.7.0) for long polynomial division
    Task 1, first homework by Julije Ožegović
    Computer Networks course @ FESB
'''

try:
    from itertools import izip 
except ImportError: 
    izip = zip  

def stupanj(polinom):
    while polinom and polinom[-1] == 0:
        polinom.pop()   
    return len(polinom)-1

def dijeljenje(B, N):
    nazivnik = stupanj(N)
    brojnik = stupanj(B)
    if nazivnik < 0: raise ZeroDivisionError 
    
    if brojnik >= nazivnik: 
        q = [0] * brojnik
        while brojnik >= nazivnik:
            d = [0]*(brojnik - nazivnik) + N
            mult = q[brojnik - nazivnik] = B[-1] / float(d[-1])
            d = [coeff*mult for coeff in d]
            B = [( coeffB - coeffd ) for coeffB, coeffd in izip(B, d)]
            brojnik = stupanj(B)
        r = B
    else: 
        q = [0]
        r = B
    return q[::-1], r[::-1] 

if __name__ == '__main__':
    print ("Dijeljenje polinoma:")
    B = [-2, -1, 2, 4][::-1]
    N = [2, -1, 1][::-1]
    print (" %s / %s =" % (B[::-1],N[::-1])),
    print (" %s , a ostatak je %s" % dijeljenje(B, N)) 
