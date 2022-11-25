import pandas as pd
from sqlalchemy import Table, Column, Integer, Float, String, DateTime, MetaData
from sqlalchemy import create_engine

data_s = pd.read_csv (r'C:\Users\magda\modul_6\clean_stations.csv')   
df_s = pd.DataFrame(data_s)

data_m = pd.read_csv (r'C:\Users\magda\modul_6\clean_measure.csv')   
df_m = pd.DataFrame(data_m)

# create connection between two DB
station_together = pd.merge(df_s, df_m, on='station', how='outer')

#create engine and connect to DB
engine = create_engine(r"sqlite:///stations_data.db")

meta = MetaData()

station = Table(
    "stations", meta,
    Column("station", String),
    Column("latitude", Float),
    Column("longitude", Float),
    Column("elevation", Float),
    Column("name", String),
    Column("country", String),
    Column("state", String),
)

measure = Table(
    "measures", meta,
    Column("station", String),
    Column("date", DateTime),
    Column("precip", Float),
    Column("tobs", Integer),
)

stations_all_data = Table(
    "stations_all_data", meta,
    Column("station", String),
    Column("latitude", Float),
    Column("longitude", Float),
    Column("elevation", Float),
    Column("name", String),
    Column("country", String),
    Column("state", String),
    Column("station", String),
    Column("date", DateTime),
    Column("precip", Float),
    Column("tobs", Integer),
)

meta.create_all(engine)
print(engine.table_names())

conn = engine.connect() 
df_s.to_sql('stations', conn, if_exists='append',index=False)
df_m.to_sql('measures', conn, if_exists='append',index=False)
station_together.to_sql('stations_all_data', conn, if_exists='append',index=False)