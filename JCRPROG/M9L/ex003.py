# 3. Escreva uma função que imprime, linha a linha, os valores de uma matriz 
# bidimensional dada como argumento. 

def renderMatrix(matrix):
    for i in range(len(matrix)):
        line = ""
        for j in range(len(matrix[i])):
            line += str(matrix[i][j]) + " "
        print(line)

# Teste 
m = [
    [1, 2, 3, 4],
    [2, 2, 3, 5],
    [3, 3, 3, 4],
    [4, 5, 4, 4]
]

renderMatrix(m)