import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {}
for (index, row) in df.iterrows():
    letter = row.letter
    code = row.code
    new_dict[letter] = code

user_input = input("Enter a word: ").upper()
list_if_letters = list(user_input)

a_list = []
for item in list_if_letters:
    corr_letter = new_dict[item]
    a_list.append(corr_letter)

print(a_list)
# TODO 1. Create a dictionary in this format: '/
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
