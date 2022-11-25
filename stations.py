import pandas as pd
from sqlalchemy import Table, Column, Integer, Float, String, DateTime, MetaData
from sqlalchemy import create_engine

data_s = pd.read_csv (r'C:\Users\magda\modul_6\clean_stations.csv')   
df_s = pd.DataFrame(data_s)
print(df_s)

data_m = pd.read_csv (r'C:\Users\magda\modul_6\clean_measure.csv')   
df_m = pd.DataFrame(data_m)
print(df_m)

#create engine and connect to DB
engine = create_engine(r"sqlite:///stations_data.db")

meta = MetaData()

# stations: station- string,latitude-float,longitude-float,elevation-float,name-string,country-string,state-string
# measure: station- string,date-datetime.date,precip-float,tobs-int

station = Table(
    "stations", meta,
    Column("station", String, primary_key=True),
    Column("latitude", Float),
    Column("longitude", Float),
    Column("elevation", Float),
    Column("name", String),
    Column("country", String),
    Column("state", String),
)

mesure = Table(
    "measures", meta,
    Column("station", String),
    Column("date", DateTime),
    Column("precip", Float),
    Column("tobs", Integer),
)

meta.create_all(engine)
print(engine.table_names())

