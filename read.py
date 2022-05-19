import pandas as pd
import json

path = "monitor.json"
file = open(path)
info = json.load(file)

df = pd.json_normalize(info['rows'])
print(df)

df.to_csv("samplecsv.csv")