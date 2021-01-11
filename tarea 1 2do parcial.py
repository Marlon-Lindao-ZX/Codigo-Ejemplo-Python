from random import*
def sorteoentre(k,a,b):
    ans=[]
    for i in range(k):
        X=randint(a,b)
        while X in ans:
            X=randint(a,b)
        ans=ans+[X]
    return ans

#programa
Vector1=[]
Vector2=[]
a=sorteoentre(10,1,100)
b=sorteoentre(5,100,200)
Vector1=list(a)
Vector2=list(b)
Vector1.sort()
Vector2.sort()
print(Vector1)
print(Vector2)

