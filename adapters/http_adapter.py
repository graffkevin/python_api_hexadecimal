from flask import Flask, request, jsonify
from adapters.postgres_adapter import PostgresAdapter
from ports.output_ports import DataOutPutPort

app = Flask(__name__)

class TypologyHttpAdapter(DataOutPutPort):
    def __init__(self, postgres_adapter):
        self.postgres_adapter = postgres_adapter
        
    def get_municipality_typology(self, code_insee: str) -> dict:
        typology_data = self.postgres_adapter.get_municipality_typology(code_insee)
        return typology_data

@app.route('/typology/<string:code_insee>', methods=['GET'])
def get_typology(code_insee):
    postgres_adapter = PostgresAdapter()
    typology_http_adapter = TypologyHttpAdapter(postgres_adapter)
    typology_data = typology_http_adapter.get_municipality_typology(code_insee)
    return jsonify(typology_data), 200
