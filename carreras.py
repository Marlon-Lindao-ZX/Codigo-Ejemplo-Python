from random import*
A=[]
n=int(input('ingrese numero de estudiantes'))
for i in range(n):
    b=[]
    mtr=randint(199900001,201599999)
    nom=input('ingrese nombre de estudiante')
    carrera=input('ingrese carrera')
    edad=randint(18,25)
    b=b+[mtr,nom,carrera,edad]
    A=A+[b]
print(A)
C=[]
X=[]
for i in range(n):
    if A[i][2] not in X:
        C=C+[A[i][2]]
        X=X+[A[i][2]]
    else:
        pass
C.sort()
print(C)
D=[]
P=0
for k in range(len(C)):
    V=0
    D=D+[V]
for i in range(n):
    e=0
    P=P+A[i][3]
    for j in range(len(C)):
        if A[i][2]==C[j]:
            D[j]=D[j]+1
            break
        else:
            pass
S=P/n
print(D)
print(S)
        
            
    


        
    

    
    
      
