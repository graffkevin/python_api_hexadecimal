from ports.output_ports import DataOutPutPort

class GetTypologyUseCase(DataOutPutPort):
    def __init__(self, typology_output_port):
        self.typology_output_port = typology_output_port
    
    def get_municipality_typology(self, code_insee: str) -> dict:
        typology_data = self.typology_output_port.get_municipality_typology_by_code(code_insee)
        return typology_data