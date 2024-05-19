export MT_API_CONFIG=config.json
export MODELS_ROOT=./models
python -m nltk.downloader punkt
python main.py --models './models'