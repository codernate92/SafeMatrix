import requests
import json 

THEHIVE_API_URL = 'http://localhost:9000/api/case/_search'
THEHIVE_API_KEY = 'your-hive-api-key'

def send_log_to_thehive(log_data):
    """Send log data to TheHive."""
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {THEHIVE_API_KEY}'
    }

    # Example log data format for creating a case in TheHive
    payload = {
        "title": f"Log analysis from {log_data.get('source')}",
        "description": f"Details: {log_data.get('message')}",
        "observedTime": log_data.get('timestamp'),
        "severity": 3,
        "type": "event"
    }

    #Send the data to TheHive
    response = requests.post(
        f"{THEHIVE_API_URL}/case",
        headers=headers,
        data=json.dumps(payload)
    )
    if response.status_code == 201:
        print(f"Log data sent to TheHive successfully: {response.json()}")
    else:
        print(f"Failed to send log data to TheHive: {response.status_code} - {response.text}")
    
# Example log data to send to TheHive
log_data = {
    "source": "AWS CloudTrail",
    "message": "Suspicious activity detected in AWS CloudTrail logs.",
    "timestamp": "2023-10-01T12:00:00Z"
}
# Send the log data to TheHive
send_log_to_thehive(log_data)