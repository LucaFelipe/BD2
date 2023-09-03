from urllib import request
from relatorio3.database import Database
import json
import datetime

class Pokedex:
    def __init__(self, database):
        self.database = database

    def query_1(self):
        result = self.database.query("SELECT * FROM pokemon WHERE type = 'Grass'")
        self.write_a_json(result, "Query 1: Lista de Pokémon do tipo Grass")
        return result

    def query_2(self):
        result = self.database.query("SELECT * FROM pokemon WHERE generation = 1")
        self.write_a_json(result, "Query 2: Lista de Pokémon da primeira geração")
        return result

    def query_3(self):
        result = self.database.query("SELECT * FROM pokemon WHERE height >= 10")
        self.write_a_json(result, "Query 3: Lista de Pokémon com altura maior ou igual a 10")
        return result

    def query_4(self):
        result = self.database.query("SELECT * FROM pokemon WHERE weight <= 5")
        self.write_a_json(result, "Query 4: Lista de Pokémon com peso menor ou igual a 5")
        return result

    def query_5(self):
        result = self.database.query("SELECT * FROM pokemon WHERE base_experience >= 200")
        self.write_a_json(result, "Query 5: Lista de Pokémon com experiência base maior ou igual a 200")
        return result

    def write_a_json(self, data, log_message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {"timestamp": timestamp, "message": log_message, "data": data}
        with open("log.json", "a") as log_file:
            json.dump(log_entry, log_file, indent=4)
            log_file.write("\n")

if __name__ == "main":
    db = Database()
    pokedex = Pokedex(db)

    # Executar as consultas e gerar logs
    pokedex.query_1()
    pokedex.query_2()
    pokedex.query_3()
    pokedex.query_4()
    pokedex.query_5()

    # Enviar os logs para o GitHub
    github_url = "https://github.com/LucaFelipe/BD2.git"
    log_data = json.load(open("log.json"))
    response = request.post(github_url, json=log_data)

    if response.status_code == 200:
        print("Logs enviados com sucesso para o GitHub.")
    else:
        print("Erro ao enviar logs para o GitHub.")
