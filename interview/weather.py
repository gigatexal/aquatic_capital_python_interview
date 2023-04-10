import pandas as pd
from typing import TextIO

def process_csv(reader: TextIO, writer: TextIO):
    with reader as r:
        weather_data = pd.read_csv(r, parse_dates=['Measurement Timestamp'])
        # Station Name
        # Measurement Timestamp - convert to date
        # Air Temperature
        d: pd.DataFrame = weather_data[['Station Name', 'Measurement Timestamp', 'Air Temperature']]
        d1: pd.DataFrame = d.assign(date=lambda x: x["Measurement Timestamp"].dt.date)
        del d # reduce mem usage?
        d1[['date']]=d1[['date']].apply(pd.to_datetime)
        # group by station name, measurement date, to get the min_temp, max temp
        min_temp = d1.groupby(['Station Name','date']).min()
        max_temp = d1.groupby(['Station Name','date']).max()
        first_temp = d1.groupby(['Station Name','date']).first()
        last_temp = d1.groupby(['Station Name','date']).last()
        print(min_temp, max_temp, first_temp, last_temp)
 
