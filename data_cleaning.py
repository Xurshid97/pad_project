import pandas as pd
import json

# Load the JSON data
with open('./unstructured_scrapping/failed_starts/final_data_failed_startups.json') as f:
    data = json.load(f)

def converter(data):
    columns = ['Country:', 'Industry:', 'Started in:', 'Closed in:','Nº of employees:', 'Funding Amount:', 'Specific cause of failure:']
    converted_data = [columns]
    
    # flatten the data
    data = [item for sublist in data for item in sublist]
    merged_data = []
    for i in range(len(data)):
        merged_dict = {}
        for dict_ in data[i]:
            merged_dict.update(dict_)
        merged_data.append(merged_dict)
    
    for i in range(len(merged_data)):
        appendable = []
        for name in columns:
            if name in merged_data[i]:
                if name == 'Funding Amount:':
                    if '-' in merged_data[i][name]:
                        appendable.append(merged_data[i][name].split('-')[0])
                    elif '<' in merged_data[i][name]:
                        appendable.append(merged_data[i][name].split('<')[1])
                    elif '>' in merged_data[i][name]:
                        appendable.append(merged_data[i][name].split('>')[1])
                    else:
                        appendable.append(merged_data[i][name])
                else:
                    appendable.append(merged_data[i][name])
            elif name == 'Nº of employees:' and 'Nº of employees' not in merged_data[i]:
                appendable.append('1')
            elif name == 'Funding Amount:' and 'Funding Amount:' not in merged_data[i]:
                appendable.append('$0')
            elif name == 'Specific cause of failure:' and 'Specific cause of failure:' not in merged_data[i]:
                appendable.append('')
        converted_data.append(appendable)
    
    return converted_data

converted_data = converter(data)

df = pd.DataFrame(converted_data[1:], columns=converted_data[0])
# print(df.head())
# save the DataFrame to a Excel file into folder structured_data
df.to_excel('./structured_data/failed/final_data_failed.xlsx', index=False)



with open('./unstructured_scrapping/success_start/final_data_successfull_startups.json') as f:
    data = json.load(f)



def converter(data):
    columns = ['State', 'Started in', 'Industries', 'Number of employees', 'Funding', 'Number of investors']
    converted_data = [columns]
    
    for i in range(len(data)):
        for j in range(len(data[i])):
            appendable = []
            for k in range(len(data[i][j])):
                entry = data[i][j][k]
                for name in columns:
                    if name in entry:
                        if name == 'Number of investors' and entry[name] != '':
                            appendable.append(entry[name].split(' ')[0])
                        elif name == 'Number of employees' and entry[name] != '':
                            appendable.append(entry[name].split('-')[0])
                        elif name == 'Industries' and entry[name] != '':
                            appendable.append(entry[name].split(',')[0])
                        else:
                            appendable.append(entry[name])
            # Verify the length of appendable before adding it to converted_data
            if len(appendable) <= len(columns):
                converted_data.append(appendable)
    
    return converted_data

converted_data = converter(data)
# Create a DataFrame
df = pd.DataFrame(converted_data[1:], columns=converted_data[0])

cleaned_data = []
for i in range(len(df)):
    cleaned_row = []
    for j in range(len(df.iloc[i])):
        if df.iloc[i][j] == '' or df.iloc[i][j] == None:
            cleaned_row = None
            break
        else:
            cleaned_row.append(df.iloc[i][j])
    cleaned_data.append(cleaned_row)

remove_none = []
for i in range(len(cleaned_data)):
    if cleaned_data[i] != None:
        remove_none.append(cleaned_data[i])


df = pd.DataFrame(remove_none, columns=converted_data[0])
# print(df)
# save the DataFrame to a Excel file into folder structured_data
df.to_excel('./structured_data/success/final_success_data.xlsx', index=False)
