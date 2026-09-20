def exibir_menu():
    print("\n--- Gestão de Tickets de Suporte ---")
    print("1. Abrir novo ticket")
    print("2. Listar tickets abertos")
    print("3. Fechar ticket")
    print("4. Sair")
    return input("Escolha uma opção: ")

def main():
    tickets = []
    id_atual = 1

    while True:
        opcao = exibir_menu()

        if opcao == '1':
            cliente = input("Nome do Cliente: ")
            descricao = input("Descrição do Problema: ")
            ticket = {"id": id_atual, "cliente": cliente, "descricao": descricao, "status": "Aberto"}
            tickets.append(ticket)
            print(f"\n✅ Ticket #{id_atual} aberto com sucesso!")
            id_atual += 1

        elif opcao == '2':
            print("\n--- Tickets Abertos ---")
            abertos = [t for t in tickets if t['status'] == 'Aberto']
            if not abertos:
                print("Nenhum ticket aberto no momento.")
            else:
                for t in abertos:
                    print(f"[{t['id']}] Cliente: {t['cliente']} | Problema: {t['descricao']}")

        elif opcao == '3':
            id_fechar = int(input("Digite o ID do ticket para fechar: "))
            encontrado = False
            for t in tickets:
                if t['id'] == id_fechar:
                    t['status'] = 'Fechado'
                    print(f"\n🔒 Ticket #{id_fechar} fechado com sucesso!")
                    encontrado = True
                    break
            if not encontrado:
                print("\n❌ Ticket não encontrado.")

        elif opcao == '4':
            print("A encerrar o sistema...")
            break
        else:
            print("\n⚠️ Opção inválida. Tenta novamente.")

if __name__ == "__main__":
    main()
