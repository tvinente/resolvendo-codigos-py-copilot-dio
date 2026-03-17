# Testar se uma palavra é um palíndromo.  

import unicodedata

palavra = input("Digite uma palavra: ")

# Remove acentos e converte para NFD, depois remove caracteres não ASCII
palavra_sem_acentos = unicodedata.normalize('NFD', palavra).encode('ascii', 'ignore').decode()

# Remove espaços e caracteres especiais, mantendo apenas letras e números
palavra_limpa = ''.join(char for char in palavra_sem_acentos if char.isalnum())

#inversão da string
palavra_invertida = palavra_limpa[::-1]

# Verificação
if palavra_limpa.lower() == palavra_invertida.lower():
    print(f"A palavra '{palavra}' é um palíndromo! ")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
