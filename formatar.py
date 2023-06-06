import string

def formata(texto):
    '''essa função formata o texto que ela recebe como argumento, retornando um texto sem caracteres especiais e pontuação, com todas as letras minúsculas'''
    caracteres = list(string.punctuation)
    #cria uma lista "caracteres" com todos os caracteres de pontuação obtidos por meio da função string.ponctuation

    caracteres_sem_numeros = ""
    #cria uma string vazia para o texto formatado#
    for caractere in texto:
        if not caractere in caracteres:
            caracteres_sem_numeros += caractere
      #cria um loop que varre todos os caracteres no texto que a função recebe e compara eles com os símbolos na lista "caracteres", caso sejam diferentes, o caracter é adicionado à "caracteres_sem_numeros"
    caracteres_sem_numeros = caracteres_sem_numeros.lower()
    #deixa toda a string em caixa baixa

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
    #substitui todas as letras com pontuação
    return caracteres_sem_numeros
