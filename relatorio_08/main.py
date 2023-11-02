from database import Database
from Relatorio08 import GameDatabase

db = Database("bolt://localhost:7687", "neo4j", "your_password")
db.drop_all()

game_db = GameDatabase(db)

game_db.create_player("p1", "Player1")
game_db.create_player("p2", "Player2")
game_db.create_player("p3", "Player3")

game_db.create_match("m1", ["p1", "p2"], "p1_won")
game_db.create_match("m2", ["p1", "p3"], "p1_won")

game_db.delete_player("p3")
game_db.delete_match("m2")

print("Jogadores:")
print(game_db.get_players())
print("Informações sobre a partida m1:")
print(game_db.get_match("m1"))
print("Histórico de partidas do jogador p1:")
print(game_db.get_player_history("p1"))

db.close()
