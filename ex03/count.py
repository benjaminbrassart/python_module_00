import string

def text_analyzer(s = None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """

    if s is None:
        print('What is the text to analyze?')
        s = input('>> ')
        return text_analyzer(s)

    if type(s) is not str:
        print('argument is not a string')
        return

    up = 0
    low = 0
    space = 0
    punct = 0

    total = len(s)

    for c in s:
        if c.isupper():
            up += 1
        elif c.islower():
            low += 1
        elif c.isspace():
            space += 1
        elif c in string.punctuation:
            punct += 1

    print(f'The text contains {total} character(s):')
    print(f'- {up} upper letter(s)')
    print(f'- {low} lower letter(s)')
    print(f'- {punct} punctuation mark(s)')
    print(f'- {space} space(s)')

if __name__ == '__main__':
    from sys import argv

    if len(argv) <= 2:
        s = None

        if len(argv) == 2:
            s = argv[1]

        text_analyzer(s)
    else:
        print('too many arguments')
