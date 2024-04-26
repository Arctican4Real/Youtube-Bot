import requests
import json

inp = input("Which ayah of the Quran? : ")

example = f"http://api.alquran.cloud/v1/ayah/{inp}/en.asad"

req = requests.get(example).json()

print(req["data"]["surah"]["englishName"], ",", req["data"]["numberInSurah"])
print(req["data"]["text"].encode('utf-8'))

reciter = "https://api.quran.com/api/v4/resources/chapter_reciter"
req = requests.get(reciter).json()
print(req)
