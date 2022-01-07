import sys
import csv
import json

output = []
with open(sys.argv[1], "r") as CSV:
    reader = csv.DictReader(CSV)
    for row in reader:
        if row['Status'] == "succeeded":
            output.append({
                "Status": row['Status'],
                "Effective Donation": row['Effective Donation'],
                "Public Name": row['Public Name'],
                "Public Message": row['Public Message'],
            })
            
with open(sys.argv[1]+".json", "w") as JSON:
    JSON.write(json.dumps(output, indent=2, sort_keys=True))