# Sintaxis

## Creación de variables

```r
x <- 10
y <- 5

print(x)
print(y)
```

## Operaciones

### Operaciones básicas

```r
suma <- x + y
print(suma)

resta <- x -y
print(resta)

multiplicacion <- x * y
print(multiplicacion)
```

### Medidas estadísticas

```r
edades <- c(25,30,35,40,45,50)

media <- mean(edades)

mediana <- median(edades)

desviacion_estandar <- sd(edades)

edades

print(media)

print(mediana)

print(desviacion_estandar)
```

### Operaciones avanzadas

```r
edades <- c(25,30,35,40,45,50)

media <- mean(edades)

mediana <- median(edades)

desviacion_estandar <- sd(edades)

edades

print(media)

print(mediana)

print(desviacion_estandar)
```

### Operaciones lógicas

```r
a <- 5

b <- 10

igual <- a ==b

mayor_que <- a<6 & b>5

y_logico <- a<6 | b<5
```

## Concatenación

```r
saludo <-"Bienvendios"

programa<-"Mi primer programa en R"

frase <- paste(saludo, programa, sep = ", ")

print (frase)

longitud <- nchar (frase)

palabras <- strsplit(frase, ", ")
```

## Estructuras de Datos

### Creación de arreglos

```r
df <- data.frame(

  Nombre = c("","",""),

  Edad= c(,,),

  Ciudad = c("","","")

)
```

### Mostrar arreglos

```r
print(df)
print(df$Nombre)
```

### Operaciones con arreglos

```r
variable <- df[df$Edad >30, ]
print(variable)
```

## If

```r
if (x > y){

  cat("X es mayor que y \n")

} else{ 

  cat("X no es mayor que y \n")

}
```

## Matrices

```r
mi_matriz <- matrix (1:9, nrow = 3, ncol = 3)

mi_matriz [2,3]

transpuesta <- t(mi_matriz)

print (transpuesta)


dim(matriz)
```

## Librerías

```r
install.packages("tidyverse")
install.packages("ggplot2")
install.packages("reshape2")
install.packages("e1071")
install.packages("dplyr")
install.packages("tidyr")
install.packages("caret")
install. packages("shiny")
install.packages("libridate")
install.packages("data.table")
install.packages("plotly")
```
