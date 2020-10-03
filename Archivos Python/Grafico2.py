import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('grafico2.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label='Grafico')
plt.xlabel('Tamano de Nubes ')
plt.ylabel('Carga de agua en la nube')
plt.title('Porcentaje de carga de agua')
plt.legend()
plt.show()
