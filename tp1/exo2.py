import numpy as np


A = np.array([[2,1,1], [1,3,2], [1,0,0]])

# I = np.eye(3)

def matrice_Augmente(A):
    I = np.eye(A.shape[0])
    Au = np.concatenate((A, I), axis=1)
    return Au

# print("Matrice Augmentée A: \n", matrice_Augmente(A))

# B = np.array([[2,1],[5,3]])

# print("Matrice Augmentée B: \n", matrice_Augmente(B))

def echanger_lignes(M, i, j):
    M[[i, j]] = M[[j, i]]
    return M

def multiplier_ligne(M, i, k):
    M[i] = k * M[i]
    return M

def soustraire_multiples(M, i, j, k):
    M[i] = M[i] - k * M[j]
    return M
def inverse_gauss_jordan(A):
    n = A.shape[0]
    Au = matrice_Augmente(A)
    
    for i in range(n):
        # Pivoting
        max_row_index = np.argmax(np.abs(Au[i:, i])) + i
        if max_row_index != i:
            Au = echanger_lignes(Au, i, max_row_index)
        
        # Make the diagonal contain all 1's
        Au = multiplier_ligne(Au, i, 1 / Au[i, i])
        
        # Make the other rows contain 0's in the current column
        for j in range(n):
            if j != i:
                Au = soustraire_multiples(Au, j, i, Au[j, i])
    
    return Au[:, n:]  


