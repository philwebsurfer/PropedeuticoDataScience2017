library(ggplot2)
data("diamonds")

## Estructura de los datos
str(diamonds)
head(diamonds)


#######################################################################################################################################
## Utilizar unicamente variables n�mericas

variables.numericas <- which(sapply(diamonds,is.numeric))   #Un �ndice (vector) para saber que columnas son numericas (int o decimal)

datos <- diamonds[,variables.numericas]
str(datos)

p <- dim(datos)[2] # n�mero de coeficientes
n <- dim(datos)[1] # n�mero de observaciones  

#######################################################################################################################################
## Modelo de regresi�n
diamonds.lm <- lm(price~.,data=datos)

#diamonds.lm
summary(diamonds.lm)


## 1) Normalidad de los errores

par(mfrow=c(1,2))

hist(diamonds.lm$residuals,main="Histograma de los residuales",prob=TRUE,ylim = c(0,0.00030),xlab = "Residuales")
lines(density(sort(rnorm(100000,0,1500))),col="blue")


qqnorm(diamonds.lm$residuals)
qqline(diamonds.lm$residuals)

par(mfrow=c(1,1))


############ prueba de Bondad de Ajuste Shapiro- Wilk para validad Normalidad
##??kol

# Nota: La prueba shapiro s�lo soporta 500 valores
shapiro.test(sample(diamonds.lm$residuals,5000))





## 2)  �Varianza constante?
## Los errores deben verse de forma aleatoria al rededor del cero en funci�n de la variable objetivo (price)
plot(diamonds.lm$residuals ~ datos$price, xlab="Precio",ylab = "Residuales",main="�Los errores tienen Varianza contante?") 
abline(h = 0, lty = 3, col="red")


###########################################################################

## �ngulo entre los precios reales y las estimaciones
model <- summary(diamonds.lm)

angulo <- (180/pi)*(acos(sqrt(model$adj.r.squared)))
angulo 

######################################################################################################################################
## Crear funci�n de Log-verosiilitud

#help(optim)

## Nota: Asignar de forma predeterminada las matrices X y Y, para que la funci�n s�lo tenga que recibir un parametro 
## que sean los coeficientes a optimizar  
datos.Y <- datos$price
datos.X <- datos
datos.X$price <- NULL ## Drop la variable price



############################################################################################################################################

log.mle <- function(parametros,X = datos.X,Y = datos.Y)
  
{

# Los parametros de la funci�n son:
  #- parmetros: un vector con los coeficientes de beta + la varianza en la �ltima posici�n del vector 
  #- X: la matrix de variables independientes, no incluye la columna de unos (puede ser data frame o matriz)
  #- Y: la variable independiente 
   
# Garantizar el tipo de objeto correcto  
  parametros <- as.vector(parametros)
  matriz.x <- cbind(1,X)  ## Agregar la columna de unos (1s)
  matriz.x <- as.matrix(matriz.x)
  Y <- as.vector(Y)
  
 # En el objeto prametros, incluir los coeficientes de beta a estimar m�s la varianza al en la �ltima entrada del vector
  k <- length(parametros)
  beta <- parametros[c(1:(k-1))]    # Extrae los elementos expecto el �ltimo
  varianza <- parametros[k]         # Extare el �ltimo elemento
  
# P es en n�mero de parametros a  estimar
p <- length(beta)

## Notar que en R ya existe por default el valor para pi = 3.14 


error <- sum((Y - matriz.x%*%beta)^2)
# Nota: La funci�n "optim" m�nimiz por default, definir nuestra funci�n con un menos 
# Nota: se definio de forma positiva "mle" pues la versi�n original tiene signo negativo, esto para poder minimizar
mle <-  (p/2)*(log(2*pi)+log(varianza)) + (1/(2*varianza))*error
  
return(mle)
}  






##############################################################################################

## Utilizar la funci�n

## iniciar los parametros 
# Deben ser 7 betas + 1 varianza
valores.iniciales <- c(100,100,100,100,100,100,100,100)
length(valores.iniciales)


## Checar que la funci�n definida previamente se ejecute e forma correcta
log.mle(valores.iniciales)


## Utilizar la funci�n optim
optim(par=valores.iniciales, log.mle, method = "L-BFGS-B")

## Comparar con los resultados de la funci�n lm
diamonds.lm$coefficients

# Parece que la soluci�n encontr� optimos locales 


#############################################################################################################

### Utilizar algunos valores iniciales cercanos a los optimos

beta <- as.vector(diamonds.lm$coefficients)
matriz.x <- as.matrix(cbind(1,datos.X))  ## Agregar la columna de 1s

## Sabemos que el estimador por MLE (sesgado) de la varianz es: 
varianza <-  sum((datos.Y - matriz.x%*%beta)^2)/(n - p)


###############
casi.optimos <- c(diamonds.lm$coefficients,varianza) + 1000
casi.optimos

optim(par=casi.optimos, log.mle, method = "L-BFGS-B")


############## 
## Comparar con los resultados de la funci�n lm
diamonds.lm$coefficients
varianza 


## Notar que para la variables  depth, table, x, y , z se tom� un valor inicial 
## alejado del optimo y la funci�n los aproxim� a los ya conocidos y correctos

