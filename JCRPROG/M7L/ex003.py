# 3. Faça um programa que conta quantos caracteres únicos existem em uma string. A 
# string 'Hello, world!' tem dez caracteres únicos, enquanto a string 'zzz' tem apenas 
# um. Utilize um dicionário para resolver esse problema.

texto = str(input("Digite um texto para verificar a quantidade de caractéres únicos: "))

splitedText = list(texto)

charList = []

for char in splitedText:
    if (char in charList):
        continue
    else:
        charList.append(char)

print("O texto digitado tem {} caracteres únicos".format(len(charList)))