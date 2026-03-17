# Solicitar como entrada dois números e realizar uma operação simples entre eles.
# Pode ser utilizado int ou float para os números, e as operações podem ser soma, subtração, multiplicação ou divisão.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = abs(num1 - num2)
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    resultado = "Operação inválida"

print("Resultado:", resultado)