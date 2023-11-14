from neo4j import GraphDatabase

class Database:
    def run_query(uri, user, password, query):
        with GraphDatabase.driver(uri, auth=(user, password)) as driver:
         with driver.session() as session:
            result = session.run(query)
            return result.data()
            
    def close(self):
        self.driver.close()
    def execute_query(self, query, parameters = None):
        data = []
        with self.driver.session() as session:
            results = session.run(query,parameters)
            for record in results:
                data.append(record)
            return data
    def drop_all(self):
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
    
    
        