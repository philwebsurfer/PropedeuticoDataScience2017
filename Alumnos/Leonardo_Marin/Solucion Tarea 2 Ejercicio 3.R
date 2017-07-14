## Limpiar area de trabajo

rm(list=ls())
ls()

## Leer datos

datos <- read.table('C:/Users/Data Mining/Documents/ITAM/Propedeutico/Alumnos/PropedeuticoDataScience2017/Alumnos/Leonardo_Marin/study_vs_sat.csv', header = TRUE, sep=",")
datos


## Calcular a mano alpha y beta

## beta
mu.x <- mean(datos$study_hours)
mu.y <- mean(datos$sat_score)


numerador <-  sum((datos$study_hours - mu.x)*(datos$sat_score - mu.y))
denominador <- sum((datos$study_hours - mu.x)^2)

beta <- numerador/denominador


## alpha

alpha <- mu.y - beta*mu.x




###########################################################
## Realizar la regresión usando la funciones ya construidas en R

lm.sat <- lm(sat_score~study_hours,data=datos)
lm.sat

summary(lm.sat)

## Estimaciones  yhat = alpha + beta*X
predict(lm.sat,datos)


#################################################################################
## Definir la matriz X

matriz.x <- matrix(NA, ncol=2,nrow=dim(datos)[1])

matriz.x[,1] <- 1
matriz.x[,2] <- datos$study_hours
print(matriz.x)

## Calcular las estimaciones: sat_score ~ matriz.x * [alpha, beta]
## En R la multiplicación de matrices se hace con el operador %*%

sat_score <- matriz.x %*% c(alpha,beta)
sat_score


#################################################################################
# Calcular la PseudoInversa

X.svd <- svd(matriz.x)


## PseudoInversa = (inversa(transpuesta(V)))*(inversa(S))*(inversa(U))
## Nota: U y V son ortogonales por tanto su inversa es la transpuesta, y la inversa de S es 1 entre los valores de la diagonal


S.inv <- diag(1/X.svd$d)  ## La inversa es 1 / los valores de la diagonal
S.inv

U <- X.svd$u
U

V <- t(X.svd$v)
V

## PseudoInversa

pseu.inv <- (t(V))%*%(S.inv)%*%(t(U))
pseu.inv

## Calcular alpha y beta

solucion_aprox <- pseu.inv%*%as.matrix(datos$sat_score)
solucion_aprox 

#################################################################################
# Solución Exacta
# (alpha,beta)=(X^t*X)^(-1)*X^t*sat_score.


A <- t(matriz.x)%*%matriz.x

solucion_exacta <- solve(A)%*%t(matriz.x)%*%as.matrix(datos$sat_score)
solucion_exacta


## Comparar con la solución ce la pseudo inversa

# En este caso las soluciones dieron igual

solucion_exacta
solucion_aprox


#################################################################################
# Visualizar las predicciones contra los valores reales

plot(datos$sat_score~datos$study_hours)
# Agregar la linea de la regresión a la grafica de dispersión 
abline(lm.sat, col="blue")



