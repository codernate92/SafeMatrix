import boto3
import gzip
import json
from io import BytesIO
from integrations.thehive_client import TheHiveClient
from integrations.splunk_client import SplunkClient
from scripts.helpers import load_settings

settings = load_settings()
s3 = boto3.client('s3')
thehive_client = TheHiveClient(settings['thehive_api_url'], settings['thehive_api_key'])
splunk_client = SplunkClient(settings['splunk_api_url'], settings['splunk_api_key'])

def process_log_data(data):
    """Process decompressed log data (e.g., filter, extract specific fields)."""
    try:
        events = json.loads(data)
        for event in events.get('Records', []):
            print(json.dumps(event, indent=2))  # Print the event details
            # Additional processing logic can go here (filter, extract fields, etc.)
            # Example: Send to TheHive or Splunk
            thehive_client.send_event(event)
            splunk_client.send_event(event)
    except json.JSONDecodeError:
        print("Error decoding JSON data.")
    
def download_and_process_logs():
    contoinuation_token = None
    while True:
        try:
            response = s3.list_objects_v2(
                Bucket=settings['s3_bucket_name'],
                Prefix=settings['s3_prefix'],
                ContinuationToken=continuation_token if continuation_token else None
            )
            
            for obj in response.get('Contents', []):
                if obj['Key'].endswith('.gz'):
                    try:
                        # Download and decompress the log file
                        data = s3.get_object(Bucket=settings['s3_bucket_name'], Key=obj['Key'])['Body'].read()
                        decompressed = gzip.GzipFile(fileobj=BytesIO(data)).read()
                        process_log_data(decompressed)
                    except Exception as e:
                        print(f"Error processing {obj['Key']}: {e}")
            
            # Check if there are more pages
            continuation_token = response.get('NextContinuationToken')
            if not continuation_token:
                break  # Exit the loop if there are no more pages
        except Exception as e:
            print(f"Error listing objects: {e}")
            break