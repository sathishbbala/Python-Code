import pandas

def generate_phonetic():
    word = input("Enter a word:  ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word] # List comprehension - looksup for the code for each letter
    except KeyError:
        print("Sorry only Alphabets are allowed")
        generate_phonetic()
    else:
        print(output_list)

data = pandas.read_csv("nato_phonetic_alphabet.csv")   # print(type(data)) # class 'pandas.core.frame.DataFrame'
# Load this into a dict
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()} # iterrows loops through pandas data frame and returns an index and a row
# print(type(phonetic_dict)) # Python dictionary
generate_phonetic()




