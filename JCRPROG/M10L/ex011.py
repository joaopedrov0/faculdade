# 11. Defina uma função recursiva que recebe como argumento uma lista de listas de
# números inteiros w e devolve o número de elementos pares que existem nas
# sublistas de w. Por exemplo, no caso da lista [[2,4,3,1],[3,5,7],[],[8,0,6]] a função deve
# devolver 5.

def countPairInMatrix(matrix, i=-2, pairCount=0):
    if i==-2:
        matrix = simplifyMatrix(matrix)
        i=len(matrix) - 1
    if i >= 0:
        if matrix[i] % 2 == 0:
            pairCount = pairCount + 1
        return countPairInMatrix(matrix, i - 1, pairCount)
    return pairCount 

def simplifyMatrix(m, i=-2, res=[]):
    if i==-2:
        i = len(m) - 1
    if i>=0:
        res = [*res, *m[i]]
        return simplifyMatrix(m, i-1, res)
    return res

# print(simplifyMatrix([[1,2,3],[4,5,6],[7,8,9]]))

print(countPairInMatrix([[2, 3, 4, 1], [3, 5, 7], [], [8, 0, 6]]))