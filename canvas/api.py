import requests
from .config import headers, school_path

def canvas_get(endpoint, params=None):
    url = f"{school_path}api/v1/{endpoint}"
    results = []
    
    #while loop for pagination
    while url:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        results.extend(response.json())

        # get the link labeled "next" in the response, if it doesn't exist we return None
        url = response.links.get("next", {}).get("url") 


    return results