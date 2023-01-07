@echo off

:start
cls

IF "%1"=="install" (
    python.exe -m pip install --upgrade pip
    REM  Used to install patoolib for unpacking .rar files
    pip install patool==1.12

    REM Used to install nltk and furthermore downloads wordnet
    pip install nltk==3.8
    REM Used to install numpy
    pip install numpy==1.23.5
    REM Used to install tensorflow for the gpu, but requires cuda and cudnn which are installed later
    pip install tensorflow==2.10.1
    pip install tensorflow-gpu==2.10.1
    REM Used to install keras used for the neural network
    pip install keras==2.10.0
    
    REM Used to install hypercorn for the webserver, which will be built ontop of fastapi
    pip install hypercorn
    REM Used to install fastapi for the webserver
    pip install fastapi
    REM Used to install pydantic, used for mainly importing settings
    pip install pydantic
    REM Used to install itsdangerous, used for some improved security
    pip install itsdangerous
    
    REM Used to prepare and install wordnet from nltk, then deletes the file it created
    echo import nltk> %~dp0cmd_pyinstall.py
    echo nltk.download('wordnet'^)>> %~dp0cmd_pyinstall.py
    python %~dp0cmd_pyinstall.py
    if exist %~dp0cmd_pyinstall.py del /F /Q %~dp0cmd_pyinstall.py

    cls
    echo "Successfully installed packages."
    echo "Please restart all your teminals to register the environment variables."
)

IF "%1"=="uninstall" (
    pip uninstall -y patool

    pip uninstall -y nltk
    pip uninstall -y numpy
    REM pip uninstall -y tensorflow
    pip uninstall -y tensorflow-gpu
    pip uninstall -y keras

    pip uninstall -y hypercorn
    pip uninstall -y fastapi
    pip uninstall -y pydantic
    pip uninstall -y itsdangerous

    cls
    echo "Successfully uninstalled packages."
)

IF "%1"=="build" (    
    pyinstaller --noconfirm --onedir --console --add-data %~dp0trained_data;trained_data\ --add-data %~dp0training_data;training_data\ %~dp0main.py

    cls
    echo Build was successful!
)

IF "%1"=="clean" (
    if exist %~dp0*.spec del /S /F /Q %~dp0*.spec
    if exist %~dp0trained_data\* del /S /F /Q %~dp0trained_data\*
    if exist %~dp0build rmdir /S /Q %~dp0build
    if exist %~dp0dist rmdir /S /Q %~dp0dist

    cls
    echo Cleaned up all files.
)

exit