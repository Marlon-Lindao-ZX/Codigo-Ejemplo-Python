def rangomayor(matriz):
    n=len(matriz[0])
    Mayor=0
    for i in range(n):
        for j in range(n):
            if matriz[i][j]>Mayor:
                Mayor=matriz[i][j]
            else:
                pass
    return Mayor

def cuenta(matriz,k):
    n=len(matriz[0])
    C=0
    for i in range(n):
        for j in range(n):
            if matriz[i][j]==k:
                C=C+1
            else:
                pass
    return C

def cuentatodos(matriz):
    n=len(matriz[0])
    a=rangomayor(matriz)
    D=[]
    for k in range(a+1):
        b=cuenta(matriz,k)
        D=D+[b]
    return D
        
