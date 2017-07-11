class Array:
    "Una clase minima para algebra lineal"    
    def __init__(self, list_of_rows): 
        "Constructor"
        self.data = list_of_rows
        nrow = len(list_of_rows)
        
        #Para el caso que sea un vector
        if not isinstance(list_of_rows[0], list):
            self.data = [[x] for x in list_of_rows]
            
        # ahora las columnas deben estar bien aunque sea un vector
        self.shape = (len(list_of_rows), len(self.data[0]))
        
        if any([len(r) != len(self.data[0]) for r in self.data]):
            raise Exception("Las filas deben ser del mismo tamano")
        
    def __repr__(self):
        
        n = len(self.data)  
        str_rep = '#'* 20 + '\n\nYo soy la matriz:\n\n'
        for i in range(n):  
            str_rep += str(self.data[i]) + '\n'
        str_rep +='\n' + '#'*20
        
        return str_rep
    
    def __str__(self):
        
        n = len(self.data)  
        str_rep = '#'* 20 + '\n\nYo soy la matriz:\n\n'
        for i in range(n):  
            str_rep += str(self.data[i]) + '\n'
        str_rep +='\n' + '#'*20
        
        return str_rep
    
    def __getitem__(self, idx):
        return self.data[idx[0]][idx[1]]
    
    def __setitem__(self, idx, new_value):
        
        self.data[idx[0]][idx[1]] = new_value
        
        return self.data[idx[0]][idx[1]]
    
    def transpose(self):
        """
        Return the transpose matrix.
        """
        

        matrix_t = zeros(self.shape[1], self.shape[0])



        for i in range(self.shape[1]):

            for j in range(self.shape[0]):

                matrix_t[i,j] = self[j,i] 

        return matrix_t
    
    def __add__(self, other):
        """
        
        sum of matrixes
        
        """
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise Exception("Las dimensiones son distintas!")
            rows, cols = self.shape
            newArray = Array([[0. for c in range(cols)] for r in range(rows)])
            for r in range(rows):
                for c in range(cols):
                    newArray.data[r][c] = self.data[r][c] + other.data[r][c]
            return newArray
        elif isinstance(other, (int, float, complex)): # en caso de que el lado derecho sea solo un numero
            rows, cols = self.shape
            newArray = Array([[0. for c in range(cols)] for r in range(rows)])
            for r in range(rows):
                for c in range(cols):
                    newArray.data[r][c] = self.data[r][c] + other
            return newArray
        else:
            return NotImplemented
        
    def __radd__(self, other):
            
        rows, cols = self.shape
        matrix = zeros(rows,cols)
            
        if isinstance(other, (int,float,complex)):
            for i in range(rows):
                for j in range(cols):
                    matrix[i,j] = self[i,j] + other

            return matrix
        else:
            return NotImplemented

    def __sub__(self, other):
            """

            substraction of matrixes

            """
            if isinstance(other, Array):
                if self.shape != other.shape:
                    raise Exception("Las dimensiones son distintas!")
                rows, cols = self.shape
                newArray = Array([[0. for c in range(cols)] for r in range(rows)])
                for r in range(rows):
                    for c in range(cols):
                        newArray.data[r][c] = self.data[r][c] - other.data[r][c]
                return newArray
            elif isinstance(other, (int, float, complex)): # en caso de que el lado derecho sea solo un numero
                rows, cols = self.shape
                newArray = Array([[0. for c in range(cols)] for r in range(rows)])
                for r in range(rows):
                    for c in range(cols):
                        newArray.data[r][c] = self.data[r][c] - other
                return newArray
            else:
                return NotImplemented
            
    def __mul__(self, other):
        """
        
        multiplication of matrixes
        
        """
        if isinstance(other, Array):
            if self.shape[1] != other.shape[0]:
                raise Exception("""Número de Columnas de la primera es distinta de \n
                        el número de filas de la segunda""")
            rows, cols = self.shape[0], other.shape[1]
            newArray = zeros(rows,cols)
            ma2_t = ma2.transpose()
            
            for r in range(rows):
                for c in range(cols):
                    
                    mult_sum = 0
                    for i in range(self.shape[1]):
                        mult_sum += ma1[r,:][i] * ma2_t[c,:][i] 
                        newArray[r,c] = mult_sum
        
            return newArray
        elif isinstance(other, (int, float, complex)): # en caso de que el lado derecho sea solo un numero
            rows, cols = self.shape
            newArray = zeros(rows,cols)
            for r in range(rows):
                for c in range(cols):
                    newArray.data[r][c] = self.data[r][c] * other
            return newArray
        else:
            return NotImplemented
        
    def __rmul__(self, other):
            
        if isinstance(other, (int, float, complex)):

            rows, cols = self.shape
            newArray = zeros(rows,cols)
        for r in range(rows):
            for c in range(cols):
                newArray.data[r][c] = self.data[r][c] * other
            return newArray
        else:
            return NotImplemented