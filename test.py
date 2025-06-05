from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgre:1234@localhost:5050/testdb"

try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("Bağlantı başarılı!")
    connection.close()
except Exception as e:
    print(f"Bağlantı hatası: {e}")


