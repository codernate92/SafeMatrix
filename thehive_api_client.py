import json
import requests

# TheHive API Configuration
THEHIVE_URL = 'https://your-thehive-instance/api'  # Replace with your TheHive URL
THEHIVE_API_KEY = 'your-api-key'  # Replace with your actual API key

def create_case_in_thehive(suspicious_activity):
    """Create a case in TheHive based on suspicious activity."""
    headers = {
        "Authorization": f"Bearer {THEHIVE_API_KEY}",
        "Content-Type": "application/json"
    }

    case_data = {
        "title": f"Suspicious Activity Detected: {suspicious_activity['alert_type']}",
        "description": suspicious_activity['details'],
        "type": "Alert",  # Modify based on your case type
        "severity": suspicious_activity.get('severity', 'Medium'),
        "status": "Open",
        "tags": ["suspicious", "security", "high-priority"],  # Add your tags
        "observedDate": suspicious_activity.get('timestamp')
    }

    response = requests.post(f'{THEHIVE_URL}/case', json=case_data, headers=headers)

    if response.status_code == 200:
        print(f"Case created in TheHive: {suspicious_activity['alert_type']}")
    else:
        print(f"Failed to create case in TheHive: {response.text}")

if __name__ == "__main__":
    # Example usage:
    sample_activity = {
        "alert_type": "Suspicious Login Attempt",
        "details": "Multiple failed login attempts detected.",
        "severity": "High",
        "timestamp": "2025-04-24T12:34:56Z"
    }

    create_case_in_thehive(sample_activity)  # Send test activity
