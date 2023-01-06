import requests

from constants import API_KEY
from settings import FROM_LANGUAGE, REGION, TO_LANGUAGE

with open("to_translate.txt", "r")as translate:
    text = translate.read()

data = [{"Text": text}]
headers = {"Ocp-Apim-Subscription-Key": API_KEY, "Ocp-Apim-Subscription-Region": REGION}
params = {"api-version": "3.0", "from": FROM_LANGUAGE, "to": TO_LANGUAGE}

response = requests.post("https://api.cognitive.microsofttranslator.com/translate", headers=headers, params=params, json=data)

translated_text = response.json()[0]["translations"][0]["text"]

with open("translation.txt", "w") as translation:
    translation.write(translated_text)
