# 9. Usando algoritmos recursivos, escreva funções que: 
# a. Defina uma função que recebe como argumento um número natural n e 
# devolva a lista dos n primeiros quadrados perfeitos. 
# b. Defina uma função que recebe como argumento um número natural n e 
# devolva a lista dos quadrados perfeitos até n, por ordem decrescente. 


# a

def nPerfectSquares(n):
    return arrayPerfectSquareConverter(list(range(1, n+1)))

def arrayPerfectSquareConverter(squareList, i=-2):
    if i == -2:
        i = 0
    if i < len(squareList):
        squareList[i] = squareList[i]**2
        arrayPerfectSquareConverter(squareList, i + 1)
    return squareList

print(nPerfectSquares(10))

# b

def perfectSquareUntilN(n, resList=[], i=-2):
    if i == -2:
        i = 1
    if i**2 <= n:
        resList.append(i**2)
        return perfectSquareUntilN(n, resList, i + 1)
    else:
        return resList

print(perfectSquareUntilN(131))