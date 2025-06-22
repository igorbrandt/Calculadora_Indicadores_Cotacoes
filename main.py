import pandas as pd

def main():
    try:
        action = int(input('''
            Bem-vindo(a) à calculadora! 
                                
            Escolha entre as seguintes opções:
            1. Calcular o retorno total acumulado;
            2. Calcular volatilidade;
            
            '''))

        file_path: str = input('''
            Informe o nome do seu arquivo csv, contendo as cotações a serem analisadas:
            ''')
        
        open_file: pd.DataFrame = read_csv(file_path)
        initial_date, initial_quote, final_date, final_quote = localizar_datas_e_cotas_iniciais_e_finais(open_file)

        if action == 1:
            mostrar_resultado_total_acumulado(initial_date, initial_quote, final_date, final_quote)
        
        elif action == 2:
            mostrar_volatilidade(open_file, initial_date, final_date)
        
        else:
            print("Escolha uma opção válida. \n")
            main()
    except ValueError:
        print("Escolha uma opção válida. \n")
        main()

def read_csv(quotation_csv_file: str) -> pd.DataFrame:
    try:
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
    except:
        print("Houve algum problema na leitura do arquivo informado. Tente novamente")
        main()

def localizar_datas_e_cotas_iniciais_e_finais(df):
    initial_date = df['date'].iloc[0].date()
    final_date = df['date'].iloc[-1].date()
    initial_quote = float(df['quote'].iloc[0])
    final_quote = float(df['quote'].iloc[-1])
    return initial_date, initial_quote, final_date, final_quote

def mostrar_resultado_total_acumulado(initial_date, initial_quote, final_date, final_quote):
    # calcula o resultado
    variacao = (final_quote/initial_quote)-1
    resultado_acumulado = round(variacao*100,2)

    print(f'''
        Resultado Total Acumulado
        Período: {initial_date} a {final_date}
        Resultado: {resultado_acumulado}%
        ''')
    
    return resultado_acumulado

def mostrar_volatilidade(df, initial_date, final_date):
    # Calcula o retorno diário percentual e cria uma terceira coluna no df
    df['retorno_diario'] = df['quote'].pct_change()

    # Remove valores nulos NaN do histórico (ex: primeiro valor re rentabilidade vai ser nulo)
    df = df.dropna(subset=['retorno_diario'])

    # Calcula desvio padrão dos retornos diários e transforma em %
    volatilidade = df['retorno_diario'].std() * 100

    print(f'''
          Volatilidade
          Período: {initial_date} a {final_date}
           {volatilidade:.2f}%
          ''')

    return volatilidade


if __name__ == "__main__":
    main()