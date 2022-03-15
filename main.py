# Importation
import math
import cmath

# Verzameling
verzameling = str(input('Werk je in reële of in complexe getallen (r / c)? '))

# Calculations
if verzameling == 'r':
    # Confirmation r
    print('Je werkt in reële getallen! ')

    # Inputs r
    a_r = float(input('Wat is je waarde voor a? '))
    b_r = float(input('Wat is je waarde voor b? '))
    c_r = float(input('Wat is je waarde voor c? '))

    # Calculations
    D = (b_r ** 2) - 4 * a_r * c_r

    if D < 0:
        print("Er zijn geen oplossingen ")
    elif D == 0:
        x = (-b_r + D ** 0.5) / (2 * a_r)
        print('Er is juist 1 oplossing, namelijk: ' + str(x))
    else:
        x_1 = (-b_r + D ** 0.5) / (2 * a_r)
        x_2 = (-b_r - D ** 0.5) / (2 * a_r)
        print('Er zijn 2 oplossingen, namelijk: ' + str(x_1) + ' en ' + str(x_2))

elif verzameling == 'c':
    # Confirmation c
    print('Je werkt in complexe getallen! ')

    # Check function
    def split(number):
        return [char for char in number]

    # Inputs c
    a_c = input('Wat is je waarde voor a? (zonder spaties) ')
    a_verzameling = None
    number_a = a_c
    a_c_list = split(number_a)
    print(a_c_list)
    if len(a_c_list) > 1:
        if 'i' in a_c_list:
            a_verzameling = 'complex'
        else:
            print('Je waarde voor a is geen correct getal! ')
    elif len(a_c_list) == 1:
        if 'i' not in a_c_list:
            a_verzameling = 'reëel'
    else:
        print('Ik kon je waarde voor a niet definiëren! ')
    print(a_verzameling)
    
    b_c = input('Wat is je waarde voor b? (zonder spaties) ')
    b_verzameling = None
    number_b = b_c
    b_c_list = split(number_b)
    print(b_c_list)
    if len(b_c_list) > 1:
        if 'i' in b_c_list:
            b_verzameling = 'complex'
        else:
            print('Je waarde voor b is geen correct getal! ')
    elif len(b_c_list) == 1:
        if 'i' not in b_c_list:
            b_verzameling = 'reëel'
    else:
        print('Ik kon je waarde voor b niet definiëren! ')
    print(b_verzameling)

    c_c = input('Wat is je waarde voor c? (zonder spaties) ')
    c_verzameling = None
    number_c = c_c
    c_c_list = split(number_c)
    print(c_c_list)
    if len(c_c_list) > 1:
        if 'i' in c_c_list:
            c_verzameling = 'complex'
        else:
            print('Je waarde voor c is geen correct getal! ')
    elif len(c_c_list) == 1:
        if 'i' not in c_c_list:
            c_verzameling = 'reëel'
    else:
        print('Ik kon je waarde voor c niet definiëren! ')
    print(c_verzameling)

    # Initialization
    if a_verzameling == 'complex':
        if a_c_list[0] == a_c_list[-4] and a_c_list[2] == a_c_list[-2]:
            a_a_complex = int(a_c_list[0])
            a_b_complex = int(a_c_list[2])
        else:
            print('Je waarde voor a is geen integer-vorm! ')

        a_z = complex(a_a_complex, a_b_complex)
        print(a_z)

    if b_verzameling == 'complex':
        if b_c_list[0] == b_c_list[-4] and b_c_list[2] == b_c_list[-2]:
            b_a_complex = int(b_c_list[0])
            b_b_complex = int(b_c_list[2])
        else:
            print('Je waarde voor b is geen integer-vorm! ')

        b_z = complex(b_a_complex, b_b_complex)
        print(b_z)

    if c_verzameling == 'complex':
        if c_c_list[0] == c_c_list[-4] and c_c_list[2] == c_c_list[-2]:
            c_a_complex = int(c_c_list[0])
            c_b_complex = int(c_c_list[2])
        else:
            print('Je waarde voor c is geen integer-vorm! ')

        c_z = complex(c_a_complex, c_b_complex)
        print(c_z)

    # Discriminant initialization
    if a_verzameling == 'reëel':
        d_a = int(a_c)
    elif a_verzameling == 'complex':
        d_a = a_z

    if b_verzameling == 'reëel':
        d_b = int(b_c)
    elif b_verzameling == 'complex':
        d_b = b_z

    if c_verzameling == 'reëel':
        d_c = int(c_c)
    elif b_verzameling == 'complex':
        d_c = c_z

    # Calculations
    D = (d_b ** 2) - 4 * d_a * d_c
    print(D)

else:
    # Restriction /
    print('Probeer opnieuw! ')