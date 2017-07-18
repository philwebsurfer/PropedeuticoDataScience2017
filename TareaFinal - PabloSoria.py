# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 11:29:22 2017

@author: Pablo.Soria
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 18:30:53 2017

@author: Pablo.Soria
"""
class Array(object):
    " Mi entorno de algebra lineal Pablo Soria Garcia "
    def __init__(self,lista):
         self.d = lista
         self.typ = type(lista[0])
         if (self.typ == list):
             self.typ = 1 #Es una matriz
             self.m=len(self.d)
             self.n=len(self.d[0])
         else:
             self.typ = 0 #Es un vector
             self.d = [[x] for x in lista]
             self.m=len(lista)
             self.n = 1  
       #Es necesario poner este método ya que se usa en la suma y de lo contrario no reconce el comando len(other) para verificar las dimensiones
    def __len__(self):
        return len(self.d)   
    def __setitem__(self,key,value):
        self.d[key]=value
# 1. Un metodo para imprimir una matriz de forma mas agradable
    def __str__(self):
        self.val()
        if self.typ == 0:
            # Es vector, dentro de un print() incluimos una lista comp. que va valor por valor en el vector, el.formt(value) es para que el join lo lea como str y lo concatene a un salto de línea \n, el parámetro {:1} nos desplaza hacia la derecha cada línea de impresión, finalmente para que el __str__ no mande error lo retornamos como un string con str()
          return str(print('\n'.join(['{:1}'.format(value) for value in self.d])))
        else:
            #Es prácticamente lo mismo que el vector pero se usa una lista comp anidada, esta l.comp va primero valor a valor en cada row y luego row por row en self.d, esto es contraintuitivo por que generalmente las listas.comp anidadas se se declara primero el loop externo y luego el interno esto se debe a que estamos usando primero el una l.comp dentro del print. Se usan dos .join() el primero hace el salto de línea y el segundo añade un espacio entre cada impresión de valores
          return str(print('\n'.join([' '.join(['{:1}'.format(value) for value in row]) for row in self.d])))
   
    def __repr__(self): #Hace exactamente lo mismo que __str__ pero funciona cuando no le ponemos print()
        self.val()
        if self.typ == 0:
          return print('\n'.join(['{:1}'.format(value) for value in self.d]))
        else:
          return print('\n'.join([' '.join(['{:1}'.format(value) for value in row]) for row in self.d]))     
# 2. Validador. Un metodo para validar que la lista de listas sea valida (columnas del mismo tamano y que las listas interiores sean numericas  
    def val(self):
        #Si es vector:
        if self.typ == 0:           
            count = sum(1 for num in self.d if type(num) == float or type(num) == int)
            if count != self.m:
                print("Verifica los argumentos")
            else:
                print("Dimensiones: OK, Argumentos: OK")
        #Si es matriz:
        else:
            count = sum(1 for row in self.d for num in row if type(num) == float or type(num)==int)
            if count != self.m*self.n:
                print("Verifica los argumentos")
            else:
                print("Dimensiones: OK, Argumentos: OK")
# 3. Indexing Hacer sentido a expresiones A[i,j]
    def __getitem__(self,ind):
        #Usamos el validador primero
        print("el indice es", ind)
        self.val()
        if self.typ == 1:#caso matricial
            return self.d[ind[0]][ind[1]]
        else:#caso vectorial
            return self.d[ind[0]]     
# 4. Iniciar matriz vacia de ceros Este metodos es muy util para preacolar espacio para guardar nuevas matrices ---- Done  
    def zeros(self):        
        if self.typ == 1:#Caso Matricial
            M = [[0 for i in range(self.n)] for j in range(self.m)]
        else:#Caso vectorial
            M = [0 for i in range(self.m)]
        return Array(M)
# 5. Transposicion B.transpose()
    def trans(self):
        #con una doble lista comp. que pasa por cada columna y luego por cada valor del renglo re asignamos el 
        a=[[self.d[i][j] for i in range(self.m)] for j in range(self.n)]
        self.d=a
        return self.__str__()
# 6. Suma A + B y resta A - B
    def __add__(self,other):       
        if (type(other) == int) or (type(other) == float): #Caso suma escalar
            c = [self.d[j] + other for j in range(self.m)]
            return Array(c)
        else:            
            if len(other) == self.m:#Caso suma de matrices
                c = [[self.d[i][j] + other.d[i][j] for j in range(self.n)] for i in range(self.m)]
                return Array(c)
            else:
                print("Las dimensiones no coinciden, la resta no fue ejecutada")               

    def __sub__(self,other):
        if (type(other) == int) or (type(other) == float): #Caso suma escalar
            c = [self.d[j] - other for j in range(self.m)]
            return self.__str__()
        else:            
            if len(other) == self.m:#Caso suma de matrices
                c = [[self.d[i][j] - other.d[i][j] for j in range(self.n)] for i in range(self.m)]
                return Array(c)
            else:
                print("Las dimensiones no coinciden, la resta no fue ejecutada")      
# 7. Multiplicacion escalar y matricial 2 A y AB
    def __mul__(self, other):
         if (type(other) == int ) or (type(other) == float ):
             c = [[self.d[i][j]*other for j in range(self.n)] for i in range(self.m)]
             return Array(c)
         else:
             c = [[sum([self.d[i][k]*other.d[k][j]for k in range(self.n)]) for j in range(self.m)] for i in range(self.n)]
             return Array(c)
         
    def __truediv__(self,other):
        if (type(other) == int ) or (type(other) == float ):
             c = [[self.d[i][j]/other for j in range(self.n)] for i in range(self.m)]
             return Array(c)
        else:
            c = [[sum([self.d[i][k]/other.d[k][j]for k in range(self.n)]) for j in range(self.m)] for i in range(self.n)]
            return Array(c)            
# 7. Forward_subs con Lx = b
    def pdot(x,y):
            n=len(x)
            b=len(y)
            if b == n:
              for i in range(b):
                 new = sum([x[i]*y[i] for i in range(n)])
            return new
    def fwdsub(self,b):
        #Vamos a validar que sea una L correcta
        if self.m == self.n:
            ones = sum([ 1 for i in range(self.m) if self.d[i][i] == 1]) # verifica la diagonal que todos sean 1's
            ceros = sum([self.d[i][j] for i in range(self.m) for j in range(self.n) if j > i]) # verifica los valores arriba de la diagonal j > i que sean ceros
            if (self.n - ceros == self.n) and (self.m == ones):
                    y = [0 for i in range(self.n)] #Creamos un vector de respuestas:
                    y[0] = b[0]# Asignamos el primer valor directamente
                    for i in range(0,self.n):
                        y[i]=b[i]-sum([self.d[i][j]*y[j] for j in range(i)])
                    return Array(y)                                                                                            
            else:
                print("la matriz insertada no es una L, por favor verifica")        
        else:
            print("Este algoritmo solo funciona para matrices invertibles")           
# 8. backrward_subs con Lx = b
    def baksub(self,b):
        #Vamos a validar que sea una U correcta      
        if self.m == self.n:
            ceros = sum([self.d[i][j] for i in range(self.m) for j in range(self.n) if i > j]) # verifica los valores arriba de la diagonal j > i que sean ceros
            if (ceros == 0) or (ceros == 0.0) :                
                    y = [0 for i in range(self.n)] #Creamos un vector de respuestas:
                    y[self.n-1] = b[self.n-1]/self.d[self.n-1][self.n-1] # Asignamos el ultimo valor de forma directa                               
                    for i in range(self.n-2,-1,-1):
                        y[i] = (b[i]-sum([self.d[i][j]*y[j] for j in range(self.n-1,i,-1)]))/self.d[i][i]
                    return Array(y)                  
            else:
                print("la matriz insertada no es una U, por favor verifica")
        else:
            print("Este algoritmo solo funciona para matrices invertibles")
# 9. Desc. LU
            
    def lu(self):
        u = self.d     
        l = [[1,0,0],[0,1,0],[0,0,1]]
        if self.n == self.m:
            for k in range(0,self.n):
                for r in range(0,self.n):
                    if k<r:
                        mult = self.d[r][k]/self.d[k][k]
                        l[r][k] = mult
                        for c in range(0,self.n):
                            u[r][c]=self.d[r][c]-(mult*self.d[k][c])                              
            return (Array(l),Array(u))
        else:
            print("Este algoritmo solo funciona para matrices invertibles")
        

# 10. Resolver Ax = b 

    def solve(self,b):
        l,u = self.lu()
        y=l.baksub(b)
        x=u.fwdsub(y)
        return x
        

x=Array([[3,2,1],[11,7,5],[19,17,13]])
l,u = x.lu()
print(l)
print(u)
z=x.solve([0,0,1])

print(z)








            
            
            
        
        
        
    
    
    