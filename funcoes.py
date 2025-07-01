import pandas as pd

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

def mostrar_resultado_anual(df):
    # localiza datas e cotas
    initial_date, initial_quote, final_date, final_quote = localizar_datas_e_cotas_iniciais_e_finais(df)

    # calcula retorno acumulado
    variacao = (final_quote/initial_quote)-1

    # identifica quantidade de meses e anos
    meses = (final_date.year - initial_date.year) * 12 + (final_date.month - initial_date.month) - 1
    anos = meses / 12

    resultado_anual = (1 + variacao) ** (1 / anos) - 1

    print(f'''
        Resultado Anual
        Período: {initial_date} a {final_date}
        Resultado: {resultado_anual * 100:.2f}%
        ''')
    
    return resultado_anual

def mostrar_indice_sharpe(df):
    ''' IS = (Ri - Rf) / Vol

        IS = Índice Sharpe
        Ri = Retorno anual do portfolio
        Rf = Risk Free Ratio,taxa livre de risco anual: CDI
        Vol = Volatilidade do portfolio
    '''
    initial_date, initial_quote, final_date, final_quote = localizar_datas_e_cotas_iniciais_e_finais(df)
    resultado_anual = mostrar_resultado_anual(df)*100
    retorno_livre_de_risco = float(input("Informe o retorno anual do ativo livre de risco, no formato ##.##: "))
    volatilidade = mostrar_volatilidade(df, initial_date, final_date)
    indice_sharpe = (resultado_anual - retorno_livre_de_risco) / volatilidade
    
    print(f'''
        Índice Sharpe
        Período: {initial_date} a {final_date}
        Resultado Anual do Portfólio: {resultado_anual:.2f}%
        Retorno do Ativo Livre de Risco: {retorno_livre_de_risco:.2f}%
        Resultado: {indice_sharpe:.2f}%
        ''')
    
    return indice_sharpe

def encerrar_programa():
    print("Encerrando programa... \n")
    return

def mostrar_menu():
    while True:
        print('''              
            Escolha entre as seguintes opções:

            Calcular:        
            1. Retorno Total Acumulado;
            2. Volatilidade;
            3. Resultado Anual;
            4. Índice Sharpe;
            5. Maior Cota;
            6. Menor Cota;
            7. Maior Rentabilidade Mensal;
            8. Menor Rentabiliade Mensal;
            0. Sair.
            ''')
        
        try:
            action = int(input("Opção desejada: "))
            return action
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")
            continue

def mostrar_maior_cota(df):
    maior_cota = max(df['quote'])

    print(f'''
        Maior Cota: {maior_cota}
        ''')

    return maior_cota

def mostrar_menor_cota(df):
    menor_cota = min(df['quote'])

    print(f'''
        Menor Cota: {menor_cota}
        ''')

    return menor_cota

def mostrar_maior_rentabilidade_mensal(df):
    rentabilidades_mensais = []
    cotas: list = df['quote'].values
    print(cotas)

    # Para cada cota, calcular a rentabilidade em relação à cota anterior
    for i in range(1, len(cotas)):
        cota_atual = cotas[i]
        cota_anterior = cotas[i - 1]

        rentabilidade = (cota_atual / cota_anterior - 1) * 100
        rentabilidades_mensais.append(rentabilidade)
    
    maior_rentabilidade = max(rentabilidades_mensais)

    print(f'''
        Maior Rentabilidade: {maior_rentabilidade:.2f}%
        ''')
    
    return maior_rentabilidade

def mostrar_menor_rentabilidade_mensal(df):
    rentabilidades_mensais = []
    cotas: list = df['quote'].values
    print(cotas)

    # Para cada cota, calcular a rentabilidade em relação à cota anterior
    for i in range(1, len(cotas)):
        cota_atual = cotas[i]
        cota_anterior = cotas[i - 1]

        if cota_anterior is None:
            continue
        else:
            rentabilidade = (cota_atual / cota_anterior - 1) * 100
            rentabilidades_mensais.append(rentabilidade)
    
    menor_rentabilidade = min(rentabilidades_mensais)

    print(f'''
        Maior Rentabilidade: {menor_rentabilidade:.2f}%
        ''')
    
    return menor_rentabilidade