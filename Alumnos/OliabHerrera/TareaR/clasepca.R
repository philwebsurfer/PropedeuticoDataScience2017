

library(FactoMineR)

inegi<-read.csv(url("https://raw.githubusercontent.com/mauriciogtec/PropedeuticoDataScience2017/master/Datos/DatosINEGI.csv"))

##cambiando a porcentajes

variables<- c("Secundarias", "DefuncionesGenerales","Nacimientos","Divorcios"  ,"Matrimonios")

for (col in variables){
  inegi[,col]<-inegi[,col] / inegi[,"Poblacion"]
}

x<-inegi[,-c(1:2)]
row.names(x)<-inegi$Estado

PCA(x)


