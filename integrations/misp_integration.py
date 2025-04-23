import requests
import yaml

def load_misp_config(config_path='config/misp_settings.yaml'):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def query_misp(ioc_value, misp_config):
    url = f"{misp_config['misp_url']}/attributes/restSearch/json"
    headers = {
        "Authorization": misp_config['misp_api_key'],
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    data = {
        "value": ioc_value
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[!] MISP query failed: {e}")
        return None

if __name__ == '__main__':
    config = load_misp_config()
    result = query_misp("8.8.8.8", config)
    print(result)
