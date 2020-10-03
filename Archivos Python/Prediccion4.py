import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor

datos = pd.read_csv("Grafico4.csv")
x = datos["electronesNegativos"]
y = datos["probabilidadRayos"]

X = x[:, np.newaxis]

while True:
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    mlr = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3,3), random_state=1)
    mlr.fit(X_train,y_train)
    print(mlr.score(X_train,y_train))
    if mlr.score(X_train,y_train) > 0.95:
        break

valor = input("Ingrese cantidad de electrones negativos: ")
print(valor)


print("Cantidad de electrones negativos ingresados: ")
print(valor)

print("\n")
print("La probabilidad de que caigan rayos es de ")
print(mlr.predict([[valor]]))
print(" %")

if(mlr.predict([[valor]]) > 60):
    print("Se sugieren tomar medidas de precaucion")
elif(mlr.predict([[valor]]) > 90):
    print("Se sugiere tomar medidas altas de precaucion")

