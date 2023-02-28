"""
Foster Weather Station,01/01/2016 01:00:00 AM,67
Foster Weather Station,01/01/2016 12:00:00 AM,67

Then the expected values for start, end, high, and low for this day would be:

* start: 67
* end: 69
* high: 73
* low: 64

### Output format

The program should read the data from STDIN and output the aggregated data to STDOUT in CSV format. The resulting CSV should follow this format:

Station Name,Date,Min Temp,Max Temp,First Temp,Last Temp
Foster Weather Station,01/01/2016,64.0,73.0,67.0,69.0
Foster Weather Station,01/02/2016,21.0,32.0,22.1,30.3
...
"""
import csv
import datetime
from datetime import date, datetime
from dataclasses import dataclass

DATA = "./data/chicago_beach_weather.csv"



if __name__ == '__main__':
    @dataclass
    class Station:
        data: dict[str, dict[date, list[tuple[datetime, float]]]]

        @property
        def max_temp(self):
            pass

        @property
        def min_temp(self):
            pass

        @property
        def first_temp(self):
            pass

        @property
        def last_temp(self):
            pass

        def update(self, station: str, date: date, datetime: datetime, temp: float):
            if station not in self.data:
                self.data[station]={date:[]}
            self.data[station].setdefault(date, [])

    with open(DATA) as data:
        dict_reader: csv.DictReader = csv.DictReader(data)
        measurement_station = Station(data={})
        for item in dict_reader:
            
            # parse columns
            station: str = item["Station Name"]
            timestamp: datetime = datetime.strptime(item["Measurement Timestamp"], r"%m/%d/%Y %H:%M:%S %p")
            timestamp_as_date: date = timestamp.date()
            temperature: float = float(item["Air Temperature"])

            measurement_station.update(station=station, date=timestamp_as_date, datetime=timestamp, temp=temperature)
            print(measurement_station.data)
    
           
             

            
             
        









