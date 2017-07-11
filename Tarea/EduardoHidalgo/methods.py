def zeros(nrow, ncol):
    
    """
    This method creates a matrix of zeros, given number of rows
    and columns.
    """
    
    from itertools import repeat

    list_of_rows = []

    for i in range(nrow):
        
        row = []
        
        row.extend(repeat(0, ncol))
        list_of_rows.append(row)

    matrix = Array(list_of_rows)
    
    return matrix

def eye(nrow):
    
    """ 
    This method creates an identity matrix.
    """
    
    zeros_matrix = zeros(nrow,nrow)
    
    for i in range(nrow):
        
        zeros_matrix[i,i] = 1
        
    eye_matrix = zeros_matrix
        
    return eye_matrix
        
    
    
    