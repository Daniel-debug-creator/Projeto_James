import string

def formata(texto):
    caracteres = list(string.punctuation)

    caracteres_sem_numeros = ""
    for caractere in texto:
        if not caractere in caracteres:
            caracteres_sem_numeros += caractere
    caracteres_sem_numeros = caracteres_sem_numeros.lower()

    caracteres_sem_numeros = caracteres_sem_numeros.replace('á', 'a')
    caracteres_sem_numeros = caracteres_sem_numeros.replace('à', 'a')
    caracteres_sem_numeros = caracteres_sem_numeros.replace('é', 'e')
    caracteres_sem_numeros = caracteres_sem_numeros.replace('í', 'i')
    caracteres_sem_numeros = caracteres_sem_numeros.replace('ó', 'o')
    caracteres_sem_numeros = caracteres_sem_numeros.replace('ú', 'u')
    caracteres_sem_numeros = caracteres_sem_numeros.replace('â', 'a')
    caracteres_sem_numeros = caracteres_sem_numeros.replace('ê', 'e')
    caracteres_sem_numeros = caracteres_sem_numeros.replace('ô', 'o')
    caracteres_sem_numeros = caracteres_sem_numeros.replace('û', 'u')
    caracteres_sem_numeros = caracteres_sem_numeros.replace('ã', 'a')
    caracteres_sem_numeros = caracteres_sem_numeros.replace('õ', 'o')
    caracteres_sem_numeros = caracteres_sem_numeros.replace('ç', 'c')
    return caracteres_sem_numeros
