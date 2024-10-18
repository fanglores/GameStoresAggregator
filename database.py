import clickhouse_connect
from sensitive_data import CLICKHOUSE_USER, CLICKHOUSE_PASSWORD, CLICKHOUSE_HOST, CLICKHOUSE_PORT
import atexit

# Games Aggregator Database

CREATE_DB_COMMAND = """
CREATE DATABASE IF NOT EXISTS gad;
"""

CREATE_DB_TABLE_COMMAND = """
-- Prices table
CREATE TABLE IF NOT EXISTS gad.prices (
    id UUID DEFAULT generateUUIDv4(),
    game_name String,
    store_name String,
    price Float64,
    last_updated DateTime,
    PRIMARY KEY (id)
) ENGINE = MergeTree()
ORDER BY id;
"""

INSERT_DB_QUERY = """
INSERT INTO gad.prices (game_name, store_name, price, last_updated) 
VALUES (%s, %s, %s, %s);
"""

REMOVE_DB_QUERY = """
ALTER TABLE gad.prices DELETE WHERE game_name = %s AND store_name = %s;
"""

GET_DB_QUERY = """
SELECT * FROM gad.prices WHERE game_name = %s;
"""

GET_ALIKE_DB_QUERY = """
SELECT * FROM gad.prices WHERE game_name LIKE %s;
"""

try:
    print('Starting up a database')
    client = clickhouse_connect.get_client(
        host=CLICKHOUSE_HOST,
        port=CLICKHOUSE_PORT,
        username=CLICKHOUSE_USER,
        password=CLICKHOUSE_PASSWORD
    )

    print('Initializing database')
    client.command(CREATE_DB_COMMAND)
    client.command(CREATE_DB_TABLE_COMMAND)

    print('Database initiated successfully')

except Exception as e:
    print("Error while initializing database:", str(e))

def __shutdown_database():
    try:
        print('Shutdown database client')
        client.close()
    except Exception as e:
        print(f'Error: Database is probably already offline\nError description: {e}')

# Guarantees that scheduler will be stopped on exit
atexit.register(__shutdown_database)

def check_connection(attempts=3, delay=1):
    for attempt in range(1, attempts + 1):
        try:
            print(f'Checking database availability: {attempt}/{attempts} attempt...')
            client.query('SELECT version()')
            print('Database available')
            return True
        except Exception as e:
            print(f'Database in unavailable.' + f' Retry in {delay} seconds' if attempt < attempts else '')
            sleep(delay)

    print(f"Couldn`t connect to ClickHouse databse in {attempts} attempts.")
    return False

def update(data):
    try:
        print('Database update')
        client.command(REMOVE_DB_QUERY, (data['name'], data['source']))
        client.command(INSERT_DB_QUERY, (data['name'], data['source'], data['price'], data['datetime']))
        return True
    except Exception as e:
        print("Error while writing into database:", str(e))
        return False

def get(query):
    try:
        print('Database get')
        return client.execute(GET_ALIKE_DB_QUERY, (query['name']))
    except Exception as e:
        print("Error while reading from database:", str(e))
        return None