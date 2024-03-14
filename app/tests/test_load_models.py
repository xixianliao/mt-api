import pytest
from .base_test_case import BaseTestCase


class TestLoadModels(BaseTestCase):

    @pytest.fixture(autouse=True)
    def setup_before_each_test(self):
        self.setup()

    def test_load_sigle_model_with_warnings(self):

        # languages
        assert self.config.language_codes == {'es': 'Spanish', 'ca': 'Catalan'}
        assert self.config.languages_list == {'ca': {'es': ['ca-es']}, 'es': {'ca': ['es-ca']}}

        # models
        assert len(self.config.loaded_models) == 2

        assert 'es-ca' in self.config.loaded_models
        model1 = self.config.loaded_models['es-ca']
        assert model1['src'] == 'es'
        assert model1['tgt'] == 'ca'

        assert 'ca-es' in self.config.loaded_models
        model2 = self.config.loaded_models['ca-es']
        assert model2['src'] == 'ca'
        assert model2['tgt'] == 'es'

        # pipeline
        # model1
        assert model1['sentence_segmenter'].__name__ == 'nltk_sentence_segmenter'
        assert len(model1['preprocessors']) == 1
        assert len(model1['postprocessors']) == 1
        assert 'get_sentencepiece_segmenter' in str(model1['preprocessors'])
        assert 'get_sentencepiece_desegmenter' in str(model1['postprocessors'])
        assert 'get_batch_ctranslator' in str(model1['translator'])

        # model2
        assert model2['sentence_segmenter'].__name__ == 'nltk_sentence_segmenter'
        assert len(model2['preprocessors']) == 1
        assert len(model2['postprocessors']) == 1
        assert 'get_sentencepiece_segmenter' in str(model2['preprocessors'])
        assert 'get_sentencepiece_desegmenter' in str(model2['postprocessors'])
        assert 'get_batch_ctranslator' in str(model2['translator'])
