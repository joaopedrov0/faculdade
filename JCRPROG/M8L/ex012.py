# 12. O valor aproximado de   pode ser calculado a partir da série: 𝜋=4
#  1
#  −4
#  3
#  +4
#  5
#  −4
#  7
#  +⋯ 
# Escreva uma função que calcule o valor de , com precisão dada como parâmetro. 

def calcular_pi(precisao):
    pi = 0
    termo = 1
    i = 0

    while abs(termo) > precisao:
        termo = 4 * ((-1) ** i) / (2 * i + 1)
        pi += termo
        i += 1

        # print(i)
        # print(termo)
        # print(pi)

    return pi

# Teste
precisao = float(input("Digite a precisão desejada: "))
pi = calcular_pi(precisao)
print(f"Valor de π calculado com precisão {precisao}: {pi}")

