import psycopg2
import yaml


def db_connection():
    config_file = 'pg/db_conf.yml'
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)

    connection = psycopg2.connect(
      dbname=config['dbname'],
      user=config['user'],
      password=config['password'],
      host=config['host'],
      port=config['port']
    )

    return connection
