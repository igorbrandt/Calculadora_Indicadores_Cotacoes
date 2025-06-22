# 1. Dado um dicionário com os valores diários de uma cota de fundo, escreva um código em Python que calcule o retorno acumulado.

# Com DICT
cotacoes_fundo_x: dict = {
  '2023-01-01': 0.99,
  '2023-01-02': 1.01,
  '2023-01-03': 1.00,
  '2023-01-04': 1.01,
  '2023-01-05': 0.98,
  '2023-01-06': 1.00,
  '2023-01-07': 1.07,
  '2023-01-08': 1.03,
  '2023-01-09': 1.05,
  '2023-01-10': 1.06,
}

def calcular_retorno_total_acumulado_dict(cotacoes: dict) -> float:
    # Ordenar as datas para garantir a sequência cronológica
    cotacoes_ordenadas: list = sorted(cotacoes.keys())

    # identifica a primeira e última datas e traz as suas cota
    ultima_cota = cotacoes[cotacoes_ordenadas[-1]]
    primeira_cota = cotacoes[cotacoes_ordenadas[0]]

    # calcula o retorno percentual
    retorno = ((ultima_cota/primeira_cota) - 1)*100
    return retorno

print(calcular_retorno_total_acumulado_dict(cotacoes_fundo_x))