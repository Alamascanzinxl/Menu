import requests
from colmeia.desenhos import abelha, imprimir_login 
import os
import sys
import time

vermelha = '\033[91m'
verde = '\033[92m'
amarela = '\033[93m'
azul = '\033[94m'
reset = '\033[0m'
M = '\033[33m'
orange = '\033[38;5;208m'
Magenta = '\u001b[35m'

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(orange + "╔══════════════════════╗")
        print("║     Dados do CEP     ║")
        print("╠══════════════════════╣")
        print("║ Logradouro: ", data["logradouro"])
        print("║ Complemento: ", data["complemento"])
        print("║ Bairro: ", data["bairro"])
        print("║ Cidade: ", data["localidade"])
        print("║ Estado: ", data["uf"])
        print("╚══════════════════════╝" + reset)
    else:
        print(vermelha + "Erro ao obter os dados do CEP." + reset)

def obter_informacoes_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    return data

def buscar_ip(ip):
    informacoes = obter_informacoes_ip(ip)

    print(orange + "╔══════════════════════════╗")
    print("║  Informações do IP       ║")
    print("╠══════════════════════════╣")
    print("║ IP: ", informacoes['query'])
    print("║ Cidade: ", informacoes['city'])
    print("║ Região: ", informacoes['regionName'])
    print("║ País: ", informacoes['country'])
    print("║ Código do País: ", informacoes['countryCode'])
    print("║ Provedor de Internet: ", informacoes['isp'])
    print("╚══════════════════════════╝" + reset)

def exibir_menu():
    abelha()
    print(orange + "\nSelecione uma opção:")
    print("1. Buscar CEP")
    print("2. Buscar Informações de IP")
    print("0. EXIT" + reset)

def login():
    while True:
        imprimir_login()
        username = input(azul + " USUÁRIO: " + reset)
        password = input(amarela + " SENHA: " + reset)

        if username.strip() and password.strip():
            if username == "boa" and password == "compra":
                print(verde + "LOGIN BEM-SUCEDIDO!" + reset)
                break
            else:
                print(vermelha + "ERRADO AMIGO(A), tente novamente." + reset)
        else:
            print(vermelha + "NOME DE USUÁRIO E SENHA SÃO OBRIGATÓRIOS. Tente novamente." + reset)

        os.system('clear')

def show_loading():
    width = 50
    total_time = 10
    start_time = time.time()
    while (elapsed_time := time.time() - start_time) < total_time:
        filled_width = int(width * (elapsed_time / total_time))
        bar = '█' * filled_width + '-' * (width - filled_width)
        sys.stdout.write(f'\r[{bar}] {int(total_time - elapsed_time)}s')
        sys.stdout.flush()
        time.sleep(0.1)
    
    sys.stdout.write('\r' + ' ' * (width + 10) + '\r')
    sys.stdout.flush()

login()

print(orange + "Carregando...")
show_loading()
os.system('clear')

def sair():
    print(vermelha + "SAINDO DA COLMEIA BZZZ..." + reset)
    exit()

# Loop principal
while True:
    os.system('clear')
    exibir_menu()
    opcao = input(M + "OPÇÃO SELECIONADA: " + reset)

    if opcao == "1":
        cep_alvo = input(orange + "DIGITE O CEP: " + reset)
        buscar_cep(cep_alvo)
    elif opcao == "2":
        ip_alvo = input(orange + "DIGITE O ENDEREÇO IP: " + reset)
        buscar_ip(ip_alvo)
    elif opcao == "0":
        sair()
    else:
        print(vermelha + "OPÇÃO INVÁLIDA. TENTE NOVAMENTE.\n" + reset)
