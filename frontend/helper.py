import requests

def get_image_url(query):
    UNSPLASH_ACCESS_KEY = 'YcIqAAMap9dKzxCXy5racBm9WD3ZxHUACw0mgUZeogE'
    endpoint = "https://api.unsplash.com/search/photos"
    params = {
        'query': query,
        'client_id': UNSPLASH_ACCESS_KEY,
        'per_page': 1
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    if data['results']:
        return data['results'][0]['urls']['regular']
    else:
        return None  # Return None if no images found
