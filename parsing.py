import  pandas as pd
import json



df = pd.read_excel('test.xlsx',sheet_name='Variant')

print(df.columns)

data = {df}

def convert_to_json(data):
    with open('new_file.json', 'w') as f:
        json.dump(data, f, indent=2)
convert_to_json(data)