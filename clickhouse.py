
from clickhouse_sqlalchemy import (
    Table, make_session, get_declarative_base, types, engines
)
from sqlalchemy import create_engine, Column, MetaData
from clickhouse_driver import Client

HOST = 'localhost'
client = Client(host=HOST)


res = client.execute("SHOW DATABASES")
print(res)

if "cti" in res:
    client.execute("DROP DATABASE cti")
client.execute("CREATE DATABASE IF NOT EXISTS cti")

CLICKHOUSE_URI = 'clickhouse+native://localhost/cti'
BROKER_LIST='local:9092'
FORMAT = 'AvroConfluent'
AVRO_SCHEMA_REGISTRY_URL = 'http://local:8081'


engine = create_engine(CLICKHOUSE_URI)
session = make_session(engine)
metadata = MetaData(bind=engine)

Base = get_declarative_base(metadata=metadata)

