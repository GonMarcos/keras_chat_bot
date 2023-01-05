'''
Description: This file contains the header of the program. It is used to import all the necessary modules and to define the functions that can be executed.
It also limits the scope of the functions that can be executed to the ones that are defined in the func_list dictionary.
'''

from installation.wizzard import install_wizzard, uninstall_wizzard, clean_wizzard, help_waizard#, version_wizard
from src.config import config


# Hold a reference to all the functions that can be executed within a dictionary.
func_list = {
    "help":         help_waizard,
    "install":      install_wizzard,
    "uninstall":    uninstall_wizzard,
    "clean":        clean_wizzard
}

try:
    from src.training.training_data.training_model import train
    # Only imports the modules if they are installed.
    #from src.ai_module.training_module import training_wizard
    #from src.ai_module.chat_module import local_chat
    #from src.api_module.api_module import api_handler
    
    # Append new references to all the functions that can be executed within a dictionary.
    func_list["train"] = train
    # func_list["version"] = version_wizard
    #func_list["chat"] = local_chat
    #func_list["api"] = api_handler

except ImportError as e:
    print("Import error: ", e)
    pass