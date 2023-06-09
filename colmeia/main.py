import requests

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("╔══════════════════════╗")
        print("║     Dados do CEP     ║")
        print("╠══════════════════════╣")
        print("║ Logradouro: ", data["logradouro"])
        print("║ Complemento: ", data["complemento"])
        print("║ Bairro: ", data["bairro"])
        print("║ Cidade: ", data["localidade"])
        print("║ Estado: ", data["uf"])
        print("╚══════════════════════╝")
    else:
        print("Erro ao obter os dados do CEP.")

def obter_informacoes_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    return data

def buscar_ip(ip):
    informacoes = obter_informacoes_ip(ip)

    print("╔══════════════════════════╗")
    print("║  Informações do IP       ║")
    print("╠══════════════════════════╣")
    print("║ IP: ", informacoes['query'])
    print("║ Cidade: ", informacoes['city'])
    print("║ Região: ", informacoes['regionName'])
    print("║ País: ", informacoes['country'])
    print("║ Código do País: ", informacoes['countryCode'])
    print("║ Provedor de Internet: ", informacoes['isp'])
    print("╚══════════════════════════╝")

def exibir_menu():
    
    print("\n  ░░░░░░░░░░░░░░░")
    print("  ░░░░███████░░░░")
    print("  ░░░█████████░░░")
    print("  ░░████     ████░░")
    print("  ░████        ████░")
    print("  ░███           ███░")
    print("  ░░██▄        ▄██░░")
    print("  ░░░███▄▄▄███░░░")
    print("  ░░░░███████░░░░\n")
   
    print("|=============================|")
    print("|  <<<<<COLMEIA PAINEL>>>>>   |")
    print("|                             |")
    print("|  [0] SAIR                   |")
    print("|  [?] CONTATE-NÓS            |") 
    print("|                             |")
    print("|  [1] BUSCAR CEP      (*+*)  |")
    print("|  [2] BUSCAR IP       (*+*)  |")
    print("|  [3] BUSCAR TELEFONE (Off)  |")
    print("|  [4] GERADOR DE CC   (Off)  |")
    print("|=============================|\n")
    
def sair():
    print("Saindo do programa...")
    exit()

# Loop principal
while True:
    exibir_menu()
    opcao = input(" SELECIONE UMA FUNÇÃO DA COLMEIA : ")

if opcao == "1":
    cep_alvo = input("Digite o CEP: ")
    buscar_cep(cep_alvo)
elif opcao == "2":
    ip_alvo = input("Digite o endereço IP: ")
    buscar_ip(ip_alvo)
elif opcao == "3":
    # Execute a ação desejada para a opção 3 aqui
    print(" [EM MANUTENÇÃO] ")
elif opcao == "4":
    # Execute a ação desejada para a opção 4 aqui
    print(" [EM MANUTENÇÃO] ")
elif opcao == "?":
    # Execute a ação desejada para a opção "?" aqui
    print("Opção ? selecionada.")
elif opcao == "0":
    sair()
else:
    print("Opção inválida. Tente novamente.\n")
