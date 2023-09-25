import datetime
import requests
from requests import Response
from config import Config


def send_inscription(inscription):
    response = requests.post(Config.URL_API,inscription)
    if response.status_code == 201 or response.status_code == 200:
        return "ok"
    else:
        return "failled"    