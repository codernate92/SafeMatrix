import boto3
import gzip
import json
from io import BytesIO

from thehive_client import create_case
from osquery_monitor import collect_osquery_data
from helpers import load_threatintel_csv

# Optional: from splunk_forwarder import send_to_splunk

bucket_name = 'aws-cloudtrail-logs-129543046295-50fd0d6b'
prefix = 'AWSLogs/129543046295/'

s3 = boto3.client('s3')

def process_log_data(data, threatintel):
    try:
        events = json.loads(data)
        for event in events.get('Records', []):
            user_identity = event.get("userIdentity", {})
            source_ip = event.get("sourceIPAddress", "")
            event_name = event.get("eventName", "")
            
            match = next((ti for ti in threatintel if ti['ioc'] in json.dumps(event)), None)
            if match:
                print(f"[!] Match found: {match['ioc']}")
                
                # Create a case in TheHive
                create_case(
                    title=f"Threat Match: {match['ioc']}",
                    description=f"Detected in CloudTrail: {event_name} from {source_ip}",
                    tags=["cloudtrail", "threatintel"]
                )
                
                # Optional: send to Splunk
                # send_to_splunk(event)
            else:
                print("[+] No match. Skipping.")
    except json.JSONDecodeError:
        print("[-] Error decoding JSON data.")

def download_and_process_logs():
    continuation_token = None
    threatintel = load_threatintel_csv("threatintel.csv")
    
    while True:
        response = s3.list_objects_v2(
            Bucket=bucket_name,
            Prefix=prefix,
            ContinuationToken=continuation_token if continuation_token else None
        )
        for obj in response.get('Contents', []):
            if obj['Key'].endswith('.gz'):
                data = s3.get_object(Bucket=bucket_name, Key=obj['Key'])['Body'].read()
                decompressed = gzip.GzipFile(fileobj=BytesIO(data)).read()
                process_log_data(decompressed, threatintel)

        continuation_token = response.get('NextContinuationToken')
        if not continuation_token:
            break

if __name__ == "__main__":
    print("[*] Running OSQuery monitor...")
    collect_osquery_data()
    
    print("[*] Processing AWS logs...")
    download_and_process_logs()
