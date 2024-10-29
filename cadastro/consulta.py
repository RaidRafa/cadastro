cpf = str(input("Digite o CPF que deseja consultar: "))

try:
    with open(f"{cpf}.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print("Arquivo encontrado!")
        print(conteudo)

except FileNotFoundError:
    print("Arquivo não encontrado!!")