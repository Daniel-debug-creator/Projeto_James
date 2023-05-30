import string

def cesar(texto, paso):
    letras_minusculas = list(string.ascii_lowercase)
    numero = '0123456789'
    final = str()
    for c in texto:
        if c.isalpha():
            pos = letras_minusculas.index(c)
            new_pos = ((pos + paso) % len(letras_minusculas))
            final += letras_minusculas[new_pos]

        elif c.isnumeric():
            final += c
            """
            pos = numero.index(c)
            new_pos = ((pos + paso) % len(numero))
            final += numero[new_pos]
            """
    return final