import sqlalchemy
print(sqlalchemy.__version__)

from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db')
print(engine.driver)
print(engine.table_names())
results = engine.execute("SELECT * FROM projects")
for r in results:
    print(r)



