class TeacherCLI:
    def __init__(self, teacher_crud):
        self.teacher_crud = teacher_crud

    def run(self):
        while True:
            print("\nEscolha uma opção:")
            print("1. Cadastrar Professor")
            print("2. Consultar Professor")
            print("3. Atualizar CPF do Professor")
            print("4. Deletar Professor")
            print("5. Sair")

            choice = input("Opção: ")

            if choice == "1":
                self.create_teacher()
            elif choice == "2":
                self.read_teacher()
            elif choice == "3":
                self.update_teacher()
            elif choice == "4":
                self.delete_teacher()
            elif choice == "5":
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def create_teacher(self):
        name = input("Nome do Professor: ")
        ano_nasc = int(input("Ano de Nascimento: "))
        cpf = input("CPF: ")
        self.teacher_crud.create(name, ano_nasc, cpf)
        print("Professor cadastrado com sucesso.")

    def read_teacher(self):
        name = input("Nome do Professor: ")
        teacher = self.teacher_crud.read(name)
        if teacher:
            print(f"Informações sobre o Professor {name}:\n{teacher[0]}")
        else:
            print(f"Professor {name} não encontrado.")

    def update_teacher(self):
        name = input("Nome do Professor: ")
        new_cpf = input("Novo CPF: ")
        self.teacher_crud.update(name, new_cpf)
        print("CPF atualizado com sucesso.")

    def delete_teacher(self):
        name = input("Nome do Professor: ")
        self.teacher_crud.delete(name)
        print("Professor deletado com sucesso.")
