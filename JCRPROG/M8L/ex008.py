# 8. Escreva uma função (FparaC) que receba uma temperatura em graus F e retorne a 
# temperatura em graus C, sendo: ) 32 ( 9
#  5 − = F C . A seguir, faça um programa que, em 
# loop, leia um valor para F da entrada padrão e o imprima o valor de C correspondente, 
# utilizando a função FparaC. 

def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    return celsius

while True:
    f = input("Digite a temperatura em Fahrenheit ('Enter' sem entrada para encerrar o programa): ")
    if (f == ""):
        break
    else:
        f = float(f)
    celsius = f_to_c(f)
    print(f"{f}°F é igual a {celsius:.2f}°C")
print("=== Programa encerrado ===")

# Obs: Usando try - except daria para fazer um tratamento da entrada de forma simples e eficáz.