'''
D R E X E L   U N I V E R S I T Y
ENGR 131 -- Introductory Programming for Engineers

Acronym generator with special morpheme support

Written by Cole Bardin
Term:  Winter 2020-2021
'''


def generate_acronym(input_phrase, special_morphemes={}):
    words = input_phrase.split()
    acronym = ''

    for n in words:
        if n not in special_morphemes:
            if n.islower() == False:
                acronym += n[0]
        if n in special_morphemes:
            acronym += special_morphemes[n]
    return acronym


if __name__ == '__main__':
    input_phrase = str(input())
    example_special_morphemes = {
        'Chemical': 'CH', 'Exchange': 'EX', 'You': 'U'}
    acronym = generate_acronym(
        input_phrase, special_morphemes=example_special_morphemes)
    print(acronym)
