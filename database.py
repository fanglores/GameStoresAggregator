from clickhouse_connect import get_client
from sensitive_data import CLICKHOUSE_USER, CLICKHOUSE_PASSWORD

# Конфигурация ClickHouse
CLICKHOUSE_HOST = 'localhost'
CLICKHOUSE_PORT = 8123
CLICKHOUSE_DATABASE = 'games_aggregator_db'

# Инициализация клиента ClickHouse
client = get_client(
    host=CLICKHOUSE_HOST,
    port=CLICKHOUSE_PORT,
    username=CLICKHOUSE_USER,
    password=CLICKHOUSE_PASSWORD,
    database=CLICKHOUSE_DATABASE
)

client.execute("""
    CREATE DATABASE IF NOT EXISTS games_aggregator_db;
    
    -- Stores table
    CREATE TABLE IF NOT EXISTS games_aggregator_db.stores (
        id UUID DEFAULT generateUUIDv4(),
        name String,
        PRIMARY KEY (id)
    ) ENGINE = MergeTree()
    ORDER BY id;
    
    -- Games table
    CREATE TABLE IF NOT EXISTS games_db.games (
        id UUID DEFAULT generateUUIDv4(),
        name String,
        PRIMARY KEY (id)
    ) ENGINE = MergeTree()
    ORDER BY id;
    
    -- Prices table
    CREATE TABLE IF NOT EXISTS games_db.prices (
        id UUID DEFAULT generateUUIDv4(),
        game_uid UUID,
        store_uid UUID,
        price Float64,
        currency String,
        last_updated DateTime,
        PRIMARY KEY (id)
    ) ENGINE = MergeTree()
    ORDER BY id;
    
    -- Indexing
    CREATE INDEX idx_game_name ON games_aggregator_db.games (name) TYPE bloom_filter(0.01) GRANULARITY 64;
    CREATE INDEX idx_store_name ON games_aggregator_db.sources (name) TYPE bloom_filter(0.01) GRANULARITY 64;
""")

def database_update():
    pass

def database_get():
    pass