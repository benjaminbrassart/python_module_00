from sys import argv

if len(argv) < 3:
    print('too few arguments')
    exit(1)
elif len(argv) > 3:
    print('too many arguments')
    exit(1)
else:
    try:
        a = int(argv[1])
        b = int(argv[2])
    except:
        print('both arguments must be integers')
        exit(1)

    print(f'Sum:        {a+b}')
    print(f'Difference: {a-b}')
    print(f'Product:    {a*b}')

    if b == 0:
        print(f'Quotient:   ERROR (division by zero)')
        print(f'Remainder:  ERROR (modulo by zero)')
    else:
        print(f'Quotient:   {a/b}')
        print(f'Remainder:  {a%b}')

