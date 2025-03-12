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
            elif opcao_escolhida == 2:
                print("\n__Lista Contatos")
            elif opcao_escolhida == 3:
                print("\n__Edita um Contato")
            elif opcao_escolhida == 4:
                print("\n__Marca ou Desmarca um Contato")
            elif opcao_escolhida == 5:
                print("\n__Lista Contatos Favoritos")
            elif opcao_escolhida == 6:
                print("\n__Apaga um Contato")
            elif opcao_escolhida == 7:
                break

print("\nAgenda Finalizada!")
