# # # import math

# # # ####### Inteiros (int) #######

# # # ## 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# # # num_01 = int(input("Inserir um numero inteiro: "))
# # # num_02 = int(input("Inserir outro numero inteiro: "))
# # # resultado = num_01 + num_02
# # # print(resultado)

# # # ## 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# # # num_01 = int(input("Inserir um numero inteiro: "))
# # # resultado = num_01 % 5
# # # print(resultado)

# # # ## 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# # # num_01 = int(input("Inserir um numero inteiro: "))
# # # num_02 = int(input("Inserir outro numero inteiro: "))
# # # resultado = num_01 * num_02
# # # print(resultado)

# # # ## 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# # # num_01 = int(input("Inserir um numero inteiro: "))
# # # num_02 = int(input("Inserir outro numero inteiro: "))
# # # resultado = num_01 // num_02
# # # print(resultado)

# # # ## 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# # # num_01 = int(input("Inserir um numero inteiro: "))
# # # resultado = num_01 ** 2
# # # print(resultado)

# # # ####### Números de Ponto Flutuante (float) #######
# # # # 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# # # num_01 = float(input("Inserir um numero flutuante: "))
# # # num_02 = float(input("Inserir outro numero flutuante: "))
# # # resultado = num_01 + num_02
# # # print(resultado)

# # # ## 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# # # num_01 = float(input("Inserir um numero flutuante: "))
# # # num_02 = float(input("Inserir outro numero flutuante: "))
# # # resultado = (num_01 + num_02) / 2
# # # print(resultado)


# # # ## 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# # # num_01 = float(input("Inserir um numero flutuante que sera a base: "))
# # # num_02 = float(input("Inserir outro numero flutuante que sera o expoente: "))
# # # resultado = num_01 ** num_02
# # # print(resultado)

# # # ## 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# # # celsius = float(input("Digite a temperatura em Celsius: "))
# # # fahrenheit = (celsius * 9/5) + 32
# # # print(f"{celsius}°C é igual a {fahrenheit}°F")

# # # ## 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# # # raio_do_circulo = float(input("Digite o raio: "))
# # # area_do_circulo = math.pi * raio_do_circulo ** 2
# # # print(f"{area_do_circulo:.2f}")

# # # ####### Strings (str) #######
# # # ## 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# # texto = input("Digite um texto: ")
# # texto_maiusculas = texto.upper()
# # print("Texto em maiúsculas:", texto_maiusculas)

# # # ## 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome_completo = input("Digite o seu nome completo: ")
# nome_completo_minusculas = nome_completo.lower()
# print("Nome em minúsculas:", nome_completo_minusculas)

# # # ## 13.Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite ouma frase: ")
frase_sem_espacos = frase.strip()
print("Essa eh a frase com espacos no inicio e no fim: ", frase)
print("Essa eh a frase sem espacos no inicio e no fim: ", frase_sem_espacos)

# # # ## 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
# lista_dia_mes_ano = data_usuario.split("/")
# print(lista_dia_mes_ano)
# print(f"O elemento 1 (dia) e o: {lista_dia_mes_ano[0]}")
# print(f"O elemento 2 (mes) e o: {lista_dia_mes_ano[1]}")
# print(f"O elemento 3 (ano) e o: {lista_dia_mes_ano[2]}")


# # # ## 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# # # ####### Booleanos (bool) #######
# # # ## 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# # # ## 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# # # ## 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# # # ## 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# # # ## 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
