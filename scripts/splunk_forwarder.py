import json
import requests

# Splunk HEC Configuration
SPLUNK_URL = 'https://your-splunk-instance:8088/services/collector/event'  # Replace with your Splunk HEC URL
SPLUNK_TOKEN = 'your-splunk-token'  # Replace with your actual Splunk token

def send_alert_to_splunk(alert_data):
    """Send alerts to Splunk using HEC."""
    headers = {
        "Authorization": f"Splunk {SPLUNK_TOKEN}",
        "Content-Type": "application/json"
    }

    # Send each alert data as a separate event to Splunk
    for alert in alert_data:
        payload = {
            "event": json.dumps(alert),
            "index": "main",  # Modify to your desired index
            "sourcetype": "_json"  # Modify to your desired sourcetype
        }

        response = requests.post(SPLUNK_URL, json=payload, headers=headers)

        if response.status_code == 200:
            print(f"Alert successfully sent to Splunk: {alert}")
        else:
            print(f"Failed to send alert to Splunk: {response.text}")

if __name__ == "__main__":
    # Example usage:
    sample_alert = {
        "alert_type": "Suspicious Activity",
        "details": "Suspicious login detected",
        "severity": "High",
        "timestamp": "2025-04-24T12:34:56Z"
    }

    send_alert_to_splunk([sample_alert])  # Send test alert
