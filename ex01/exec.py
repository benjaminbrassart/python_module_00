from sys import argv

if len(argv) != 1:
    s = ' '.join(argv[1:]) # merge arguments into a single string

    s = s[::-1] # reverse string
    s = s.swapcase() # swap case (doy)

    print(s)
