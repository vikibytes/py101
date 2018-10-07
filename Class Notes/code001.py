import json
from urllib.request import urlopen

with urlopen("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=demo") as response:
    source = response.read()

data = json.loads(source)
print(data)
# print(json.dumps(data, indent=2)
