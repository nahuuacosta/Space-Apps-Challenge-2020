import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('grafico1.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label='Grafico')
plt.xlabel('Aire Caliente')
plt.ylabel('Probabilidad de nubes')
plt.title('Prediccion de nubes')
plt.legend()
plt.show()
