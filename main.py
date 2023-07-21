from adapters.http_adapter import app, TypologyHttpAdapter
from core.use_case import GetTypologyUseCase
from adapters.postgres_adapter import PostgresAdapter

if __name__ == '__main__':
    postgres_adapter = PostgresAdapter()
    typology_http_adapter = TypologyHttpAdapter(postgres_adapter)
    get_typology_use_case = GetTypologyUseCase(typology_http_adapter)
    app.run()