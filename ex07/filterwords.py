from sys import argv
import string

if len(argv) != 3:
    print("ERROR")
    exit(1)

s = argv[1]

try:
    n = int(argv[2])
except:
    print("ERROR")
    exit(1)

s = ''.join([c for c in argv[1] if c not in string.punctuation])
words = s.split(' ')
words = [word for word in words if len(word) > n]

print(words)
