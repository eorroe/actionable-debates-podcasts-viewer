import json
import os

files = [f for f in os.listdir('.') if f.endswith('.json3')]
if not files:
    print("No json3 files found")
    exit(1)

filename = files[0]
print(f"Reading: {filename}")

with open(filename, 'r') as f:
    data = json.load(f)

# Print structure
print("Keys:", list(data.keys()) if isinstance(data, dict) else "List")

if isinstance(data, dict):
    if 'events' in data:
        print(f"Number of events: {len(data['events'])}")
        # Print first few events
        for i, event in enumerate(data['events'][:5]):
            print(f"Event {i}: {json.dumps(event, indent=2)[:500]}")
    else:
        print("No 'events' key found")
        print("Sample:", json.dumps(data, indent=2)[:1000])
elif isinstance(data, list):
    print(f"List of {len(data)} items")
    if data:
        print("First item:", json.dumps(data[0], indent=2)[:500])
