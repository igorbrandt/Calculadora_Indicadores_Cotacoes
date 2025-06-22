import pandas as pd
from funcoes import read_csv, mostrar_resultado_anual, mostrar_resultado_total_acumulado, mostrar_volatilidade, localizar_datas_e_cotas_iniciais_e_finais

def main():
    try:
        action = int(input('''
            Bem-vindo(a) à calculadora! 
                                
            Escolha entre as seguintes opções:
            1. Calcular o retorno total acumulado;
            2. Calcular volatilidade;
            3. Calcular resultado anual;
            
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
        
        elif action == 3:
            mostrar_resultado_anual(open_file)

        else:
            print("Escolha uma opção válida. \n")
            main()
    except ValueError:
        print("Escolha uma opção válida. \n")
        main()

if __name__ == "__main__":
    main()