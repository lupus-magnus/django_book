# Crie um programa que solicita ao usuário que digite o seu login, e em seguida, verifica se está nas seguintes regras:
# inicia com maiuscula
# tem, no minimo, seis caracteres
# possui, pelo menos, dois caracteres numericos
# possui, pelo menos, três letras
# possui tamanho de até dez caracteres

username_is_valid = True
on_repeat = True
error_list = []
tried_users = []

while on_repeat:

    username = input("Por favor, insira o seu nome:\t")
    print("\n\n\n")
    # Verificando se a primeira letra e maiuscula
    if not username[0].isupper():
        msg = "Erro:\tSeu username deve possuir a primeira letra maiuscula."
        print(msg)
        error_list.append(msg)
        username_is_valid = False

    # Verificando se possuimos chars suficientes
    if len(username) < 6:
        msg = "Erro:\tSeu username deve ter 6 ou mais caracteres."
        print(msg)
        error_list.append(msg)
        username_is_valid = False

    # Se temos 2 ou mais digitos
    digits_counter = 0
    for letter in username:
        if letter.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        msg = "Erro:\tDeve haver dois ou mais digitos numericos no username"
        print(msg)
        error_list.append(msg)
        username_is_valid = False

    # pelo menos 3 letras
    alpha_counter = 0
    for letter in username:
        if letter.isalpha():
            alpha_counter += 1
    if alpha_counter < 3:
        msg = "Erro:\tDeve haver tres ou mais chars alfabeticos no username"
        print(msg)
        error_list.append(msg)
        username_is_valid = False

    # tamanho de ate 10 chars
    if len(username) > 10:
        msg = "Erro:\tO username deve conter ate 10 caracteres."
        print(msg)
        error_list.append(msg)
        username_is_valid = False

    # Pra finalizar, se o username estiver de acordo com todas as condicoes, ele e aprovado
    if username_is_valid:
        print("\n\n", "\tLOGIN DE SUCESSO\t".center(40, "#"), sep="")

    if on_repeat:
        new_user = {
            "username": username,
            "valid": "SUCCESS" if username_is_valid else "FAILURE",
            "errors": error_list,
        }
        tried_users.append(new_user)
        error_list = []
        msg = ""
        set_on_repeat = input("\n\nDeseja tentar de novo?\n1-\tSim\n2-\tNão\n\n")
        username_is_valid = True
        if int(set_on_repeat) == 2:
            for obj in tried_users:
                print(f'\n\n{obj["username"]}: {obj["valid"]}')
                print("Errors:")
                if len(obj["errors"]):
                    for err in obj["errors"]:
                        print(err)
                else:
                    print("None. Username is valid.")
            print("\n\n")

            on_repeat = False
