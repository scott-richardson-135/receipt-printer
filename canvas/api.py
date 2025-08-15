import requests
from .config import headers, school_path

def canvas_get(endpoint, params=None):
    url = f"{school_path}api/v1/{endpoint}"
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()