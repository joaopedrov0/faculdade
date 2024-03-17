#Programa exercicio 4
print("Bem vindo ao programa de calculo de MDC")
a = int(input("Coloque o primeiro numero: "))
#No código acima colocamos os 2 valores que serão utilizados para o calculo do MDC
div_a = 1
div_b = 1
r_a = a / div_a

list_a = [] # Lista do primeiro número
list_b = [] # Lista do segundo número


while div_a <= a:
    div_a = div_a + 1
    if a % div_a == 0:
        print((div_a))
        list_a.append(div_a)

b = int(input("Coloque o segundo numero: "))
r_b = b / div_b

while div_b <= b:
    div_b = div_b + 1
    if b % div_b == 0:
        print((div_b))
        list_b.append(div_b)

print(list_a)
print(list_b)

bigger = 0

for num in list_a:
    print(num)
    if num in list_b:
        print(num)
        bigger = num
        
    
print("O maior divisor comum entre {} e {} é {}".format(a, b, bigger))