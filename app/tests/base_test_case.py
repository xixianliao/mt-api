from fastapi.testclient import TestClient
from main import app

class BaseTestCase:
    def setup(self):
        self.client = TestClient(app)


class APIBaseTestCase(BaseTestCase):
    API_VERSION = 1
    SERVICE = 'translate'

    def get_endpoint(self, endpoint: str = '/') -> str:
        endpoint = f'/{endpoint}' if not endpoint.startswith('/') else endpoint
        return f'/api/v{self.API_VERSION}/{self.SERVICE}{endpoint}'
