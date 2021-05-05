# FYP Backend

This repository is the source code for the  backend system of SnakeClassifier FYP project. 

## Set up

### Prerequisites
*   Python 3.7+ (Tested with Python 3.7)
*   MySQL (Optional)

Make sure you have the `Python 3` and installed. You can verify your version by running:

```
python3 --version
```

#### Notes
*   You may want to use `venv` for managing the python environments. The following are the tutorial on how to setup venv on Unix machine. For windows or more information, see this [link](https://docs.python.org/3/tutorial/venv.html)
    1. Making the the virtual environment:
       run this on terminal `python3 -m venv venv`
    2. Activate the Virtual environment `source venv/bin/activate`

### Running the server for the first time
1.  Download and open the project directory:
    ```bash
    cd FYP-Back-End
    ```

2.  Install the required library by running the following code in the terminal:
    ```bash
    pip install -r requirements.txt
    ```

3.  Make migrations:
    ```bash
    python manage.py makemigrations
    ```

4.  Migrate to the database server
    ```bash
    python manage.py migrate
    ```
    
5.  Put the model to be executed under `classifier` directory
    ```bash
    mv ../final_EfficientNetB0.h5 classifier/final_EfficientNetB0.h5
    ```
    
5.  Run the server
    ```bash
    python manage.py runserver
    ```

### Re-running the server
If the database and model have been set up, then the system can be started directly using:
```bash
python manage.py runserver
```
