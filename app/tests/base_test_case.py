from fastapi.testclient import TestClient
from main import app
from app.helpers.config import Config

class BaseTestCase:
    def setup(self):
        self.client = TestClient(app)
        self.config_data = {
                "languages": {
                    "es": "Spanish",
                    "ca": "Catalan"
            },
            "models": [
                    {
                    "src": "ca",
                    "tgt": "es",
                    "model_type": "ctranslator2",
                    "model_path": "mt-aina-ca-es",
                    "src_sentencepiece_model": "spm.model",
                    "tgt_sentencepiece_model": "spm.model",
                    "load": True,
                    "sentence_split": "nltk",
                    "pipeline": {
                        "sentencepiece": True,
                        "translate": True
                    }
                    },
                    {
                    "src": "es",
                    "tgt": "ca",
                    "model_type": "ctranslator2",
                    "model_path": "mt-plantl-es-ca",
                    "src_sentencepiece_model": "spm.model",
                    "tgt_sentencepiece_model": "spm.model",
                    "load": True,
                    "sentence_split": "nltk",
                    "pipeline": {
                        "sentencepiece": True,
                        "translate": True
                    }
                    }
                ]
            }
        self.config = Config(config_data=self.config_data)


class APIBaseTestCase(BaseTestCase):
    API_VERSION = 1
    SERVICE = 'translate'

    def get_endpoint(self, endpoint: str = '/') -> str:
        endpoint = f'/{endpoint}' if not endpoint.startswith('/') else endpoint
        return f'/api/v{self.API_VERSION}/{self.SERVICE}{endpoint}'
