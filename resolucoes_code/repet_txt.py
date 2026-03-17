# Solicitar uma string e um número inteiro como entrada. Retornar a string repetida o número de vezes informado.
string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))
resultado = string * numero
print(' '.join(resultado))