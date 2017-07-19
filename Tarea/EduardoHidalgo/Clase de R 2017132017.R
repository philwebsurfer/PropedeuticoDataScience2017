algo<-read.csv("DatosINEGI.csv")
head(algo)


for (var in c("Secundarias","DefuncionesGenerales","Nacimientos","Divorcios","Matrimonios")){
  algo[ ,col]<-algo[ ,col] / algo[ ,"Poblacion"]
}
x<-algo[ ,-(1:2)]
row.names(x)<-algo$Estado
head(x)
install.packages("FactoMineR")
library(FactoMineR)
model<-PCA(x)