import pandas as pd
import matplotlib.pyplot as plt

# Especificar o caminho completo para o arquivo Excel
dataset = pd.read_excel('FILE_DIR')

# Solicitar ao usuário as datas de início e término
print("As datas vão de 01/01/1990 a 30/09/2023")
data_inicial = input("Digite a data de início (no formato DD/MM/AAAA): ")
data_final = input("Digite a data de término (no formato DD/MM/AAAA): ")

# Solicitar ao usuário qual tipo de temperatura deseja visualizar
print("Escolha o tipo de temperatura:")
print("1. Mínima")
print("2. Média")
print("3. Máxima")

opcao = input("Digite o número da opção desejada (1 a 3): ").strip()

# Filtrar os dados com base nas datas especificadas
data_filtrada = dataset[(dataset['Data Medição'] >= data_inicial) & (dataset['Data Medição'] <= data_final)]

# Criar o gráfico correspondente
if opcao == '1':
    plt.plot(data_filtrada['Data Medição'], data_filtrada['Temperatura Mínima (°C)'], label='Mínima', color='g')
elif opcao == '2':
    plt.plot(data_filtrada['Data Medição'], data_filtrada['Temperatura Média (°C)'], label='Média', color='b')
elif opcao == '3':
    plt.plot(data_filtrada['Data Medição'], data_filtrada['Temperatura Máxima (°C)'], label='Máxima', color='orange')
else:
    print("Opção inválida. Escolha um número de 1 a 3.")

plt.title(f'Temperatura em Belém de {data_inicial} a {data_final}')
plt.xlabel('Data Medição')
plt.ylabel(f'Temperatura ({opcao.capitalize()} - °C)')
plt.grid(True)
plt.xticks(rotation=45)

# Exibir o gráfico final
plt.legend()
plt.show()
