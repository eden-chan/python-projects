import pandas
#TODO 1. Create a dictionary in this format:
nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_alphabet_dict = {row.letter: row.code for (index, row) in nato_phonetic_alphabet.iterrows()}
print(nato_phonetic_alphabet_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic(word):
    letters = list(word)
    try:
        phonetic_code = [nato_phonetic_alphabet_dict[letter] for letter in letters]
    except KeyError:
        print("Alphabet letters only! Try again.")
    else:
        print(f"Your word in phonetic code is {phonetic_code}")

while True:
    word = input("Enter a word. Enter the word 'quit' to exit the program.\n").upper()
    if word == 'QUIT':
        print("Exitting program!")
        break
    else:
        generate_phonetic(word)
