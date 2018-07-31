import re

patron = '[\w]+\@[a-z]+[.][a-z]{3}$'

correo = input("Correo: ")

if __name__ == "__main__":
    if re.match(patron, correo):
        print('Entrada Válida')
    else:
        print('Entrada Inválida')

