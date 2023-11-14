from teacher_cli import TeacherCLI
from teacher_crud import TeacherCRUD
from database import Database

uri = "bolt://3.83.153.152:7687"
user = "neo4j"
password = "street-watches-catchers"
database = Database(uri, user, password)

teacher_crud = TeacherCRUD(database)

teacher_cli = TeacherCLI(teacher_crud)

teacher_cli.run()

teacher_renzo = teacher_crud.read("Renzo")
if teacher_renzo:
    print(f"Ano de Nascimento de Renzo: {teacher_renzo[0]['t.ano_nasc']}")
    print(f"CPF de Renzo: {teacher_renzo[0]['t.cpf']}")
else:
    print("Professor Renzo não encontrado.")

teachers_m = database.execute_query("MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf")
for teacher in teachers_m:
    print(f"Nome: {teacher['t.name']}, CPF: {teacher['t.cpf']}")

cities = database.execute_query("MATCH (c:City) RETURN c.name")
for city in cities:
    print(f"Nome da Cidade: {city['c.name']}")

schools = database.execute_query("MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number")
for school in schools:
    print(f"Nome da Escola: {school['s.name']}, Endereço: {school['s.address']}, Número: {school['s.number']}")
