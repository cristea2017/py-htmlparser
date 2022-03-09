# Beautifulsoup lxml
import json
from unicodedata import name
from bs4 import BeautifulSoup as bs


with open("index.html") as file:
    src = file.read()
    # print('>>>File', src)

soup = bs(src, "xml")


h1 = soup.find("h1")
print('title >', h1)

div = soup.find_all('div', class_='sabai-entity sabai-entity-type-content sabai-entity-bundle-name-companii-listing sabai-entity-bundle-type-directory-listing sabai-entity-mode-summary sabai-clearfix')
data = []
for item in div:
    # print('div >', item)
    title = item.find('div', class_='sabai-directory-title')
    address = item.find(
        'div', class_='sabai-directory-location')
    contact = item.find(
        'div', class_='sabai-directory-contact')
    desc = item.find(
        'div', class_='sabai-directory-body')

    print('Title >>>', title.text.strip())
    print('Address >>>', address.text.strip())
    print('Contact >>>', contact.text.strip())
    print('Description >>>', desc.text.strip())
    data.append({'name': title.text.strip(),
                 'address': address.text.strip(),
                 'contact': contact.text.strip(),
                 'description': desc.text.strip()})


with open('data.json', 'w') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
