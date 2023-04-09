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

@dataclass
class Row:
    station: str
    ts: datetime
    ts_as_date: date
    temps: list[tuple[datetime, float]]

    def add_temp(self, ts: datetime, temperature: float):
        self.temps.append((ts, temperature))

    @property
    def min_temp(self):
        return sorted



if __name__ == '__main__':
    # construct a balanced tree for each station and then each date
    # rebalance on each insert so that the main node is the first date or oldest date and the last is the most recent
    # mayne not a tree but a list of tuples could do this
    # perhaps the row class is fine if it just inherited from tuple instead of being a dataclass
    # namedtuple?
    # or just make Row sortable?
    # https://stackoverflow.com/questions/7152497/making-a-python-user-defined-class-sortable-hashable
    grouped_entries: dict[tuple, Row]
    grouped_entries = {}
    with open(DATA) as data:
        dict_reader: csv.DictReader = csv.DictReader(data)
        for item in dict_reader:
            
            # parse columns
            station: str = item["Station Name"]
            timestamp: datetime = datetime.strptime(item["Measurement Timestamp"], r"%m/%d/%Y %H:%M:%S %p")
            timestamp_as_date: date = timestamp.date()
            temperature: float = float(item["Air Temperature"])
            
            # helpers
            key = (station, timestamp)
            if key not in grouped_entries:
                grouped_entries.setdefault(key, \
                        Row(station=station, ts=timestamp, ts_as_date=timestamp_as_date, temps=[(timestamp, temperature)]))

            else:
                grouped_entries[key].add_temp(timestamp, temperature)

    print(grouped_entries)






             
           
             

            
             
        









