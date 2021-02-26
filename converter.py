import json
import pandas as pd


# Load data using Python JSON module.
# Replace '666.json' with the path where your JSON file located.
with open('666.json','r') as f:
    data = json.loads(f.read())

elements = {"tag": "Tags",
            "trigger": "Triggers",
            "variable": "User-Defined Variables",
            "builtInVariable": "Built-In Variables",
            "folder": "Folders",
            "zone": "Zones",
            "customTemplate": "Templates"}

# Change the name of the final xlsx file, if necessary
with pd.ExcelWriter('output-GTM.xlsx') as writer:
    for i in elements:
        if i in data["containerVersion"].keys():
            pd.json_normalize(data["containerVersion"][i]).to_excel(writer, sheet_name=elements[i], index=False)

print("Done.")
