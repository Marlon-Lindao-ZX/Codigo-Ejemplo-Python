from random import*
def desordena(palabra):
    v=len(palabra)
    NP=[]
    I=[]
    for i in range(v):
        X=randint(0,v-1)
        while X in I:
            X=randint(0,v-1)
        b=palabra[X]
        NP=NP+[b]
        I=I+[X]
    return NP
        
