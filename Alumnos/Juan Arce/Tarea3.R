install.packages("ggplot2")
install.packages("corrplot")
install.packages("FactoMineR")
library(ggplot2)
dt<-as.data.frame(diamonds)

head(dt)
str(dt)

fit <- lm(dt$price ~ dt$carat + dt$depth + dt$table + dt$x + dt$y + dt$z)
summary(fit)

library(FactoMineR)

dt$cut <- NULL
dt$color <- NULL
dt$clarity <- NULL

head(dt)

model <- PCA(dt)

##¿Qué tan bueno fue el ajuste?
#El ajuste del modelo no parece tan bueno, ya que al eliminar 
#las variables cualitativas también dejamos fuera información 
#que podría ser importante.

#Una varaible aporta al modelo si su coeficiente o pvalue
#es mayor que 0.05 o no.  En el caso de que sea mayor a 0.05
#no podemos rechazar la hipótesis de que ese valore es 0, por 
#lo que no sería relevante.

##¿Qué medida puede ayudarnos a saber la calidad e¡del ajuste?
#La R cuadrada.  

##Utilice la función optim de R para?
optim(dt)

