import json
import pandas as pd


# Load data using Python JSON module.
# Replace '666.json' with the path where your JSON file located.
with open('666.json','r') as f:
    data = json.loads(f.read())

elements = ["tag", "trigger", "variable", "builtInVariable", "folder", "zone", "customTemplate"]
tabs = []

for el in elements:
    if el in data["containerVersion"].keys():
        tabs.append(el)

# Change the name of the final xlsx file, if necessary
with pd.ExcelWriter('output-GTM.xlsx') as writer:
    for i in tabs:
        pd.json_normalize(data["containerVersion"][i]).to_excel(writer, sheet_name=i, index=False)
