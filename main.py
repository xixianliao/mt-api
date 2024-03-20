import os
import argparse
import uvicorn
from app import create_app

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejemplo de uso de argparse para el argumento -m/--models")
    parser.add_argument("-m", "--models", type=str, help="Path de los modelos descargados manualmente", required=False)
    parser.add_argument("-l", "--load", type=str, nargs="+", help="Opción para cargar modelos", default=["es-ca", "ca-es"])

    args = parser.parse_args()
    models = args.models
    models_to_load = args.load
    if 'all' in models_to_load:
        load_all_models = True
    else:
        load_all_models = False
    
    if models:
        download_models = False
        os.environ['MODELS_ROOT'] = models
    else:
        download_models = True

    app = create_app(download_models, load_all_models, models_to_load)
    uvicorn.run(app, host="0.0.0.0", port=8000, log_config = "logging.yml")

else:
    app = create_app(download_models=False, models_to_load=["es-ca", "ca-es"])