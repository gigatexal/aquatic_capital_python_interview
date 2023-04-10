import pandas as pd
import datetime
from typing import TextIO

def process_csv(reader: TextIO, writer: TextIO):
    with reader as r:
        weather_data = pd.read_csv(r, parse_dates=['Measurement Timestamp'])
        # Station Name
        # Measurement Timestamp - convert to date
        # Air Temperature
        d: pd.DataFrame = weather_data[['Station Name', 'Measurement Timestamp', 'Air Temperature']]
        d1=d.assign(date=lambda x: x["Measurement Timestamp"].dt.date)
        print(d1)
