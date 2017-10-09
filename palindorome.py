
def palindrome(word):
    if(word == word[::-1]):
        return True
    else:
        return False


if __name__ == ('__main__'):
    word = str(input('Ingrese una palabra: '))
    result = palindrome(word)
    if(result):
        print('La palabra {} es palindrome'.format(word))
    else:
        print('la palabra {} no es palindrome'.format(word))
