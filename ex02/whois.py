from sys import argv

if len(argv) == 1:
    exit(0)

if len(argv) > 2:
    print('more than one argument are provided')
    exit(1)

s = argv[1]

try:
    n = int(s)
except:
    print('argument is not an integer')
    exit(1)

if n == 0:
    print('I\'m Zero.')
elif n % 2 == 0:
    print('I\'m Even.')
else:
    print('I\'m Odd.')
