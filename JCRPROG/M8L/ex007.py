# 7. Crie um programa que implemente e teste uma função que, dadas duas listas 
# representando dois conjuntos: 
# a. Retorne uma lista que represente a união dos dois conjuntos. 
# b. Retorne uma lista que represente a interseção dos dois conjuntos. 
# c. Retorne uma lista que represente a diferença entre os dois conjuntos. 
# d. Verifique se o primeiro é um subconjunto do segundo.

def uniao(conjunto1, conjunto2):
    resultado = []
    elementos = {}
    
    for item in conjunto1:
        if item not in elementos:
            elementos[item] = True
            resultado.append(item)
    
    for item in conjunto2:
        if item not in elementos:
            elementos[item] = True
            resultado.append(item)
    
    return resultado

def intersecao(conjunto1, conjunto2):
    resultado = []
    elementos = {}
    
    for item in conjunto1:
        elementos[item] = True
    
    for item in conjunto2:
        if item in elementos:
            resultado.append(item)
    
    return resultado

def diferenca(conjunto1, conjunto2):
    resultado = []
    elementos = {}
    
    for item in conjunto2:
        elementos[item] = True
    
    for item in conjunto1:
        if item not in elementos:
            resultado.append(item)
    
    return resultado

def eh_subconjunto(conjunto1, conjunto2):
    elementos = {}
    
    for item in conjunto2:
        elementos[item] = True
    
    for item in conjunto1:
        if item not in elementos:
            return False
    
    return True

# Testes
conjunto1 = [1, 2, 3, 4]
conjunto2 = [3, 4, 5, 6]

print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)
print("União:", uniao(conjunto1, conjunto2))
print("Interseção:", intersecao(conjunto1, conjunto2))
print("Diferença (conjunto1 - conjunto2):", diferenca(conjunto1, conjunto2))
print("Conjunto 1 é subconjunto do Conjunto 2?", eh_subconjunto(conjunto1, conjunto2))
