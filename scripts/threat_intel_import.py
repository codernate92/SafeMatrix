import requests
import csv

THEHIVE_API_URL = 'http://localhost:9000/api/case/_search'
THEHIVE_API_KEY = 'your-hive-api-key'

def import_threat_intelligence(file_path):
    """Import threat intelligence data from a CSV file into TheHive."""
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {THEHIVE_API_KEY}'
    }

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Prepare the payload for TheHive
            payload = {
                "title": row.get('title'),
                "description": row.get('description'),
                "severity": row.get('severity'),
                "type": row.get('type'),
                "source": row.get('source'),
                "tlp": row.get('tlp'),
                "tags": row.get('tags').split(',') if row.get('tags') else [],
                "observables": [
                    {
                        "dataType": "ip",
                        "data": row.get('ip')
                    },
                    {
                        "dataType": "domain",
                        "data": row.get('domain')
                    }
                ]
            }

            # Send the data to TheHive
            response = requests.post(
                f"{THEHIVE_API_URL}/case",
                headers=headers,
                json=payload
            )
            if response.status_code == 201:
                print(f"Threat intelligence data imported successfully: {response.json()}")
            else:
                print(f"Failed to import threat intelligence data: {response.status_code} - {response.text}")
# Example usage
import_threat_intelligence('threat_intel.csv')