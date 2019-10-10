# Test app of CV

The app should recognize objects on a video

## Installation

1. Install **python 3.7** and **pip**
2. Create environment
    ```bash
    $ python -m venv venv
    ```
3. Activate environment
    
    in PowerShell:
    ```bash
    $ ./venv/Scripts/Activate.ps1
    ```
   
    in cmd:
    ```bash
    $ ./venv/Scripts/activate.bat
    ```
   
    in bash:
    ```bash
    $ source ./venv/bin/activate
    ```
   
4. Install requirements
    ```bash
    $ pip install -r requirements.txt
    ```
   
## How to run

1. Put video file to `./data` folder
2. In `main.py` in string `cap = cv.VideoCapture('data/video.mkv')` change path to your file
3. Activate environment
4. run program
    ```bash
    $ python main.py
    ```