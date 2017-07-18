

setwd("C:/ITAM")

#download.file("https://raw.githubusercontent.com/mauriciogtec/PropedeuticoDataScience2017/master/Datos/DatosINEGI.csv?_sm_au_=iFV4zFHRq7n42Pj6", "inegi.csv")
inegi <- read.csv("inegi.csv")
print(inegi)
str(inegi)

 
for(col in c("Secundarias","DefuncionesGenerales","Nacimientos","Divorcios","Matrimonios")) {
   #inegi[ ,col] <- inegi[,col] / inegi[ "Poblacion"]
  inegi[,col] = inegi[,col] / inegi["Poblacion"]
}
X<-inegi[ ,-(1:2)]
row.names(X)<- inegi$X...Estado

install.packages("FactoMineR")
library(FactoMineR)

model <-PCA(X)
