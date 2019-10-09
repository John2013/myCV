# Test app of CV

The app should recognize objects on a video

## Installation

1. Install **Anaconda** or **Miniconda** for **Python3.7**
    https://www.anaconda.com/distribution/
2. Create environment
    ```bash
    $ conda create --name myEnv 
    ```
3. Activate environment
    ```bash
    $ conda activate myEnv
    ```
4. Install requirements
    ```bash
    $ conda install --file .\requirements.txt
    ```
   
## How to run

1. Put video file to `./data` folder
2. In `main.py` in string `cap = cv.VideoCapture('data/video.mkv')` change path to your file
3. Activate environment
4. run program
    ```bash
    $ python main.py
    ```