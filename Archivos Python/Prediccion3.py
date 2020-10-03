import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor

datos = pd.read_csv("Grafico3.csv")
x = datos["nivelHumedad"]
y = datos["probabilidadLluvia"]

X = x[:, np.newaxis]

while True:
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    mlr = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3,3), random_state=1)
    mlr.fit(X_train,y_train)
    print(mlr.score(X_train,y_train))
    if mlr.score(X_train,y_train) > 0.95:
        break

valor = input("Ingrese el nivel de humedad: ")
print(valor)


print("Nivel de humedad ingresado: ")
print(valor)
print(" KM ")
print("\n")
print("Hay una probabilidad de lluvias del ")
print(mlr.predict([[valor]]))
print(" %")
