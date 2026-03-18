import json
from datetime import date

FILE="streak.json"


def update_streak(user):

    today = str(date.today())

    try:
        with open(FILE,"r") as f:
            data=json.load(f)
    except:
        data={}

    if user not in data:
        data[user]={"streak":1,"last":today}

    else:

        if data[user]["last"] != today:
            data[user]["streak"]+=1
            data[user]["last"]=today

    with open(FILE,"w") as f:
        json.dump(data,f)

    return data[user]["streak"]