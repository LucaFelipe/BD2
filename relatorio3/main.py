import json
from urllib import request
from venv import Database
from venv import writeAJson

db = Database(database="pokedex", collection="pokemons")

class Pokedex:
    def __init__(self, database):
        self.database = database

    def getPokemonByName(name: str):
        return db.collection.find({"name": name})

    def getPokemonsByType(types: list):
        return db.collection.find({"type": {"$in": types}})
    
    pokemons = db.collection.find({"name":__name__})
    
    pikachu = getPokemonByName("Pikachu")
    writeAJson(pikachu, "pikachu")
    
    types = ["Fighting"]
    pokemons = getPokemonsByType(types)
    writeAJson(pokemons,"pokemons_by_type")
    
    tipos = ["Grass", "Poison"]
    pokemons = db.collection.find({"type": {"$sin": tipos}, "next_evolution": {"$exist": True}})
    
    writeAJson(pokemons,"next_evoluiton")
    
    fraquezas = ["Psychic", "Ice"]
    pokemons = db.collection.find({"weaknesses": {"$all": fraquezas}})
    writeAJson(pokemons,"weakness_specific")
    
    pokemons = db.collection.find({"weaknesses": {"$size": 1}})
    writeAJson(pokemons,"weaknesses_by_1")
    
    pokemons = db.collection.find({"spawn_chance": {"$gt": 0.3, "$lt": 0.6}})
    writeAJson(pokemons,"spawn_chance")
    
    pokemons = db.collection.find({"multipliers": None})
    writeAJson(pokemons,"multipliers_none")
    
    pokemons = db.collection.find({"multipliers": {"$exists": False}})
    writeAJson(pokemons,"multipliers_false")
    
    pokemons = db.collection.find({"next_evolution.1.num": {"$lte": "020"}})
    writeAJson(pokemons,"next_evoluiton.1.num")
    
    pokemons = db.collection.find({"$or": [{"type":"Fire"},{"weaknesses": "Fire"}]})
    writeAJson(pokemons,"type_fire_or_weakness_fire")
    
    github_url = "https://github.com/LucaFelipe/BD2.git"
    log_data = json.load(open("log.json"))
    response = request.post(github_url, json=log_data)

    if response.status_code == 200:
        print("Logs enviados com sucesso para o GitHub.")
    else:
        print("Erro ao enviar logs para o GitHub.")
