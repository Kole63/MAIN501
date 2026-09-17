import numpy as np 

# 1- Definissons les matrices A,B,C,D
A = np.array([[7,0],[-1,5],[-1,2]])
B = np.array([[-1,4],[-4,0]])
C = np.array([[7],[3]])
D = np.array([[8,2]])
# 2- calculons les produits matriciels AB, AC, AD, BA, BC, BD, CA, CB, CD, DA, DB, DC

AB = np.dot(A,B)
AC = np.dot(A,C)
# AD = np.dot(A,D)
# BA = np.dot(B,A)
BC = np.dot(B,C)
# BD = np.dot(B,D)
# CA = np.dot(C,A)
# CB = np.dot(C,B)
CD = np.dot(C,D)
# DA = np.dot(D,A)
DB = np.dot(D,B)
DC = np.dot(D,C)


print("AB = \n", AB)
print("AC = \n", AC)
# print("AD = \n", AD) #la où c'est marquer # ce n'est pas possible de faire le produit car le nombre de colones est différent du nombre de lignes
# print("BA = \n", BA)
print("BC = \n", BC)
# print("BD = \n", BD)
# print("CA = \n", CA)
# print("CB = \n", CB)
print("CD = \n", CD)
# print("DA = \n", DA)
print("DB = \n", DB)
print("DC = \n", DC)

# 3- Affichons le resultat des commandes np.ones et np.eye pour les matrices de tailles (3,1), (1,3), (3), (3,3) et (3,2)
r1 = np.ones((3,1))
r2 = np.ones((1,3))
r3 = np.ones((3))
r4 = np.eye(3)
r5 = np.eye(3,2)

print("Ones((3,1)) : r1 = \n", r1)
print("Ones((1,3)) : r2 = \n", r2)
print("Ones((3)) : r3 = \n", r3)
print("Eye(3) : r4 = \n", r4)
print("Eye(3,2) : r5 = \n", r5)
# 4- Definissons de la façon la plus simple les vecteurs v1, v2, v3, v4, v5 et la matrice R
v1 = np.arange(1,17)
print("v1 = \n", v1)

v2 = np.arange(28,10,-2)
print("v2 = \n", v2)


v3 = np.array([2**i for i in range(9)])
print("v3 = \n", v3)

v4 = np.array([3**i for i in range(9)]) 
v5 = np.array([5**i for i in range(9)])
R = np.array([v3,v4,v5])

print("La matrice R = \n", R)


# # 5- Ecrire un code (en 2 lignes) qui crée une matrice de taille 5 × 5 dont les coefficients aléatoires
# sont compris entre 0. et 1., et la normaliser telle que la somme des valeurs absolues de ces éléments
# est égale à 1.

M = np.random.random_sample((5,5))
M_normalized = M / np.sum(np.abs(M))
M = M_normalized
print("Matrice aléatoire M = \n", M)

# 6- Ecrire une fonction qui renvoie la transpodée d'une matice sans utiliser la fonction np.transpose. La fonction doit prendre en argument une matrice M et renvoyer sa transposée.

def transpose(M):
    rows, cols = M.shape
    transposed = np.zeros((cols, rows))
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = M[i][j]
    return transposed

tranpose_B= transpose(B)
print("Transposée de B = \n", tranpose_B)


