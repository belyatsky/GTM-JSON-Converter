import json
import pandas as pd


# Load data using Python JSON module.
# Replace '666.json' with the path where your JSON file located.
# Make sure you placed your file into 
with open('666.json','r') as f:
    data = json.loads(f.read())

json_tags = data["containerVersion"]["tag"]
json_triggers = data["containerVersion"]["trigger"]
json_variables_custom = data["containerVersion"]["variable"]
json_variables_builtIn = data["containerVersion"]["builtInVariable"]

elements = ["tag", "trigger", "variable", "builtInVariable", "folder"]
tabs = []

for el in elements:
    if el in data["containerVersion"].keys():
        tabs.append(el)

# Change the name of the final xlsx file, if necessary
with pd.ExcelWriter('output-GTM.xlsx') as writer:
    for i in tabs:
        pd.json_normalize(data["containerVersion"][i]).to_excel(writer, sheet_name=i, index=False)
