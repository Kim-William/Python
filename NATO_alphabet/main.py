

import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter:row.code for index, row in df.iterrows()}

\
input= 'WoongKeol'

name_codes = [char for char in input.upper()]
output_list = [phonetic_dict[code] for code in name_codes]

print(f"{input} = {output_list}")

