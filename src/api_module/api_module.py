import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve

from src.config import config, network
#from src.api_module.routes.api import api_router
#from src.api_module.routes.error import error_router

def api_handler():
    app = network.app
    asyncio_config = Config()
    asyncio_config.bind = ["localhost:80"]
    #app.include_router(api_router)
    #app.include_router(error_router)
    asyncio.run(serve(app, asyncio_config))