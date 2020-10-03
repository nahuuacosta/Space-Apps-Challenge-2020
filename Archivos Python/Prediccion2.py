import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor

datos = pd.read_csv("Grafico2.csv")
x = datos["tamanoNube"]
y = datos["cargaAgua"]

X = x[:, np.newaxis]

while True:
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    mlr = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3,3), random_state=1)
    mlr.fit(X_train,y_train)
    print(mlr.score(X_train,y_train))
    if mlr.score(X_train,y_train) > 0.95:
        break

valor = input("Ingrese tamaño nube en Kilometros: ")
print(valor)


print("Dimension de la nube: ")
print(valor)
print(" KM ")
print("\n")
print("Tendra una carga de agua de ")
print(mlr.predict([[valor]]))
print(" %")
