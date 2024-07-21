# 4. Implemente um programa com uma função para calcular o número de combinações 
# possíveis de m elementos em grupos de n elementos (n ≤ m), dado pela fórmula de 
# combinação: 
# �
# �!
#  (𝑚−𝑛)!𝑛!

# Combinações onde a ORDEM NÃO IMPORTA e com ESPAÇO AMOSTRAL LIMITADO

def fatorial(num):
    if num == 0 or num == 1:
        return 1
    resultado = 1
    for i in range(2, num + 1):
        resultado *= i
    return resultado

def combinacoes(m, n):
    return fatorial(m) // (fatorial(n) * fatorial(m - n))

# Exemplo de uso
m = int(input("Digite a quantidade de elementos do conjunto que você deseja analisar (conjunto inteiro): "))

while True:
    n = int(input("Digite o tamanho das combinações que você deseja analisar (deve ser maior do que o conjunto inteiro):    "))

print("O número de combinações possíveis de {} elementos em grupos de {} elementos é: {}".format(m, n, combinacoes(m, n)))
