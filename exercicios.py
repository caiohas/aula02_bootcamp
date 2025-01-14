import math

###### Inteiros (int) #######
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num_01 = int(input("Inserir um numero inteiro: "))
num_02 = int(input("Inserir outro numero inteiro: "))
resultado = num_01 + num_02
print(resultado)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
num_01 = int(input("Inserir um numero inteiro: "))
resultado = num_01 % 5
print(resultado)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
num_01 = int(input("Inserir um numero inteiro: "))
num_02 = int(input("Inserir outro numero inteiro: "))
resultado = num_01 * num_02
print(resultado)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
num_01 = int(input("Inserir um numero inteiro: "))
num_02 = int(input("Inserir outro numero inteiro: "))
resultado = num_01 // num_02
print(resultado)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
num_01 = int(input("Inserir um numero inteiro: "))
resultado = num_01 ** 2
print(resultado)

###### Números de Ponto Flutuante (float) #######
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
num_01 = float(input("Inserir um numero flutuante: "))
num_02 = float(input("Inserir outro numero flutuante: "))
resultado = num_01 + num_02
print(resultado)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
num_01 = float(input("Inserir um numero flutuante: "))
num_02 = float(input("Inserir outro numero flutuante: "))
resultado = (num_01 + num_02) / 2
print(resultado)


# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
num_01 = float(input("Inserir um numero flutuante que sera a base: "))
num_02 = float(input("Inserir outro numero flutuante que sera o expoente: "))
resultado = num_01 ** num_02
print(resultado)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C é igual a {fahrenheit}°F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio_do_circulo = float(input("Digite o raio: "))
area_do_circulo = math.pi * raio_do_circulo ** 2
print(f"{area_do_circulo:.2f}")

###### Strings (str) #######
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
texto = input("Digite um texto: ")
texto_maiusculas = texto.upper()
print("Texto em maiúsculas:", texto_maiusculas)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_completo = input("Digite o seu nome completo: ")
nome_completo_minusculas = nome_completo.lower()
print("Nome em minúsculas:", nome_completo_minusculas)

# 13.Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite ouma frase: ")
frase_sem_espacos = frase.strip()
print("Essa eh a frase com espacos no inicio e no fim: ", frase)
print("Essa eh a frase sem espacos no inicio e no fim: ", frase_sem_espacos)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
lista_dia_mes_ano = data_usuario.split("/")
print(lista_dia_mes_ano)
print(f"O elemento 1 (dia) e o: {lista_dia_mes_ano[0]}")
print(f"O elemento 2 (mes) e o: {lista_dia_mes_ano[1]}")
print(f"O elemento 3 (ano) e o: {lista_dia_mes_ano[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
parte1 = input("Digite a primeira parte do texto: ")
parte2 = input("Digite a segunda parte do texto: ")
texto_concatenado = parte1 + parte2
print("Texto concatenado: ", texto_concatenado)

###### Booleanos (bool) #######
# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
valor1 = input("Digite uma expressao booleana (True ou False): ")
valor2 = input("Digite outra expressao booleana (True ou False): ")
resultado_and = valor1 and valor2
print("Resultado do AND lógico: ", resultado_and)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
valor1 = input("Digite uma expressao booleana (True ou False): ")
valor2 = input("Digite outra expressao booleana (True ou False): ")
resultado_or = valor1 or valor2
print("Resultado do OR lógico: ", resultado_or)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
valor1 = input("Digite uma expressao booleana (True ou False): ")
resultado_not = not valor1 
print("Resultado do NOT lógico: ", resultado_or)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num_01 = int(input("Inserir um numero inteiro: "))
num_02 = int(input("Inserir outro numero inteiro: "))
resultado_igualdade = (num_01 == num_02)
print("Resultado da igualdade: ", resultado_igualdade)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
num_01 = int(input("Inserir um numero inteiro: "))
num_02 = int(input("Inserir outro numero inteiro: "))
resultado_diferenca = (num_01 != num_02)
print("Resultado da diferença:", resultado_diferenca)

# 21. Conversor de Temperatura
## Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
## O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
## garantir que a entrada seja numérica, tratando qualquer ValueError. 
## Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
try:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F")
except:
    print("Digite um número válido de temperatuda para a operação de conversão.")

# 22. Verificador de Palíndromo
## Crie um programa que verifica se uma palavra ou frase é um palíndromo 
## (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
## Utilize try-except para garantir que a entrada seja uma string. 
## Dica: Utilize a função isinstance() para verificar o tipo da entrada.
entrada = input("Digite uma palavra ou frase: ")
if isinstance(entrada, str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")

# 23. Calculadora Simples
## Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
## Use try-except para lidar com divisões por zero e entradas não numéricas. 
## Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
## Imprima o resultado ou uma mensagem de erro apropriada.
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/' and num2 != 0:
        resultado = num1 / num2
    else:
        print("Operador inválido ou divisão por zero.")
    print("Resultado:", resultado)
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")

# 24. Classificador de Números
## Escreva um programa que solicite ao usuário para digitar um número. 
## Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número 
## como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".
try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")

# 25. Conversão de Tipo com Validação
## Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
## O programa deve converter a string de entrada em uma lista de números inteiros. 
## Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
## Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
## Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.
entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")

# Fim