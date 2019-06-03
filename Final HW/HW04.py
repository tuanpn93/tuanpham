import numpy as np
import pandas as pd


str = "Ah meta descriptions… the last bastion of traditional marketing! The only cross-over point between marketing and search engine optimisation! The knife edge between beautiful branding and an online suicide note!"
print(str.split())
s = pd.Series(str.split())


def check_vow(str):
    vowels = ['a', 'A', 'o', 'O', 'e', 'E', 'i', 'I', 'u', 'U']
    listOfVowel = [i for i in str if i in vowels]
    if len(listOfVowel) >= 3:
        return True
    else:
        return False


s2 = s.map(lambda x: ''.join([z for z in filter(check_vow, [x])]), na_action='ignore')

print(s2)
