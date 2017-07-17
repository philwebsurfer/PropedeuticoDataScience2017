recetas <- read.csv("recetas.csv")
head(recetas)
View(recetas)
X <- recetas[ , -(1:1)] #le quita las primeras dos columnas recetas | 1:2 = c(1,2)
row.names(X) <- recetas$Clase_terapeutica_III
#install.packages("FactoMineR", dependencies = TRUE)
library("FactoMineR")

model <- PCA(X)
