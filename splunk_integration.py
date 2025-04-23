import requests
import json

THEHIVE_API_URL = 'http://localhost:9000/api/case/_search'
THEHIVE_API_KEY = 'your-hive-api-key'
SPLUNK_API_URL = 'https://splunk.example.com:8089/services/search/jobs/export'

def send_event_to_splunk(event_data):
    """Send event data to Splunk."""
    headers = {
        'Authorization': 'Splunk your_splunk_token',
        'Content-Type': 'application/json'
    }

    payload = {
        "event": event_data,
        "sourcetype": "json",
        "index": "your_index"
    }
    response = requests.post(
        SPLUNK_API_URL,
        headers=headers,
        data=json.dumps(payload)
    )
    if response.status_code == 200:
        print(f"Event data sent to Splunk successfully: {response.json()}")
    else:
        print(f"Failed to send event data to Splunk: {response.status_code} - {response.text}")

#Example event data to send to Splunk
event_data = {
    "source": "AWS CloudTrail",
    "message": "Suspicious activity detected in AWS CloudTrail logs.",
    "timestamp": "2023-10-01T12:00:00Z"
}
# Send the event data to Splunk
send_event_to_splunk(event_data)