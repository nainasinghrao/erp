from  connection_db import engine


with engine.connect() as con:
    print("Connected")
