# -*- coding: utf-8 -*-
import numpy as np
from sklearn.linear_modl import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
Y = np.array([3, 4.4, 5, 5.3, 6])

modelo = LinearRegression()
modelo.fit(X, Y)
coef = modelo.coef_[0]
intercepto = modelo.intercept_
print(f"pendiente: {coef}")
print(f"intercepto: {intercepto}")
horas_nuevas = np.array([[6], [7], [10]])
predicciones = modelo.predict(horas_nuevas)

for prediccion in zip(horas_nuevas, predicciones):
        print(f" predicción es: {prediccion}") 