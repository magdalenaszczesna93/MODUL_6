import pandas as pd
from sqlalchemy import Table, Column, Integer, Float, String, DateTime, MetaData
from sqlalchemy import create_engine

data = pd.read_csv (r'C:\Users\magda\modul_6\clean_stations.csv')   
df = pd.DataFrame(data)
print(df)

#create engine and connect to DB
engine = create_engine(r"sqlite:///stations_data.db")
print(engine.driver)



# stations: station- string,latitude-float,longitude-float,elevation-float,name-string,country-string,state-string
# measure: station- string,date-datetime.date,precip-float,tobs-int