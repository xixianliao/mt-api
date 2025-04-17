export MT_API_CONFIG=config.json
export MODELS_ROOT=./models
python -m nltk.downloader -d . punkt
#python main.py --models './models' --load MULTI-MULTI-salamandra-instruct 
python main.py  --load MULTI-MULTI-salamandra-instruct 