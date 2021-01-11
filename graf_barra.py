import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111)

datos=[10,0,9,10,7,3,1,-3]
xx=range(len(datos))

ax.bar(xx,datos)

plt.show()