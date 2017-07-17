INEGI <- read.csv('DatosINEGI.csv')
cols <- colnames(INEGI)
for (col in c("Secundarias", "DefuncionesGenerales", "Nacimientos", "Divorcios", "Matrimonios")) {
  INEGI[ ,col] <- INEGI[ ,col]  / INEGI[ ,"Poblacion"] 
}
X <- INEGI[ ,-(1:2)] # le quita las primeras dos columnas INEGI | 1:2 = c(1,2)
row.names(X) <- INEGI$Estado
head(X)
install.packages("FactoMineR")
library(FactoMineR)
model <- PCA(X)