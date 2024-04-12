word_without_vowels = ""
user_word = input('Ingresa una palabra: ')
user_word = user_word.upper()
vowels = ['A','E','I','O','U']

for i in user_word:
    if i not in vowels:
        word_without_vowels = word_without_vowels + i

print(word_without_vowels)
