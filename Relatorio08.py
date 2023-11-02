from neo4j import GraphDatabase

class GameDatabase:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def create_player(self, player_id, name):
        with self._driver.session() as session:
            session.write_transaction(self._create_player, player_id, name)

    @staticmethod
    def _create_player(tx, player_id, name):
        tx.run("MERGE (p:Player {id: $player_id}) SET p.name = $name", player_id=player_id, name=name)

    def create_match(self, match_id, player_ids, result):
        with self._driver.session() as session:
            session.write_transaction(self._create_match, match_id, player_ids, result)

    @staticmethod
    def _create_match(tx, match_id, player_ids, result):
        tx.run("CREATE (m:Match {id: $match_id, result: $result})", match_id=match_id, result=result)
        for player_id in player_ids:
            tx.run("MATCH (p:Player {id: $player_id}) "
                   "MERGE (p)-[:PARTICIPATED_IN]->(m)", player_id=player_id)

    def get_players(self):
        with self._driver.session() as session:
            return session.read_transaction(self._get_players)

    @staticmethod
    def _get_players(tx):
        result = tx.run("MATCH (p:Player) RETURN p.id, p.name")
        return [{"id": record["p.id"], "name": record["p.name"]} for record in result]

    def get_match(self, match_id):
        with self._driver.session() as session:
            return session.read_transaction(self._get_match, match_id)

    @staticmethod
    def _get_match(tx, match_id):
        result = tx.run("MATCH (m:Match {id: $match_id}) RETURN m.id, m.result", match_id=match_id)
        return {"id": result.single()["m.id"], "result": result.single()["m.result"]}

    def get_player_history(self, player_id):
        with self._driver.session() as session:
            return session.read_transaction(self._get_player_history, player_id)

    @staticmethod
    def _get_player_history(tx, player_id):
        result = tx.run("MATCH (p:Player {id: $player_id})-[:PARTICIPATED_IN]->(m:Match) RETURN m.id, m.result", player_id=player_id)
        return [{"match_id": record["m.id"], "result": record["m.result"]} for record in result]

    def delete_player(self, player_id):
        with self._driver.session() as session:
            session.write_transaction(self._delete_player, player_id)

    @staticmethod
    def _delete_player(tx, player_id):
        tx.run("MATCH (p:Player {id: $player_id}) DETACH DELETE p", player_id=player_id)

    def delete_match(self, match_id):
        with self._driver.session() as session:
            session.write_transaction(self._delete_match, match_id)

    @staticmethod
    def _delete_match(tx, match_id):
        tx.run("MATCH (m:Match {id: $match_id}) DETACH DELETE m", match_id=match_id)


uri = "bolt://localhost:7687"
user = "neo4j"
password = "your_password"
game_db = GameDatabase(uri, user, password)

# Criar jogadores e partidas
game_db.create_player("p1", "Player1")
game_db.create_player("p2", "Player2")
game_db.create_player("p3", "Player3")

game_db.create_match("m1", ["p1", "p2"], "p1_won")
game_db.create_match("m2", ["p1", "p3"], "p1_won")

# Obter lista de jogadores
players = game_db.get_players()
print("Lista de jogadores:")
for player in players:
    print(player)

# Obter informações sobre uma partida específica
match_info = game_db.get_match("m1")
print("\nInformações sobre a partida m1:")
print(match_info)

# Obter histórico de partidas de um jogador
player_history = game_db.get_player_history("p1")
print("\nHistórico de partidas do jogador p1:")
for match in player_history:
    print(match)

# Deletar um jogador e uma partida
game_db.delete_player("p3")
game_db.delete_match("m2")

game_db.close()
