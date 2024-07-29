# 15. Defina uma função recursiva que recebe como argumento uma lista de listas de
# números inteiros w e devolve True se cada lista em w tiver igual número de
# elementos positivos e negativos, e False em caso contrário. Por exemplo, no caso da
# lista [[2,4,-3,-1],[-3,0,7],[-8,6]] a função deve devolver True pois todas as listas têm
# igual número de elementos positivos e negativos

# Observação: A função não deve se importar em calcular a quantidade de neutros (0)

def compairSignalsList(numList, i=-2, negative=0, positive=0):
    if i ==-2:
        i=len(numList) - 1
    if i > -1:
        if numList[i] > 0:
            positive = positive + 1
        if numList[i] < 0:
            negative = negative + 1
        return compairSignalsList(numList, i-1, negative, positive)
    return True if negative == positive else False

def compairSignalsMatrix(w):
    for matrixLine in w:
        if compairSignalsList(matrixLine):
            continue
        return False
    return True


print(compairSignalsMatrix([[2,4,-3,-1],[-3,0,7],[-8,6]]))