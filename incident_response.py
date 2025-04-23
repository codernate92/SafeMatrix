import requests
import json
import logging
from typing import Optional, Dict, Any

# Configure logging once at module level
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# API configurations
THEHIVE_BASE_URL = 'http://localhost:9000/api'
THEHIVE_API_KEY = 'your-hive-api-key'
CORTEX_API_URL = 'http://localhost:9001/api/invoke'
CORTEX_API_KEY = 'your-cortex-api-key'

# Shared headers
def get_auth_headers(api_key: str) -> Dict[str, str]:
    return {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

def enrich_case_with_cortex(case_id: str) -> Optional[Dict[str, Any]]:
    """
    Use Cortex to enrich data for a case.
    
    Args:
        case_id: The ID of the case to enrich
    Returns:
        Optional[Dict]: Enrichment data if successful, None otherwise
    """
    if not case_id or not CORTEX_API_KEY:
        logger.error("Case ID and API key are required")
        return None

    cortex_payload = {
        "identifier": "malware-analysis",
        "data": {
            "file": {
                "path": "/path/to/file",
                "hash": "sha256",
                "type": "file"
            }
        }
    }
    
    try:
        response = requests.post(
            CORTEX_API_URL,
            headers=get_auth_headers(CORTEX_API_KEY),
            json=cortex_payload
        )
        response.raise_for_status()
        return update_case_in_thehive(case_id, response.json())
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to enrich case: {str(e)}")
        return None

def update_case_in_thehive(case_id: str, enriched_data: Dict[str, Any]) -> bool:
    """Update the case in TheHive with enrichment data."""
    if not all([case_id, enriched_data, THEHIVE_API_KEY]):
        logger.error("Case ID, enriched data, and API key are required")
        return False

    try:
        response = requests.patch(
            f"{THEHIVE_BASE_URL}/case/{case_id}",
            headers=get_auth_headers(THEHIVE_API_KEY),
            json={
                "title": "Enriched Case Data",
                "description": f"Enriched data: {json.dumps(enriched_data)}"
            }
        )
        response.raise_for_status()
        logger.info(f"Case {case_id} updated successfully")
        return True
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to update case: {str(e)}")
        return False

if __name__ == "__main__":
    enrich_case_with_cortex("abc-123")
