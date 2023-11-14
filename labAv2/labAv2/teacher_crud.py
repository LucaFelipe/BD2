class TeacherCRUD:
    def __init__(self, database):
        self.database = database

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.database.execute_query(query, parameters)

    def read(self, name):
        query = "MATCH (t:Teacher {name: $name}) RETURN t"
        parameters = {"name": name}
        return self.database.execute_query(query, parameters)

    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DELETE t"
        parameters = {"name": name}
        self.database.execute_query(query, parameters)

    def update(self, name, new_cpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $new_cpf"
        parameters = {"name": name, "new_cpf": new_cpf}
        self.database.execute_query(query, parameters)
