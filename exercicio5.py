"""
Titulo: Exercicio 5
Autor: Pedro Colombo
Data: 25/02/2025
Versão: 0.0.1
Problema: calcule o salario de um professor horista na Universidade XYZ. O programa deve perguntar o numero de horas trabalhadas, calcular e imprimir na tela o valor do salario bruto, do salario lquido e do total de descontos, sabendo que o desconto do imposto e 30% e que o valor da hora-aula e R$ 40,00.

"""

# Alocação de memória

hora_aula = 40

    

# Entrada de dados

horas_trabalhadas = int(input("Qual foi a quantidade de horas que você trabalhou? "))
                              

# Processamento de dados

salario_bruto = hora_aula * horas_trabalhadas

salario_liquido = salario_bruto * 7/10

desconto = salario_bruto * 3 / 10


#Saida de dados
print(f"O seu salario bruto foi de R${salario_bruto}, por conta da incisão de impostos no valor de R${desconto}, o seu salário líquido ficou em R$ {salario_liquido} ")
