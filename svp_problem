from fpylll import IntegerMatrix, LLL

# Définir les paramètres n, p, a et L
n = 7  # dimension
p = int("0x372bb4e2c6ba2d5a", 16) # valeur p
a = int("0x225f565888c685fb", 16)  # valeur a
L = 2**54.37  # borne supérieure L

# Définir la matrice A
A = IntegerMatrix(n, n)
A[0, 0] = 1
for i in range(1, n):
    A[i, i] = p
    A[0, i] = pow(a, i, p)

# Appliquer l'algorithme LLL pour trouver un vecteur court dans le réseau
A_LLL = LLL.reduction(A)

# Obtenir le vecteur court trouvé
short_vector = A_LLL[0]

# Vérifier si la norme du vecteur est inférieure à L
norm_short_vector = short_vector.norm()
if norm_short_vector < L:
    print("Le vecteur court trouvé est :", short_vector)
    print("La norme du vecteur trouvé est :", norm_short_vector)
else:
    print("Aucun vecteur court trouvé avec une norme inférieure à L.")
