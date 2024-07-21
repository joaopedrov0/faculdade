# 6. Escreva uma função que recebe duas matrizes (A e B). Se as duas matrizes tiverem 
# dimensões compatíveis, sua função deve retornar o produto das duas (C = A × B). 
# Caso contrário, sua função deve retornar uma lista vazia. 

def matriz_multiplicacao(A, B):

    if len(A[0]) != len(B):
        return []

    m = len(A)
    p = len(B[0])

    # Inicializar a matriz "zerada"
    res = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(len(B)):
                res[i][j] += A[i][k] * B[k][j]
    
    return res

# Teste
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

print(matriz_multiplicacao(A, B))
