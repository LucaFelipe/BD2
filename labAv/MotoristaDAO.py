from labAv.MotoristaCLI import MotoristaCLI

if __name__ == "__main__":
    db_url = 'mongodb://localhost:27017'  
    db_name = 'AtividadeAv'  

    motorista_cli = MotoristaCLI(db_url, db_name)
    print('Bem-vindo ao CLI do Motorista!')
    while True:
        print('\nOpções:')
        print('1. Criar Motorista')
        print('2. Ler Motorista')
        print('3. Atualizar Motorista')
        print('4. Deletar Motorista')
        print('5. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            motorista_cli.criar_motorista()
        elif opcao == '2':
            motorista_cli.ler_motorista()
        elif opcao == '3':
            motorista_cli.atualizar_motorista()
        elif opcao == '4':
            motorista_cli.deletar_motorista()
        elif opcao == '5':
            motorista_cli.fechar_conexao()
            break
        else:
            print('Opção inválida.')
            