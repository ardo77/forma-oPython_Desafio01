import email


def cadastrar_contato(agenda: list):
    nome = input("Informe o Nome do Contato: ")
    telefone = input("Informe o Telefone de Contato: ")
    email = input("Informe o E-mail de Contato: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False,
    }

    agenda.append(contato)

    return


def listar_contatos(agenda: list):
    for indice, contato in enumerate(agenda, start=1):
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        favorito = "★" if contato["favorito"] else "_"

        print(f"| ID {indice}. [_{favorito}_] {nome}, {telefone}, {email}")


def editar_contato(agenda: list, indice: int):
    print(f"Nome Atual: {agenda[indice]['nome']}")
    novo_nome = input("Se desejar, informe o novo nome: ")

    print(f"\nTelefone Atual: {agenda[indice]['telefone']}")
    novo_telefone = input("Se desejar, informe o novo telefone: ")

    print(f"\nE-mail Atual: {agenda[indice]['email']}")
    novo_email = input("Se desejar, informe o novo e-mail: ")

    agenda[indice]["nome"] = novo_nome if novo_nome != "" else agenda[indice]["nome"]
    agenda[indice]["telefone"] = (
        novo_telefone if novo_telefone != "" else agenda[indice]["telefone"]
    )
    agenda[indice]["email"] = (
        novo_email if novo_email != "" else agenda[indice]["email"]
    )

    return


def marcar_desmarcar_contato_favorito(agenda: list, indice: int):
    if agenda[indice]["favorito"]:
        agenda[indice]["favorito"] = False
    else:
        agenda[indice]["favorito"] = True

    return


agenda = []

while True:
    print("\n__Menu da Agenda__")
    print("1. Adicionar um Contato")
    print("2. Visualizar Contatos")
    print("3. Editar um Contato")
    print("4. Marcar ou Desmarcar um Contato com Favorito")
    print("5. Lista de Contatos Favoritos")
    print("6. Apagar um Contato")
    print("7. Sair")

    opcao_escolhida = input("Informe o número da ação desejada: ")

    try:
        opcao_escolhida = int(opcao_escolhida)
    except Exception as e:
        print(f"Opção informada inválida.\nErro: {e}")
    else:
        if opcao_escolhida < 1 or opcao_escolhida > 7:
            print("Opção informada não corresponde as apresentadas.")
        else:
            if opcao_escolhida == 1:
                print("\n__Cadastra um Contato__")
                cadastrar_contato(agenda)
                print("Contato gravado com sucesso!")

            elif opcao_escolhida == 2:
                print("\n__Lista de Contatos__")
                listar_contatos(agenda)

            elif opcao_escolhida == 3:
                print("\n__Edita um Contato__")
                listar_contatos(agenda)
                indice_contato = input("Informe o ID do contato a ser editado: ")

                try:
                    indice_contato = int(indice_contato)
                except Exception as e:
                    print(f"Índice informado é inválido.\nErro: {e}")
                else:
                    if indice_contato < 1 or indice_contato > len(agenda):
                        print("Índice informado é inexistente.")
                    else:
                        editar_contato(agenda, (indice_contato - 1))
                        print("Contato atualizado com sucesso!")

            elif opcao_escolhida == 4:
                print("\n__Marca ou Desmarca um Contato__")
                listar_contatos(agenda)
                indice_contato = input(
                    "Informe o ID do contato a ser Marcado ou Desmarcado: "
                )

                try:
                    indice_contato = int(indice_contato)
                except Exception as e:
                    print(f"Índice informado é inválido.\nErro: {e}")
                else:
                    if indice_contato < 1 or indice_contato > len(agenda):
                        print("Índice informado é inexistente.")
                    else:
                        marcar_desmarcar_contato_favorito(agenda, (indice_contato - 1))
                        print("Ação realizada com sucesso!")

            elif opcao_escolhida == 5:
                print("\n__Lista Contatos Favoritos__")
            elif opcao_escolhida == 6:
                print("\n__Apaga um Contato__")
            elif opcao_escolhida == 7:
                break

print("\nAgenda Finalizada!")
