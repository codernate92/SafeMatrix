import json

def cleanup_log_data(log_data):
    """Clean up log data by normalizing and removing duplicates."""
    cleaned_data = []
    seen = set()  # To keep track of processed items and avoid duplicates

    for log in log_data:
        # Example cleanup: Remove logs with missing critical fields
        if 'timestamp' not in log or 'activity' not in log:
            continue

        # Normalize log structure (you can add more complex normalization here)
        log['timestamp'] = log['timestamp'].replace("T", " ")  # Convert timestamp format

        # Check for duplicates based on unique fields (e.g., event ID)
        event_id = log.get('event_id')
        if event_id and event_id not in seen:
            seen.add(event_id)
            cleaned_data.append(log)

    return cleaned_data

def process_logs(input_file, output_file):
    """Load, clean, and save log data."""
    with open(input_file, 'r') as f:
        logs = json.load(f)

    cleaned_logs = cleanup_log_data(logs)

    # Save cleaned logs to a new file
    with open(output_file, 'w') as f:
        json.dump(cleaned_logs, f, indent=2)

    print(f"Data cleaned and saved to {output_file}")

if __name__ == "__main__":
    # Example usage:
    input_log_file = 'raw_logs.json'  # Replace with your actual log file
    output_log_file = 'cleaned_logs.json'  # Output cleaned log file
    process_logs(input_log_file, output_log_file)
