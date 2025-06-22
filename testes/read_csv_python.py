# 1. Dado um dicionário com os valores diários de uma cota de fundo, escreva um código em Python leia o arquivo.

# Python Raiz
file = "data.csv"

def read_csv_file(file: str) -> list[list]:
    # abre o arquivo em modo leitura
    with open(file, mode='r', encoding='utf-8') as open_file:

        # Cria uma lista de strings
        lines = open_file.readlines()

    # Remove quebras de linha e separa por vírgula
    data = [line.strip().split(',') for line in lines]
    return data

print(read_csv_file(file))





