import requests
from lxml import html

setCode = "khm"
setNum = "136"

url = "https://scryfall.com/card/" + setCode + "/" + setNum

path = "//meta/@content"

response = requests.get(url)

byte_data = response.content

source_code = html.fromstring(byte_data)

tree = source_code.xpath(path)
print(tree)