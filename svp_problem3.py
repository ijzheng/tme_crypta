import gmpy2
def legendre_symbol(a, p):
    return pow(a, (p - 1) // 2, p)

def tonelli_shanks(n, p):
    Q = p - 1
    S = 0
    while Q % 2 == 0:
        Q //= 2
        S += 1
    if S == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre_symbol(z, p):
            break
    M = S
    c = pow(z, Q, p)
    t = pow(n, Q, p)
    R = pow(n, (Q + 1) // 2, p)
    while t != 1:
        for i in range(1, M):
            if pow(t, 2**i, p) == 1:
                break
        b = pow(c, 2**(M - i - 1), p)
        M = i
        c = pow(b, 2, p)
        t = (t * c) % p
        R = (R * b) % p
    return R

n = mpz('f8b9ba8c81437ec226cfbb5a50fc068666dc6fa3f8d1dfeb6ebb03390c845dcfabd690d787049ebea144973385185bd16be99c0def23ef190438c9bda14f0ee9949de252979661b25c846a76da239713116a7da63528f9f770e63e50189744df783600d82760b1c3f37b6c410155e0b30fe1551a9f50359f24a4937a7ad2617d',16)
# Définir la matrice A
from fpylll import IntegerMatrix, LLL
A = IntegerMatrix(2, 2)
A[0, 0] = int(x)
A[1, 1] = 0
A[0, 1] = 1
A[1,0] = int(n)

# Appliquer l'algorithme LLL pour trouver un vecteur court dans le réseau
A_LLL = LLL.reduction(A)

# Obtenir le vecteur court trouvé
short_vector = A_LLL[0]
print(short_vector)
