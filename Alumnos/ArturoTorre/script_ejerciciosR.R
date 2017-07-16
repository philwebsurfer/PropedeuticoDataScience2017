library(ggplot2)
library(FactoMineR)
library(RColorBrewer)


#Regresion lineal
str(diamonds)

regresion<- lm(price~carat+depth+table+x+y+z, data=diamonds)

regresion

summary(regresion)

errores = regresion$residuals

plot(regresion$fitted.values,diamonds$price)

ys <- as.data.frame(cbind(regresion$fitted.values,diamonds$price))
names(ys) <- c("fit_y","y")


ggplot(ys,aes(x=fit_y,y=y, color="red")) + geom_point(aes(colour = y)) +
  theme_light() +
  ggtitle("Precio de los diamantes y sus valores ajustados") +
  xlab ("Valores ajustados de Y") + ylab("Valores reales de Y") +
  theme(legend.position = "none")

x_y = as.data.frame(cbind(diamonds$price,diamonds$carat))
names(x_y) <- c("price","carat")

ggplot(x_y,aes(x=carat,y=price, color="red")) + geom_point(aes(colour = price)) +
  theme_light() +
  ggtitle("Price vs Carat") +
  xlab ("Carat") + ylab("Price") +
  theme(legend.position = "none")

indice <- seq(1,nrow(diamonds),1)

errores_plot <- as.data.frame(cbind(indice,errores))
names(errores_plot)

ggplot(errores_plot,aes(x=indice,y=errores)) + geom_point(aes(colour = errores)) +
  theme_light() +
  ggtitle("Distribucion de los errores") +
  theme(legend.position = "none")

#rss <- sum(residuals(regresion)^2)

### Optim
diamonds <- as.data.frame(diamonds)

min.RSS <- function(data,par){
  with(data,sum((diamonds$price - (par[1]*1 + par[2]*diamonds$carat + par[3]*diamonds$depth + 
                       par[4]*diamonds$table + par[5]*diamonds$x + par[6]*diamonds$y + 
                       par[7]*diamonds$z))^2))
}

result <- optim(par=c(1,0.79,61.7,57.4,5.7,5.7,3.5),min.RSS,data=diamonds, method = "BFGS")
print(result)

## Maxima verosimilitud

X <- as.matrix(cbind(diamonds$carat,diamonds$depth,diamonds$table,diamonds$x,diamonds$y,
                         diamonds$z))
y <- diamonds$price

theta<-c(1,0.79,61.7,57.4,5.7,5.7,3.5,1)

ols.lf<-function(theta,y,X){
  n<-nrow(X)
  k<-ncol(X)
  beta<-theta[1:k]
  sigma2<-theta[k+1]
  e<-y-X%*%beta
  logl<- -.5*n*log(2*pi)-.5*n*log(sigma2)-
    ((t(e)%*%e)/(2*sigma2))
  return(-logl)
}

p<-optim(c(1,1,1,1,1,1,1),ols.lf,method="BFGS",y=y,X=X, hessian = T)
print(p)
OI<-solve(p$hessian)
se<-sqrt(diag(OI))




K <- ncol(X)
ols.lf <- function(theta,y, X,K) {
  beta <- theta[1:K]
  sigma <- exp(theta[K+1])
  e <- (y - X%*%beta)/sigma
  logl <- sum(log(dnorm(e)/sigma))
  return(logl)
}

p<-optim(c(1,1,1,1,1,1,1,1),ols.lf,method="BFGS",y=y,X=X,K=K, hessian = T)
print(p)


##################
theta<-c(1,0.79,61.7,57.4,5.7,5.7,3.5,1)

ols.lf <- function(theta, y, X) {
  sum(dnorm(y, mean = X %*% theta[-1], sd = exp(theta[1]), log = TRUE))
}

ols.lf <- function(theta, y, X) {
  sum(dnorm((y - X %*% theta[-1])/exp(theta[1]), log = TRUE))
}

p<-optim(c(1,1,1,1,1,1,1),ols.lf,method="BFGS",y=y,X=X, hessian = T)
print(p)



#PCA
library(FactoMineR)
model <- PCA(X)

#PCA DELTA
summary(delta)

model2 <- PCA(delta[-1])
model2