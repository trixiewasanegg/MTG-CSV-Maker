import requests
import re
from lxml import html

setCode = "khm"
setNum = "136"

#regexes
powerRegex="[0-9]+\/[0-9]+"
blankRegex = "\\n[ ]*"
anyRegex = "[a-zA-Z0-9()].*[a-zA-Z0-9()]"
newLineRegex = "\n.*"

def metaQuery(code,num):
    url = "https://scryfall.com/card/" + code + "/" + num

    response = requests.get(url)

    byte_data = response.content

    source_code = html.fromstring(byte_data)

    cardNameRaw = source_code.xpath("//span[@class='card-text-card-name']//text()")
    cardName = re.sub(blankRegex,"",cardNameRaw[0])
    print("Card Name: " + str(cardName))
    cardTypeRaw = source_code.xpath("//p[@class='card-text-type-line']//text()")
    cardType = re.sub(blankRegex,"",cardTypeRaw[0])
    print("Card Type: " + str(cardType))
    cardDescRaw = source_code.xpath("//div[@class='card-text-oracle']//text()")
    cardDescMerge = ""
    for n in cardDescRaw:
        cardDescMerge = cardDescMerge +" "+ str(n)
    cardDescTmp = re.findall(anyRegex,cardDescMerge)
    cardDesc = ""
    for n in cardDescTmp:
        cardDesc = cardDesc + "\n" + str(n)
    print("Card Desc: " + str(cardDesc))
    cardPowerRaw = source_code.xpath("//div[@class='card-text-stats']//text()")
    cardPower = re.findall(powerRegex,cardPowerRaw[0])
    print("Card Power: " + str(cardPower[0]))
    cardMana = source_code.xpath("//span[@class='card-text-mana-cost']//text()")
    print("Card Mana: " + str(cardMana[0]))


metaQuery(setCode,setNum)