def zamiana_liter(stringInput):
    new_word = []
    for i in stringInput:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        #check which letter is "i" in english alphabet
        order_in_english_alphabet = alphabet.index(stringInput[i])
        #replace it with the next letter
        next_letter = alphabet[(order_in_english_alphabet + 1)]
        new_word.append(next_letter)
    return ''.join(result)
input_word = input("Enter a word: ")
new_word = zamiana_liter(input_word)
print(new_word)
