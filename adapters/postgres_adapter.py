from pg.db_connection import db_connection
from ports.output_ports import DataOutPutPort


class PostgresAdapter(DataOutPutPort):
    def __init__(self):
        self.connection = db_connection()
        
    def get_municipality_typology(self, code_insee: str) -> dict:
        conn = self.connection
        cur = self.connection.cursor()

        try:
            cur.callproc('get_urban_typology', (code_insee,))
            result = cur.fetchone()
        except Exception as e:
            result = None
            raise ('Error: ', str(e))

        cur.close()
        conn.close()

        if result:
            typology_data = {'code': result[0], 'lib': result[1]}
            return typology_data
        return None
