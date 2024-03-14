import json
from fastapi.testclient import TestClient
from main import app
from app.helpers.config import Config
from app.settings import (CONFIG_JSON_PATH)

class BaseTestCase:
    def setup(self):
        with open(CONFIG_JSON_PATH, 'r') as jsonfile:
            self.config_data = json.load(jsonfile)
        
        self.config = Config(config_data=self.config_data)
        self.client = TestClient(app)


class APIBaseTestCase(BaseTestCase):
    API_VERSION = 1
    SERVICE = 'translate'

    def get_endpoint(self, endpoint: str = '/') -> str:
        endpoint = f'/{endpoint}' if not endpoint.startswith('/') else endpoint
        return f'/api/v{self.API_VERSION}/{self.SERVICE}{endpoint}'
