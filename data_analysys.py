import pandas as pd
import json

# Load the JSON data
with open('final_data.json') as f:
    data = json.load(f)

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)
# print each row of the DataFrame
for i in range(len(df)):
    # print each column of the row if not none
    for j in range(len(df.iloc[i])):
        if df.iloc[i][j] != None:
            print(df.iloc[i][j])
