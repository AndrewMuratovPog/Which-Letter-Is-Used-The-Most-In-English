# https://www.mit.edu/~ecprice/wordlist.10000

with open("Wordlist.txt", "r") as word_list:
    list_of_words = [word.strip("\n") for word in word_list.readlines()]

dict_of_letters = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0
}

max_use_of_letter = 0
max_letter = ""

for word in list_of_words:
    for letter in word:
        dict_of_letters[letter] += 1  
        if dict_of_letters[letter] > max_use_of_letter:
            max_use_of_letter = dict_of_letters[letter]
            max_letter = letter

print(dict_of_letters)
print(max_use_of_letter)
print(max_letter)
