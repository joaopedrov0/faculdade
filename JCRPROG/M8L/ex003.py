# 3. Escreva um programa com uma função que, dado um número inteiro (n > 1), retorne 
# uma lista com os fatores primos de n. 

# Encontrar os números primos que, quando multiplicados, resultam no número digitado.

def fatores_primos(n):
    fatores = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            fatores.append(divisor)
            n //= divisor
        divisor += 1
    return fatores

numero = int(input("Digite um número inteiro maior que 1: "))
print("Os fatores primos de {} são: {}".format(numero, fatores_primos(numero)))