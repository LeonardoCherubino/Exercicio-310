#Exercicio 3.10 - Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do salário e a porcentagem do aumento.

antigo_salario = float(input('Entre com o valor do salário atual: '))
porcentagem_aumento = float(input('Entre com o valor do aumento em %: '))
novo_salario = antigo_salario + (antigo_salario * porcentagem_aumento / 100)
diferenca_salario = novo_salario - antigo_salario
print('O novo salário é: R$ {}'.format(novo_salario))
print('O aumento foi de: R$ {}'.format(diferenca_salario))
