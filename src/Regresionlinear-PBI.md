# 🔰Regresión Linear

![](C:\Users\Jtole\AppData\Roaming\marktext\images\2025-04-10-12-40-38-image.png)

<img src="file:///C:/Users/Jtole/AppData/Roaming/marktext/images/2025-04-10-12-41-22-image.png" title="" alt="" width="648">

```python
# El código siguiente, que crea un dataframe y quita las filas duplicadas, siempre se ejecuta y actúa como un preámbulo del script: 

# dataset = pandas.DataFrame(año, Importe venta total)
# dataset = dataset.drop_duplicates()

# Pegue o escriba aquí el código de script:
# El código siguiente, que crea un dataframe y quita las filas duplicadas, siempre se ejecuta y actúa como un preámbulo del script: 

# dataset = pandas.DataFrame(año, Coste unitario, Precio Unitario, Unidades)
# dataset = dataset.drop_duplicates()

# Pegue o escriba aquí el código de script:
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Declarar el modelo indicando que vamos a utilizar regresión lineal 
model = LinearRegression()

# Ajustar el modelo con 'Unidades' como predictor e 'Importe venta total' como la variable objetivo
model.fit(dataset[['año']], dataset['Importe venta total'])

# Hacer predicciones utilizando 'Unidades', es decir según la cantidad conocer el importe
predicciones = model.predict(dataset[['año']])

# Graficar los resultados
plt.scatter(dataset['año'], dataset['Importe venta total'], color='blue')  # Datos reales
plt.plot(dataset['año'], predicciones, color='red')  # Línea de regresión
plt.title('Regresión Lineal')

nuevo_importe = 2023  # El valor de las unidades para el cual deseas predecir
prediccion_nueva = model.predict([[nuevo_importe]])

plt.title(f'Monto Predicción nueva de: {prediccion_nueva[0]:.2f}')
plt.xlabel('año')
plt.ylabel('Importe venta total')

# Agregar el nuevo punto al gráfico analizar
plt.scatter(nuevo_importe, prediccion_nueva, color='green', zorder=5) 

#visualizar el resultado
plt.show()
```
