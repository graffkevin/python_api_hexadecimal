import psycopg2
from ports.output_ports import DataOutPutPort

class PostgresAdapter(DataOutPutPort):
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname="geofalco",
            user='geouser',
            password='geopassword',
            host='127.0.0.1',
            port='5433'    
        )
        with open('queries/typology.sql', 'r') as file:
            self.typology_query = file.read()

    def get_municipality_typology(self, code_insee: str) -> dict:
        conn = self.connection
        cur = self.connection.cursor()
        
        query = self.typology_query
        try:
            cur.execute(query, (code_insee,))
            result = cur.fetchone()
        except Exception as e:
            result = None
            raise ('Error: ', e)
        
        cur.close()
        conn.close()
        
        if result:
            typology_data = {'code': result[0], 'lib': result[1]}
            return typology_data
        return None