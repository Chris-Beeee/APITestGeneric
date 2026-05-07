import requests
from config.settings import settings

class APIClient:
    def __init__(self):
        self.base_url = settings.BASE_URL
        self.session = requests.Session()
        
        headers = {
            "Content-Type": "application/json"
        }
        
        # If an API key exists in settings, add it to the headers.
        # (Modify the header name 'x-api-key' based on your API's requirements)
        if settings.API_KEY:
            headers["x-api-key"] = settings.API_KEY
            
        self.session.headers.update(headers)

    def get(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, timeout=settings.TIMEOUT, **kwargs)
        return response

    def post(self, endpoint, data=None, json=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, data=data, json=json, timeout=settings.TIMEOUT, **kwargs)
        return response

    def put(self, endpoint, data=None, json=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, data=data, json=json, timeout=settings.TIMEOUT, **kwargs)
        return response

    def delete(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url, timeout=settings.TIMEOUT, **kwargs)
        return response
