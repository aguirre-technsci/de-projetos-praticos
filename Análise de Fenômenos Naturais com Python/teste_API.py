import requests

# Substitua 'SUA_CHAVE_API' pela chave de API que você obteve do Weatherstack
API_KEY = 'ab7b224566c2b9789277089770839902'

# Função para obter dados meteorológicos com base nas coordenadas de latitude e longitude
def obter_dados_meteorologicos(latitude, longitude):
    base_url = f'http://api.weatherstack.com/current?access_key={API_KEY}&query={latitude},{longitude}&units=m'
    response = requests.get(base_url)
    dados = response.json()
    return dados

# Solicitar que o usuário insira as coordenadas de latitude e longitude
latitude = input("Digite a latitude: ")
longitude = input("Digite a longitude: ")

try:
    # Converter as entradas do usuário para valores de ponto flutuante
    latitude = float(latitude)
    longitude = float(longitude)
    
    # Obtendo dados meteorológicos reais
    dados_meteorologicos = obter_dados_meteorologicos(latitude, longitude)

    # Extraindo informações de temperatura e umidade
    temperatura = dados_meteorologicos['current']['temperature']
    umidade = dados_meteorologicos['current']['humidity']

    # Exibindo as informações coletadas
    print(f"Coordenadas: Latitude {latitude}, Longitude {longitude}")
    print(f"Temperatura: {temperatura}°C")
    print(f"Umidade: {umidade}%")
except ValueError:
    print("Por favor, insira valores válidos de latitude e longitude (números decimais).")
except KeyError:
    print("Não foi possível obter dados meteorológicos para as coordenadas fornecidas.")
