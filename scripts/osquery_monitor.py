import os
import json
def query_osquery(query):
    result = os.popen(f"osqueryi --json 'SELECT * FROM logged_in_users;'").
    parsed = json.loads(result)
    for row in parsed:
        print(f"User: {row['username']}, Login Time: {row['time']}")
