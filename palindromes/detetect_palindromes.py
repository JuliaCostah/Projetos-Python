import math

def is_polindrome(word):
    j = len(word) - 1 # pega a posição da última letra
    result = 0
    
    for i in range(len(word)):
        if word[i] == word[j]:
            result += 1
        
        if i >= j:
            break
        j -= 1
        
    if result == math.ceil(len(word)/2):
        return 'A palavra é palíndroma.'
    else:
        return 'A palavra não é palíndroma.'

word = input('Palavra: ')
result = is_polindrome(word)
print(result)