import os
import argparse
import uvicorn
from app import create_app

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejemplo de uso de argparse para el argumento -m/--models")
    parser.add_argument("-m", "--models", type=str, help="Modelos a utilizar", required=False)
    
    args = parser.parse_args()
    models = args.models
    if models:
        download_models = False
        os.environ['MODELS_ROOT'] = models
    else:
        download_models = True
    app = create_app(download_models)
    uvicorn.run(app, host="0.0.0.0", port=8001, log_config = "logging.yml")

else:
    app = create_app()