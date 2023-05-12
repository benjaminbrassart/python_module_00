from sys import argv

if len(argv) == 1:
    exit(0);

MORSE = {
    "A": "", "B": "", "C": "", "D": "", "E": "", "F": "",
    "G": "", "H": "", "I": "", "J": "", "K": "", "L": "",
    "M": "", "N": "", "O": "", "P": "", "Q": "", "R": "",
    "S": "", "T": "", "U": "", "V": "", "W": "", "X": "",
    "Y": "", "Z": "", "0": "", "1": "", "2": "", "3": "",
    "4": "", "5": "", "6": "", "7": "", "8": "", "9": "",
    " ": "/",
}

s = ' '.join(argv[1:])
codes = []

print(s)

for c in s:
    morse = MORSE.get(c.upper(), None)

    if morse is None:
        print("ERROR")
        exit(1)

    codes += morse

print(' '.join(codes))
