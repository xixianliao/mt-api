from app.utils.translate import translate_text
from app.utils.utils import get_model_id
from .base_test_case import BaseTestCase


class TestTranslations(BaseTestCase):
    def test_translate_text_es_ca(self):
        model_id = get_model_id('es', 'ca')
        text = 'Hola, ¿Cómo estás?'
        expected_translation = 'Hola, com estàs?'
        translation = translate_text(model_id, text, 'es', 'ca')
        assert translation == expected_translation


    def test_translate_text_ca_es(self):
        model_id = get_model_id('ca', 'es')
        text = 'Hola, com estàs?'
        expected_translation = 'Hola, ¿cómo estás?'
        translation = translate_text(model_id, text, 'ca', 'es')
        assert translation == expected_translation
