import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('grafico4.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label='Grafico')
plt.xlabel('Cantidad de electrones negativos')
plt.ylabel('Probabilidad de rayos')
plt.title('Probabilidad de que caigan rayos')
plt.legend()
plt.show()
