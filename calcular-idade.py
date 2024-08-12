def calcular_idade():
    while True:
        nome = input("Digite seu nome completo: ")

        try:
            ano_nascimento = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))

            if 1922 <= ano_nascimento <= 2021:
                idade = 2022 - ano_nascimento
                print(f"\nNome: {nome}")
                print(f"Idade em 2022: {idade} anos")
                break
            else:
                print("Ano inválido. Por favor, insira um ano entre 1922 e 2021.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido para o ano de nascimento.")


# Executando o programa
calcular_idade()
