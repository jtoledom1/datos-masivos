---
# 🧮 **Ejercicio 1: Funciones - Factorial**

```r
# 🔰 Definir la función factorial
factorial <- function(n) {
  resultado <- n  # Inicializa el resultado
  while (n > 1) {  # Mientras n > 1
    n <- n - 1      # Decrementa n
    resultado <- resultado * n  # Multiplica
  }
  return(resultado)  # Devuelve el factorial
}

# 🔰 Llamada a la función
factorial(7)  # Resultado: 5040

print(factorial(7))

```

---

# 🧩 **Ejercicio 2: Matrices y Operaciones**

```r
# 🔰 Crear vectores columna
m <- c(14, 13, 10)
n <- c(10, 11, 15)
o <- c(19, 3, 15)

# 🔰 Formar la matriz B
B <- cbind(m, n, o)
B  # Imprimir matriz B

# 🔰 Crear la matriz A
A <- matrix(c(19, 8, 11, 2, 18, 17, 15, 19, 10), nrow = 3)
A  # Imprimir matriz A

# 🔰 Operaciones entre A y B
print(A + B)  # Suma elemento a elemento
print(A * B)  # Multiplicación elemento a elemento
print(A - B)  # Resta elemento a elemento

# 🔰 Diagonal y suma de diagonal
diag(A)  # Elementos diagonales
sum(diag(A))  # Suma de la diagonal
```

---

# 🔢 **Ejercicio 3: Resolución de Sistemas de Ecuaciones**

```r
# 🔰 Sistema 2x2
A <- matrix(c(3, 2, 2, -1), nrow = 2, byrow = TRUE)
B <- c(12, 1)
solucion <- solve(A, B)
print(solucion)  # Imprimir solución

# 🔰 Sistema 3x3
A <- matrix(c(2, 3, -1, 4, -1, 2, -3, 2, 4), nrow = 3, byrow = TRUE)
B <- c(9, 1, 5)
solucion <- solve(A, B)
print(solucion)  # Imprimir solución
```

## 🔰 Sistema 2x2

- **3x + 2y = 12**

- **2x - 1y = 1**



## 🔰 Sistema 3x3

- **2x + 3y - 1z = 9**

- **4x - 1y + 2z = 1**

- **-3x + 2y + 4z = 5**

---

# 📊 **Ejercicio 4: Pruebas Estadísticas**

```r
# 🔰 Muestras de datos
Metodo_A <- c(79.98, 80.04, 80.02, 80.04, 80.03, 80.03, 80.04, 79.97, 80.05, 80.03, 80.02, 80.00, 80.02)
Metodo_B <- c(80.02, 79.94, 79.98, 79.97, 79.97, 80.03, 79.95, 79.97)

# 🔰 Boxplot comparativo
boxplot(Metodo_A, Metodo_B)

# 🔰 Pruebas estadísticas
t.test(Metodo_A, Metodo_B)  # Comparar medias
var.test(Metodo_A, Metodo_B)  # Comparar varianzas
```

p>0.05

Mayor son similares 

p<0.05

Menor son diferentes



VAR= VARIANZAS

T.TEST= PROMEDIOS







---

# 🏆 **Ejercicio 5: Comparaciones Múltiples**

```r
# 🔰 Valores (falta completar los datos reales)
Metodo_A <- c(18, 30, 25, 70, ...)  # Agregar datos
Metodo_B <- c(40, 40, 40, ...)      # Agregar datos
Metodo_C <- c(900, 900, 900, ...)   # Agregar datos

# 🔰 Boxplot comparativo
boxplot(Metodo_A, Metodo_B, Metodo_C)

# 🔰 Pruebas de t entre métodos
t.test(Metodo_A, Metodo_B)
t.test(Metodo_A, Metodo_C)
t.test(Metodo_C, Metodo_B)

# 🔰 Pruebas de varianza entre métodos
var.test(Metodo_A, Metodo_B)
var.test(Metodo_A, Metodo_C)
var.test(Metodo_C, Metodo_B)
```

---

# 📅 **Ejercicio 6: Datos Mensuales**

```r
# 🔰 Datos de cada mes (falta completar)
Mayo <- c(1000, 1200, 1300, ...)  # Agregar datos
Junio <- c(1800, 1900, 1800, ...)  # Agregar datos
Julio <- c(800, 4500, 3500, ...)   # Agregar datos

# 🔰 Boxplot comparativo
boxplot(Mayo, Junio, Julio)

# 🔰 Pruebas de t entre meses
t.test(Mayo, Junio)
t.test(Mayo, Julio)
t.test(Julio, Junio)

# 🔰 Pruebas de varianza entre meses
var.test(Mayo, Junio)
var.test(Mayo, Julio)
```

---
