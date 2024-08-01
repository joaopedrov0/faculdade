# 13. Defina uma função recursiva que recebe como argumento uma lista de listas de 
# números inteiros w e devolve True se alguma das listas em w tiver mais números 
# pares do que ímpares e False em caso contrário. Por exemplo, no caso da lista 
# [[2,4,3,1],[3,5,7],[8,1,6]] a função deve devolver True pois a lista [8,1,6] tem mais pares 
# que ímpares. 

def compairOddEvensList(numList, i=-2, odd=0, even=0):
    if i ==-2:
        i=len(numList) - 1
    if i > -1:
        if numList[i] % 2 == 0:
            even = even + 1
        if numList[i] % 2 != 0:
            odd = odd + 1
        return compairOddEvensList(numList, i-1, odd, even)
    return True if even > odd else False

def compairOddEvensMatrix(w):
    for matrixLine in w:
        if not compairOddEvensList(matrixLine):
            continue
        return True
    return False


print(compairOddEvensMatrix([[2,4,3,1],[3,5,7],[8,1,6]]))