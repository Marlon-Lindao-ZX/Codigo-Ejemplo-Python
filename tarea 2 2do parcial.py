A=input('ingrese palabra ')
V='aeiou'
X=A[-1]
if X in V:
     F=A[-2:]
else:
     F=A[-3:]
print(A,X,F)
