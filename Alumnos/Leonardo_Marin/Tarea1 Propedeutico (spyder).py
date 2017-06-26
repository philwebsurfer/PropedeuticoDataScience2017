# -*- coding: utf-8 -*-
"""
Editor de Spyder

"""


"""        CREAR UN SISTEMA DE ÁLGEBRA LINEAL        """




"""    Comenzando desde cero...    """

class Array:
    "Una clase minima para algebra lineal"    
    def __init__(self, list_of_rows): 
        "Constructor y validador"
        # obtener dimensiones
        self.data = list_of_rows
        nrow = len(list_of_rows)
        #  ___caso vector: redimensionar correctamente
        if not isinstance(list_of_rows[0], list):
            nrow = 1
            self.data = [[x] for x in list_of_rows]
        # ahora las columnas deben estar bien aunque sea un vector
        ncol = len(self.data[0])
        self.shape = (nrow, ncol)
        # validar tamano correcto de filas
        if any([len(r) != ncol for r in self.data]):
            raise Exception("Las filas deben ser del mismo tamano")

     
    def __repr__(self):
        return "Matriz (" + str(self.data) + ")"
    
    def __str__(self):
        return str(self.data)

    def __getitem__(self, idx):
        return self.data[idx[0]][idx[1]]
    
    def __setitem__(self, idx, new_value):
        self.data[idx[0]][idx[1]] = new_value
        
        
        
# Funciones        
        
    def zeros(shape):    
        return [[0 for j in range(shape[0])] for i in range(shape[1])]
        
    def eye(shape):  
        mat = [[0 if i != j else 1 for j in range(shape[0])] for i in range(shape[0])]
        return(mat)
        
    

    def __add__(self, other):
        "Hora de sumar"
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise Exception("Las dimensiones son distintas!")
            rows, cols = self.shape
            newArray = Array([[0. for c in range(cols)] for r in range(rows)])
            for r in range(rows):
                for c in range(cols):
                    newArray.data[r][c] = self.data[r][c] + other.data[r][c]
            return newArray
        elif isinstance(2, (int, float, complex)): # en caso de que el lado derecho sea solo un numero
            rows, cols = self.shape
            newArray = Array([[0. for c in range(cols)] for r in range(rows)])
            for r in range(rows):
                for c in range(cols):
                    newArray.data[r][c] = self.data[r][c] + other
            return newArray
        else:
            return NotImplemented # es un tipo de error particular usado en estos metodos


    def __radd__(self, other):
        "Hora de sumar"
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise Exception("Las dimensiones son distintas!")
            rows, cols = self.shape
            newArray = Array([[0. for c in range(cols)] for r in range(rows)])
            for r in range(rows):
                for c in range(cols):
                    newArray.data[r][c] = self.data[r][c] + other.data[r][c]
            return newArray
        elif isinstance(2, (int, float, complex)): # en caso de que el lado derecho sea solo un numero
            rows, cols = self.shape
            newArray = Array([[0. for c in range(cols)] for r in range(rows)])
            for r in range(rows):
                for c in range(cols):
                    newArray.data[r][c] = other +  self.data[r][c]
            return newArray
        else:
            return NotImplemented # es un tipo de error particular usado en estos metodos


    def __sub__(self, other):
        "Hora de restar"
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise Exception("Las dimensiones son distintas!")
            rows, cols = self.shape
            newArray = Array([[0. for c in range(cols)] for r in range(rows)])
            for r in range(rows):
                for c in range(cols):
                    newArray.data[r][c] = self.data[r][c] - other.data[r][c]
            return newArray
        elif isinstance(2, (int, float, complex)): # en caso de que el lado derecho sea solo un numero
            rows, cols = self.shape
            newArray = Array([[0. for c in range(cols)] for r in range(rows)])
            for r in range(rows):
                for c in range(cols):
                    newArray.data[r][c] = self.data[r][c] + other
            return newArray
        else:
            return NotImplemented # es un tipo de error particular usado en estos metodos


    def __transpuesta__(self):
        rows, cols = self.shape
        TArray = Array([[0. for r in range(rows)] for c in range(cols)])
        for c in range(cols):
            for r in range(rows):
                 TArray.data[c][r] = self.data[r][c] 
        return TArray
        



    def __mult__(self, other):
        "Hora de Multiplicar"
        if isinstance(other, Array):
            if self.shape[1] != other.shape[0]:
                raise Exception("Las dimensiones no son consistentes para realizar la multiplicación!")
            rows1, cols1 = self.shape
            rows2, cols2 = other.shape
            multArray = Array([[0. for c in range(cols2)] for r in range(rows1)])
            for r in range(rows1):
                #suma=int(0)
                for c in range(cols2):
                    for k in range(rows2):                    
                        #suma=suma + self.data[r][k] * other.data[k][c]
                        #multArray.data[r][c] = suma
                        multArray.data[r][c] += self.data[r][k] * other.data[k][c]
            return multArray
       


    def __rmult__(self,other):
        rows, cols = self.shape
        rmultArray = Array([[0. for c in range(cols)] for r in range(rows)])
        for r in range(rows):
            for c in range(cols):
                 rmultArray.data[r][c] = self.data[r][c] * other
        return rmultArray










## Ejemplos


## Crear Matrices    
Array([1,2,3])
## Validar que las columnas deban tener la misma longitud
Array([[1,2,3], [4,5]])

## Declarar MAtrices
A = Array([[1,2,3], [4,5,0]])
A
#Imprimir un objeto
print(A)


## Nota, Recordatorio de campo escondido
A.__dict__ # el campo escondido __dict__ permite acceder a las propiedades de clase de un objeto



# Acceder a elementos de un objeto por medio de indices
A[0,0]
print(A)

## Asignar valores especificos a un objeto por medio de indices
A[0,0] = 99
print(A)


## Iniciar una matriz de ceros
Array.zeros([2,7])

## Crear una matriz identidad
Array.eye([5,5])


###################################
## Transpuesta de una matriz
A = Array([[1,2,3], [4,5,0]])
print(A)
Array.__transpuesta__(A)



###################################
## Suma de matrices y escalares

## Suma de matrices
A+A

#Suma de escalares
A+1     ## suma por la derecha
1+A     ##suma por la izquierda

# Resta de matrices
A-A


## Multiplicación de matrices
A = Array([[1,0,0],[0,1,0]])
B = Array([[1,0],[2,0],[0,1]])
C = Array([[1,0],[2,0]])

print(A)
print(B)
print(C)


## Multiplicación valida
Array.__mult__(A,B)

## Validación de una multiplicación no valida
Array.__mult__(A,C)



## Multiplicacón de una matriz por un escalar
D = Array([[1,2,3],[-1,-2,0-3]])
print(D)

Array.__rmult__(D,2)







