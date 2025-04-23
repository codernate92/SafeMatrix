# SafeMatrix - Threat Detection and Response Tool

## Overview
SafeMatrix is an automated tool for processing AWS CloudTrail logs, detecting suspicious activities, and integrating with threat intelligence platforms like TheHive and Splunk.

### Features
- **CloudTrail Log Processing**: Automatically download and process CloudTrail logs from AWS S3.
- **Event Parsing**: Parse and enrich the logs with threat intelligence.
- **Threat Detection**: Identify suspicious activities in the logs.
- **Integrations**: TheHive for incident management, Splunk for SIEM.

## Requirements
- Python 3.x
- `boto3` (AWS SDK for Python)
- `requests` (for integrations with TheHive)
- `pytest` (for testing)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/safematrix.git
   cd safematrix
2. Install dependencies
pip install -r requirements.txt

3. Set up your AWS credentials for accessing CloudTrail logs.
4. To run the log processor: 
python main.py
5. Run test units (optional):
pytest test_log_processor.py
