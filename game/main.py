import random
import re
import math


def choose_options():
    options = ('SP', 'PT', 'CDF', 'PDLM', 'PQ', 'ME', 'M', 'E', 'S', 'L', 'M', 'MC', 'BA', 'FPT',
               'LDM', 'OT', 'BI', 'P', 'J', 'SB', 'ET', 'L', 'RDA', 'JG', 'PCC', 'CH', 'OC', 'RDS')

    user_option = input(""" Bienvenido al juego de la direccion
    1. Escoge un miembro al azar
    2. Salir """)

    if not user_option:
        print("Vacio")
        return None


    if user_option == 1:
        total = len(options) + 1
        computer_option = random.choice(range(total))

        computer_option = options[computer_option]

        print(computer_option)

        if computer_option in ('FPT', 'SB', 'E'):
            print('CRACK')

        elif not computer_option in ('MC', 'BA', 'JG'):
            print("Te salvaste! puro og")

        else:
            print('MALO! el mongosaurio chulito para el joven')

    

    elif user_option == 2:
        print('Bye')
        return None

    else:
        print('Cualquiera')
        return None


def main():
    while True:
        choose_options()
     

if __name__ == "__main__":
    main()
