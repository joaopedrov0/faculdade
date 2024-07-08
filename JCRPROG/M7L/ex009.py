# 9. Escreva um programa que lê duas notas de vários alunos e armazena tais notas em 
# um dicionário, onde a chave é o nome do aluno. A entrada de dados deve terminar 
# quando for lida uma string vazia como nome. Seu programa deve também calcular a 
# média do aluno e exibir o nome e a média do aluno de maior média.

alunos = {}

melhorAluno = "Ninguém"
melhorMedia = 0

while True:
    
    nome = str(input("Digite o nome do aluno: \n"))

    if (nome == "" or nome == " "):
        break

    nota1 = float(input("Digite a primeira nota do aluno: \n"))
    nota2 = float(input("Digite a segunda nota do aluno: \n"))

    if (nota1 + nota2)/2 > melhorMedia:
        melhorMedia = (nota1 + nota2)/2
        melhorAluno = nome

    alunos[nome] = [nota1, nota2]

print("A maior média foi {}, de {}".format(melhorMedia, melhorAluno))