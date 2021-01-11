from random import*
def Gemword(n):
    Vocales='aeiou'
    Consonantes='qwrtypsdfghjklñzxcvbnm'
    V=len(Vocales)
    C=len(Consonantes)
    I=randint(0,1)
    P=[]
    for i in range(n):
        if I==0:
            X=randint(0,V-1)
            b=Vocales[X]
            P=P+[b]
            I=1
        else:
            X=randint(0,C-1)
            P=P+[Consonantes[X]]
            I=0
    return P
