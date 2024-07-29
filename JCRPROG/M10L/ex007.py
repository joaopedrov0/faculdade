# 7. Escreva uma função recursiva que, dada uma string s e um caractere c, conte o
# número de ocorrências do caractere c na string s.

def repeatCount(s, c, i=-2, occurrences=0):
    if i == -2:
        i = len(s) - 1
    if i > -1:
        if str(s[i]) == str(c):
            occurrences = occurrences + 1
        return repeatCount(s, c, i - 1, occurrences)
    
    return occurrences

print(repeatCount("abacate", "1"))