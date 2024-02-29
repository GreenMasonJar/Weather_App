import os
from dotenv import load_dotenv
import requests

#load api key from env file (will not be committed to git repo)
load_dotenv()
apiKey = os.getenv("api_key")

#inputting correct url to fetch api
base_url = "https://api.openweathermap.org/data/2.5/weather?"
city = "Ogden"
url = base_url + "appid=" + apiKey + "&q=" + city

#fetching the api as json
response = requests.get(url).json()

#printing response to verify
print(response)









