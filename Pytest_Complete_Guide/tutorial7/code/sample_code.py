import random
import time
import requests

def random_sum():
    a=random.randint(1,6)
    b=random.randint(1,6)
    return a+b

def silly():
    params={
        "timestamp":time.time(),
        "number":random.randint(1,6)
    }

    response=requests.get("https://httpsbin.org/get",params)
    if response.status_code==200:
        return response.json()['args']