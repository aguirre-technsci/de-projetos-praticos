import pandas as pd
import matplotlib.pyplot as plt
import os

# Obter o diretório do script atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Definir o diretório atual para o diretório do script
os.chdir(diretorio_atual)

# Carregar o arquivo .xlsx
nome_arquivo = "belem.xlsx"

# Verificar se o arquivo existe no diretório atual
if not os.path.isfile(nome_arquivo):
    print(f"O arquivo '{nome_arquivo}' não foi encontrado no diretório atual.")
else:
    df = pd.read_excel(nome_arquivo)

    # Pedir ao usuário o intervalo de tempo
    print("Selecione o intervalo de tempo:")
    print("1. Dia do Mês do Ano X até dia do mês do ano Y")
    print("2. Mês do ano X até mês do ano Y")
    print("3. Ano X até ano Y")

    opcao = int(input("Escolha uma opção (1/2/3): "))

    # Filtrar os dados com base na opção escolhida
    if opcao == 1:
        dia_inicio = int(input("Digite o dia de início: "))
        mes_ano_inicio = input("Digite o mês e o ano de início (MM-AAAA): ")
        dia_fim = int(input("Digite o dia de fim: "))
        mes_ano_fim = input("Digite o mês e o ano de fim (MM-AAAA): ")

        df = df[(df.iloc[:, 0] >= f'{mes_ano_inicio}-{dia_inicio:02d}') & (df.iloc[:, 0] <= f'{mes_ano_fim}-{dia_fim:02d}')]
    elif opcao == 2:
        mes_ano_inicio = input("Digite o mês e o ano de início (MM-AAAA): ")
        mes_ano_fim = input("Digite o mês e o ano de fim (MM-AAAA): ")

        df = df[(df.iloc[:, 0] >= mes_ano_inicio) & (df.iloc[:, 0] <= mes_ano_fim)]
    elif opcao == 3:
        ano_inicio = int(input("Digite o ano de início: "))
        ano_fim = int(input("Digite o ano de fim: "))

        df = df[(df.iloc[:, 0].dt.year >= ano_inicio) & (df.iloc[:, 0].dt.year <= ano_fim)]

    # Pedir ao usuário as estatísticas desejadas
    print("Selecione as estatísticas desejadas:")
    print("1. Mínimo")
    print("2. Média")
    print("3. Máximo")
    print("4. Mínimo, Média e Máximo")

    opcao = input("Escolha uma opção (1/2/3/4): ")

    if '4' in opcao:
        estatisticas = [df.columns[1], df.columns[2], df.columns[3]]
    else:
        estatisticas = []
        if '1' in opcao:
            estatisticas.append(df.columns[1])
        if '2' in opcao:
            estatisticas.append(df.columns[2])
        if '3' in opcao:
            estatisticas.append(df.columns[3])

    if not estatisticas:
        print("Nenhuma estatística individual selecionada para exibir.")
    else:
        plt.figure(figsize=(12, 6))

        # Cores para as linhas dos gráficos
        cores = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

        for i, col in enumerate(estatisticas):
            plt.plot(df.iloc[:, 0].dt.year, df[col], label=col, color=cores[i])

        plt.xlabel('Ano')
        plt.ylabel('Valores')
        plt.title('Estatísticas das Temperaturas')
        plt.legend(loc='upper left')
        plt.show()
