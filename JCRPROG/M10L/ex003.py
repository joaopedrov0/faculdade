# 3. Usando algoritmos recursivos, escreva funções que:
# a. Calcule o produtório de um número m, n vezes.
# b. Calcule a potência n de um número k.
# c. Some os dígitos de um número inteiro não negativo.
# d. Calcule a média dos dígitos de um número inteiro não negativo.

# a
def produtorio(m, n, res=1):
    if n > 0:
        res = res * m
        return produtorio(m, n - 1, res)
    return res

# print(produtorio(3, 3))

# b
def pow(k, n, res=1):
    if n > 0:
        res = res * k
        return pow(k, n - 1, res)
    return res

# ! Esse código é semelhante ao do produtório pois quando se é calculado o produtório de uma constante, o resultado é exatamente o mesmo de calcular a potência desse mesmo número, sendo expoente a quantidade de vezes que o produtório fará essa multiplicação

# c
def absoluteSum(n):
    return sumList(list(str(n)))

def sumList(numList, i=-2, res=0):
    if i == -2:
        i = len(numList)-1
    if i < 0:
        return res
    res = res + int(numList[i])
    return sumList(numList, i-1, res)

# print(absoluteSum(324232))

# d
def digitMedia(n):
    return absoluteSum(n)/len(list(str(n)))

print(digitMedia(345))