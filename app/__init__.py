import re

#patron = '[\w]+\@[a-z]+[.][a-z]{3}$'

patron = '[(\w+\S)][@uip.edu.pa|@uip.pa|@gmail.com|@outlook.es|yahoo.com]'
#patron = "niñ[oa]s"

correo = input("Correo: ")

if __name__ == "__main__":
    if re.match(patron, correo):
        print('Entrada Válida')
    else:
        print('Entrada Inválida')

