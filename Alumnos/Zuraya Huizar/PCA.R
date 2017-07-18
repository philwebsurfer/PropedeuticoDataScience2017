INEGI <- read.csv(url("https://raw.githubusercontent.com/mauriciogtec/PropedeuticoDataScience2017/master/Datos/DatosINEGI.csv"))
head(INEGI)  

for (col in c("Secundarias", "DefuncionesGenerales", "Nacimientos", "Divorcios", "Matrimonios")){
  INEGI[ ,col]<-INEGI[ ,col]/INEGI[ ,"Poblacion"]
}

X<-INEGI[ ,-(1:2)] #le quita las dos primeras columnas INEGI
row.names(X)<-INEGI$Estado
head(X)

#install.packages("FactoMineR")
library(FactoMineR)
model<-PCA(X)