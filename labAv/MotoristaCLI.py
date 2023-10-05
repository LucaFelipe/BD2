from database import Database
from labAv.Corrida import Corrida
from labAv.Motorista import Motorista
from labAv.Passageiro import Passageiro

class MotoristaCLI:
    def __init__(self, db_url, db_name):
        self.db = Database(db_url, db_name)
        self.collection = self.db.get_motoristas_collection()

    def criar_motorista(self):
        nome_motorista = input('Digite o nome do motorista: ')

        num_corridas = int(input('Quantas corridas deseja adicionar? '))
        corridas = []

        for i in range(num_corridas):
            nota = float(input(f'Digite a nota da corrida {i + 1}: '))
            distancia = float(input(f'Digite a distância da corrida {i + 1} (em km): '))
            valor = float(input(f'Digite o valor da corrida {i + 1} (em R$): '))

            nome_passageiro = input(f'Digite o nome do passageiro da corrida {i + 1}: ')
            documento_passageiro = input(f'Digite o documento do passageiro da corrida {i + 1}: ')

            passageiro = Passageiro(nome_passageiro, documento_passageiro)
            corrida = Corrida(nota, distancia, valor, passageiro.__dict__)
            corridas.append(corrida.__dict__)

        motorista = Motorista(nome_motorista, corridas)

        # Inserir o motorista no banco de dados
        result = self.collection.insert_one(motorista.__dict__)
        print('Motorista criado com sucesso. ID:', result.inserted_id)

    def ler_motorista(self):
        id_motorista = input('Digite o ID do motorista que deseja ler: ')
        motorista = self.collection.find_one({'_id': id_motorista})
        if motorista:
            print('Motorista encontrado:')
            print(motorista)
        else:
            print('Motorista não encontrado.')

    def atualizar_motorista(self):
        self.id_motorista = input('Digite o ID do motorista que deseja atualizar: ')

    def deletar_motorista(self):
        id_motorista = input('Digite o ID do motorista que deseja deletar: ')
        result = self.collection.delete_one({'_id': id_motorista})
        if result.deleted_count == 1:
            print('Motorista deletado com sucesso.')
        else:
            print('Motorista não encontrado ou não pôde ser deletado.')

    def fechar_conexao(self):
        self.db.close_connection()
