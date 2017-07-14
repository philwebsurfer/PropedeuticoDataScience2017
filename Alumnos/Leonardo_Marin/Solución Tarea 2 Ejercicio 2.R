


##########################################################################################################################
## Ejercicio 2

##########################################################################################################################

pseudoinversa1 <- function(A)
{
  
  # A debe ser matriz
  A.svd <- svd(A)   #Descomposición SVD
  A.svd
  
  S.inv.fix <- diag(1/A.svd$d)  ## La inversa es 1 / los valores de la diagonal
  S.inv.fix[S.inv.fix == Inf] <- 0
  
  U <- A.svd$u
  V <- t(A.svd$v)
  
  ## PseudoInversa
  A.inv <- (t(V))%*%(S.inv.fix)%*%(t(U))  
  
  return(A.inv)
}


########################################

# Probar funcion
A <- matrix(c(1,1,0,2),ncol=2)

solve(A)
pseudoinversa1(A)

########################################




#####################################################################################################

sistema_ecuaciones1 <- function(A,b)
{
  ##A: matriz; b: puede ser vectot
  b <- as.matrix(b) 
  x <- pseudoinversa1(A)%*%b
  return(x)
  
}


## Probar funcion
A <- matrix(c(1,1,0,2),ncol=2)
b <- matrix(c(5,3))

# Solucuín exacta
solve(A)%*%b
# solucíon Función
sistema_ecuaciones1(A,b)



#######################################

# Hacer pruebas con distintas matrices

# Matriz de 2x3
B = matrix(c(1,1,0,2,8,-1),ncol=3)
B

solve(B) # Marca error por no ser cuadrada
pseudoinversa1(B) 

## Validación

## B.inv * B = In  (Mal)
## B * B.inv = In  (Ok)
pseudoinversa1(B) %*% B
B %*% pseudoinversa1(B) 


##################################################
# Solucionar un sistema que incluya la matriz B

c <- matrix(c(2,1))

##
sistema_ecuaciones1(B,c)

# Validación
B%*%sistema_ecuaciones1(B,c)




##################################################################

#Probar la función para matrices aleatorias de nxm  (9x9 max)

#help(sample)  

(n <- sample(1:9,1))
(m <- sample(1:9,1))
(coeficientes <- sample(-9:9,n*m,replace=TRUE))
(d <- sample(-9:9,n))

(W <- matrix(coeficientes,n,m)) 
(z <- matrix(d))

pseudoinversa1(W)
sistema_ecuaciones1(W,z)

#Validación (W * (resultado sistema) debe dar el vector z) 
W%*%sistema_ecuaciones1(W,z)

pseudoinversa1(W)%*%W # (Mal)
W%*%pseudoinversa1(W) # (Ok)




#######################################################################################
## Pruebas con matrices que tienen filas linealmente dependientes (No son Invertibles)

## El vector está en la imagen (primer ejemplo)

AA <- matrix(c(1,1,0,0),ncol=2,byrow = TRUE)
bb <- matrix(c(4,0))

AA
bb


## AA no tiene inbversa
solve(AA)
## Psuedoinversa(AA)
pseudoinversa1(AA)




# Solucuín exacta (Error)
solve(AA)%*%b
# solucíon Función
sistema_ecuaciones1(AA,bb)


## Validación
bb
AA%*%sistema_ecuaciones1(AA,bb)



#######################################################################################
## Pruebas con matrices que tienen filas linealmente dependientes (No son Invertibles)

## El vector NO está en la imagen (primer ejemplo)

AA1 <- matrix(c(1,1,0,0),ncol=2,byrow = TRUE)
bb1 <- matrix(c(1,1))

AA1
bb1

## Psuedoinversa(AA1)
pseudoinversa1(AA1)

# solucíon Función
sistema_ecuaciones1(AA1,bb1)


## Validación
bb1
AA1%*%sistema_ecuaciones1(AA1,bb1)


#######################################################################################
## Pruebas con matrices que tienen filas linealmente dependientes (No son Invertibles)

## El vector está en la imagen (segundo ejemplo)
## Números muy proximos a cero,

AA2 <- matrix(c(1,1,0,1e-32),ncol=2,byrow = TRUE)
bb2 <- matrix(c(4,0))

AA2
bb2

## Psuedoinversa(AA2)
pseudoinversa1(AA2)

# solucíon Función
sistema_ecuaciones1(AA2,bb2)


## Validación
bb2
AA2%*%sistema_ecuaciones1(AA2,bb2)


#######################################################################################
## Pruebas con matrices que tienen filas linealmente dependientes (No son Invertibles)

## El vector NO está en la imagen (segundo ejemplo)
## Números muy proximos a cero,

AA3 <- matrix(c(1,1,0,1e-32),ncol=2,byrow = TRUE)
bb3 <- matrix(c(1,1))

AA3
bb3

## Psuedoinversa(AA3)
pseudoinversa1(AA3)
AA3*pseudoinversa1(AA3)


# solucíon Función
sistema_ecuaciones1(AA3,bb3)


## Validación
bb3
AA3%*%sistema_ecuaciones1(AA3,bb3)




