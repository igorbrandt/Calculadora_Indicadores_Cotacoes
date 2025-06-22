# 1. Dado um dicionário com os valores diários de uma cota de fundo, escreva um código em Python que calcule o retorno acumulado.

# Com import csv
import csv

file_path = "data.csv"

def csv_reader(file_to_read: str) -> list[dict]:
    '''
    Função que lê o csv
    '''
    with open(file_to_read, mode='r', encoding='utf-8') as open_file:
        reader = csv.reader(open_file) # cria um iterador de linhas: um objeto que pode ser percorrido com for
        for line in reader:
            print(line)


def calcular_retorno_total_acumulado_csv(x):
    '''
    Função que calcula o retorno total
    '''