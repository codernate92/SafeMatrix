import json
import requests

SPLUNK_HEC_URL = "https://your-splunk-hec-endpoint:8088/services/collector"
SPLUNK_TOKEN = "Your-Splunk-Token"

def send_to_splunk(event):
    headers = {
        "Authorization": f"Splunk {SPLUNK_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "event": event,
        "sourcetype": "aws:cloudtrail",
        "index": "main"
    }
    
    try:
        response = requests.post(SPLUNK_HEC_URL, headers=headers, data=json.dumps(payload), verify=False)
        if response.status_code == 200:
            print("[+] Sent event to Splunk.")
        else:
            print(f"[-] Splunk error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"[-] Exception sending to Splunk: {e}")
