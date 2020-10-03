import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('grafico3.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label='Grafico')
plt.xlabel('Nivel de humedad')
plt.ylabel('Probabilidad de lluvias')
plt.title('Probabilidad de lluvias')
plt.legend()
plt.show()
