from collections import *   # nie zaleca się stosowania tej formy importu

PUNCTATIONS = ".,?!-:;()\"" # literówka
forms_in_text = {}
digrams_in_text = {}
trigrams_in_text = {}


def get_forms_from_text(filepath):
    with open(filepath, "r", encoding="utf-8") as infile:
        for line in infile:
            line = line.strip()
            for punct in PUNCTATIONS:
                line = line.replace(punct, " " + punct)
            for token in line.split():
                if token in set(PUNCTATIONS):
                    continue
                elif token in forms_in_text.keys():
                    forms_in_text[token] += 1
                else:
                    forms_in_text[token] = 1


def get_digrams_from_text(filepath):
    new_digram = []
    with open(filepath, "r", encoding="utf-8") as infile:   # DRY - patrz funkcja wyżej
        for line in infile:
            line = line.strip()
            for punct in PUNCTATIONS:
                line = line.replace(punct, " " + punct)
            for token in line.split():
                if token in set(PUNCTATIONS):
                    continue
                else:
                    new_digram.append(token)
                    if len(new_digram) == 2:
                        if str(new_digram) in digrams_in_text.keys():
                            digrams_in_text[str(new_digram)] += 1
                            new_digram[0] = new_digram[1]
                            new_digram.pop(1)
                        else:
                            digrams_in_text[str(new_digram)] = 1
                            new_digram[0] = new_digram[1]   # DRY - wyciąganie wspólnego czynnika za nawias
                            new_digram.pop(1)


def get_trigrams_from_text(filepath):   # czy dałoby się tę funkcję uogólnić na n-gramy?
    new_trigram = []
    with open(filepath, "r", encoding="utf-8") as infile:
        for line in infile:
            line = line.strip()
            for punct in PUNCTATIONS:
                line = line.replace(punct, " " + punct)
            for token in line.split():
                if token in set(PUNCTATIONS):
                    continue
                else:
                    new_trigram.append(token)
                    if len(new_trigram) == 3:
                        if str(new_trigram) in trigrams_in_text.keys():
                            trigrams_in_text[str(new_trigram)] += 1
                            new_trigram[0] = new_trigram[1]
                            new_trigram.pop(1)  # czemu pop(1)?
                        else:
                            trigrams_in_text[str(new_trigram)] = 1
                            new_trigram[0] = new_trigram[1]
                            new_trigram.pop(1)



def sort_elements_in_dictionary(dictionary):
    return {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}



get_forms_from_text("potop.txt")
print(sort_elements_in_dictionary(forms_in_text))


get_digrams_from_text("potop.txt")
print(Counter(digrams_in_text).most_common(20)) # to nie gwarantuje wypisania remisów



get_trigrams_from_text("potop.txt")
print(Counter(trigrams_in_text).most_common(20))


