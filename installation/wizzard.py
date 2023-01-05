import os, subprocess, shutil
from distutils.dir_util import copy_tree

installation_path = os.path.join(os.getcwd(), "installation")
full_path = os.path.join(installation_path, "commands.bat")
temp_path = os.path.join(installation_path, "temp")


def install_wizzard():
    if not os.path.exists(temp_path):
        os.mkdir(temp_path)

    subprocess.call([full_path, "install"])
    import patoolib
    patoolib.extract_archive(os.path.join(installation_path, "archieves", "python_3_10.rar"), outdir=temp_path)
    subprocess.call([os.path.join(temp_path, 'cuda_installation.exe')], shell=True)
    copy_tree(os.path.join(temp_path, 'cuDNN'), 'C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.2/')
    shutil.rmtree(temp_path)


def uninstall_wizzard():
    subprocess.call([full_path, "uninstall"])


def clean_wizzard():
    subprocess.call([full_path, "clean"])


def help_waizard():
    help_contents = "Usage(s):\n"
    help_contents += "===================================================================================\n"
    help_contents += "'python .\main.py install'\n"
    help_contents += "This will install all dependancies reuired for the bot.\n"
    help_contents += "\n"
    help_contents += "'python .\main.py uninstall'\n"
    help_contents += "This will uninstall all dependancies that were reuired for the bot.\n"
    help_contents += "\n"
    help_contents += "'python .\main.py clean'\n"
    help_contents += "This will delete all training data.\n"
    help_contents += "\n"
    help_contents += "'python .\main.py train'\n"
    help_contents += "This will train the bot based on the training_data json file.\n"
    help_contents += "\n"
    help_contents += "'python .\main.py build'\n"
    help_contents += "This will build the files into an application with pyinstaller using onedir.\n"
    help_contents += "\n"
    help_contents += "'python .\main.py chat'\n"
    help_contents += "This will allow you to chat with the bot.\n"
    help_contents += "\n"
    help_contents += "'python .\main.py version'\n"
    help_contents += "This will print out the versions of karas, cuda, cuDNN and other important versions.\n"
    help_contents += "===================================================================================\n"
    print(help_contents)
    return


# def version_wizard():
#     #nvcc --version
#     import tensorflow as tf
#     print(tf.__version__)
#     print(tf.config.list_physical_devices())