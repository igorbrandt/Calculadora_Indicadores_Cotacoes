# 1. Dado um dicionário com os valores diários de uma cota de fundo, escreva um código em Python que calcule o retorno acumulado.
# Com import pandas
import pandas as pd

def main():
    try:
        action = int(input('''
            Bem-vindo(a) à calculadora! 
                                
            Escolha entre as seguintes opções:
            1. Calcular o retorno total acumulado;
            2. Calcular volatilidade;
            
            '''))

        file_path = input('''
            Informe o nome do seu arquivo csv, contendo as cotações a serem analisadas:
            ''')
        open_file = read_csv(file_path)

        if action == 1:
            mostrar_resultado_total_acumulado(open_file)
        
        elif action == 2:
            mostrar_volatilidade(file_path)
        
        else:
            print("Escolha uma opção válida. \n")
            main()
    except ValueError:
        print("Escolha uma opção válida. \n")
        main()

def read_csv(quotation_csv_file):
    df = pd.read_csv(quotation_csv_file, sep=';', decimal=',')

    # confere se existem ao menos dois registros
    if len(df) < 2:
        print("Dados insuficientes. Deve haver ao menos dois registros.")
        return

    # Converte a coluna de data para o tipo datetime e salva no DF (atribuindo df['date'])
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Converte a coluna de cota para o tipo número e salva no DF (atribuindo df['quote'])
    df['quote'] = df['quote'].astype(str).str.replace('"', '').str.replace(',', '.')
    df['quote'] = pd.to_numeric(df['quote'], errors='coerce')

    # Ordena pela data ASC
    df = df.sort_values(by='date')
    return df

def mostrar_resultado_total_acumulado(df):
    # localiza datas e cotas iniciais e finais
    initial_date = df['date'].iloc[0].date()
    final_date = df['date'].iloc[-1].date()
    initial_quote = float(df['quote'].iloc[0])
    final_quote = float(df['quote'].iloc[-1])

    # calcula o resultado
    variacao = (final_quote/initial_quote)-1
    resultado_acumulado = round(variacao*100,2)

    print(f'''
        Resultado Total Acumulado
        Período: {initial_date} a {final_date}:
        Resultado: {resultado_acumulado}%
        ''')
    
    return resultado_acumulado

def mostrar_volatilidade(df):
    '''
    Função que traz a volatilidade
    '''

if __name__ == "__main__":
    main()