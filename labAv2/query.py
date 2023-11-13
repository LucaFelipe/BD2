class Query:
    def __init__(self, database):
        self.database = database

    def find_teacher_by_name(self, name):
        query = f"MATCH (t:Teacher {{name: '{name}'}}) RETURN t"
        return self.database.execute_query(query)

    def find_teachers_by_name_starting_with(self, letter):
        query = f"MATCH (t:Teacher) WHERE t.name STARTS WITH '{letter}' RETURN t"
        return self.database.execute_query(query)

    def find_all_cities(self):
        query = "MATCH (c:City) RETURN c"
        return self.database.execute_query(query)

    def find_schools_by_number_range(self, min_number, max_number):
        query = f"MATCH (s:School) WHERE {min_number} <= s.number <= {max_number} RETURN s"
        return self.database.execute_query(query)
