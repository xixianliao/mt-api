from fastapi.testclient import TestClient
from app import create_app
import os

class BaseTestCase:

    def setup(self):
        os.environ['MODELS_ROOT'] = "./models"
        self.app = create_app(models_to_load=["es-ca", "ca-es"])
        self.client = TestClient(self.app)


class APIBaseTestCase(BaseTestCase):
    API_VERSION = 1
    SERVICE = 'translate'

    def get_endpoint(self, endpoint: str = '/') -> str:
        endpoint = f'/{endpoint}' if not endpoint.startswith('/') else endpoint
        return f'/api/v{self.API_VERSION}/{self.SERVICE}{endpoint}'
