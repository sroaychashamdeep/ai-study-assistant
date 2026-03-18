import json

FILE="progress.json"

def load_progress():

    try:
        with open(FILE,"r") as f:
            return json.load(f)
    except:
        return {}

def save_progress(data):

    with open(FILE,"w") as f:
        json.dump(data,f)