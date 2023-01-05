import os, sys, json
import argparse

class NetworkConfig():
    try:
        from fastapi import FastAPI
        from pydantic import BaseSettings
        from fastapi.middleware.cors import CORSMiddleware
        from fastapi.middleware.gzip import GZipMiddleware
        from starlette.middleware.sessions import SessionMiddleware
        from starlette.requests import Request
    
        class Settings(BaseSettings):
            app_name = "Keras Bot"
            items_per_user: int = 50
            web_scheme: str = "http"
            address: str = "127.0.0.1"
            port: int = 8000
        
        settings = Settings()
        app = FastAPI(title=settings.app_name)

        #CERTIFICATE_PATH = os.path.join(root_path, "app/security/certificates/certificate_name.crt").replace("\\", "/")
        #PRIVATE_KEY_PATH = os.path.join(root_path, "app/security/certificates/certificate_name.key").replace("\\", "/")
        # Generated with:
        # import secrets
        # secrets.token_hex(16)
        SECRET_KEY = "75ffebf419f166434eb0f9ced0a28eb7"
        app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
        ALLOWED_HOSTS = ["*"]
        app.add_middleware(CORSMiddleware, allow_origins=ALLOWED_HOSTS, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
        app.add_middleware(GZipMiddleware, minimum_size=1000)

        async def catch_exceptions_middleware(request: Request, call_next):
            try:
                return await call_next(request)
            except Exception:
                from starlette.responses import Response
                # you probably want some kind of logging here
                return Response("Internal server error", status_code=500)
        app.middleware('http')(catch_exceptions_middleware)
    except ImportError as e:
        pass


class ArgConfig():
    @classmethod
    def args(cls):
        #Handle the parameters for the application
        parser = argparse.ArgumentParser(prog = 'Karas cuDNN', description = 'A chat bot based on deep learning, using karas, tensorflow and cuDNN', add_help=False)
        parser.add_argument('-help', '--help', action='store_true', default=False)
        parser.add_argument('-train', '--train', action='store_true', default=False)
        parser.add_argument('-version', '--version', action='store_true', default=False)
        parser.add_argument('-install', '--install', action='store_true', default=False)
        parser.add_argument('-uninstall', '--uninstall', action='store_true', default=False)
        parser.add_argument('-clean', '--clean', action='store_true', default=False)
        parser.add_argument('-chat', '--chat', action='store_true', default=False)
        parser.add_argument('-api', '--api', action='store_true', default=False)
        listed_arguments = parser.parse_args()
        
        args = []
        for argument in vars(listed_arguments):
            if getattr(listed_arguments, argument):
                args.append(argument)

        if (len(args) >= 2):
            print("Too many arguments, please use only one argument at a time")
            sys.exit(0)
        
        if (len(args) == 0):
            print("No argument provided, please use -help to see the list of available arguments")
            sys.exit(0)

        exec_mudule = str(args[0]).lower()
        return exec_mudule


class VenvConfig():
    @classmethod
    def __get_base_prefix_compat(cls):
        """Get base/real prefix, or sys.prefix if there is none."""
        return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

    @classmethod
    def ensure_virtualenv(cls):
        if not cls.__get_base_prefix_compat() != sys.prefix:
            msg = "Please activate the virtual environment before running the application\n"
            msg += "To create the virtual environment, run the following command (without quotes):\n"
            msg += "    - 'python -m venv venv'\n"
            msg += "To activate the virtual environment, run the following command (without quotes):\n"
            msg += "    - 'venv\\Scripts\\activate'\n"
            print(msg)
            sys.exit(0)
        


class Config:
    VenvConfig.ensure_virtualenv()
    
    #Handle all the configuration for the bots training and data models
    def load_intents(path):
        #load all .json file in training_data folder recursively
        intents = { "intents": [] }
        for root, dirs, files in os.walk(path):
            for file in files:
                if file == "settings.json":
                    continue

                if file.endswith(".json"):
                    json_data = json.loads(open(os.path.join(root, file)).read())
                    for index, intent in  enumerate(json_data["intents"]):
                        json_data["intents"][index]["tag"] = file.replace(".json", "") + "__" + json_data["intents"][index]["tag"]
                    intents["intents"].extend(json_data["intents"])
        return intents

    ROOT_PATH = os.getcwd()
    TRAINING_PATH = os.path.join(os.getcwd(), "src", "training", "training_data")
    TRAINING_SETTINGS = json.loads(open(os.path.join(TRAINING_PATH, "settings.json")).read())
    INTENTS = load_intents(TRAINING_PATH)

    TRAINED_PATH = os.path.join(os.getcwd(), "src", "training", "trained_data")
    TRAINED_WORDS = os.path.join(TRAINED_PATH, "words.pkl")
    TRAINED_CLASSES = os.path.join(TRAINED_PATH, "classes.pkl")
    TRAINED_MODEL = os.path.join(TRAINED_PATH, "chatbot_model.h5")
    network = None

    exec_mudule = ArgConfig.args()

    if (exec_mudule == "api"):
        network = NetworkConfig()

config = Config()