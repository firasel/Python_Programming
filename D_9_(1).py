# Wallpaper setup
import json

import requests

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

response = requests.get(api_url)
content = response.content.decode('UTF-8')
# Convert string content to dictionary
dict_content = json.loads(content)
image_url = dict_content['url']
# Download the image
res = requests.get(image_url)
# Save the image
with open('apod.png', 'wb') as image:
    image.write(res.content)
