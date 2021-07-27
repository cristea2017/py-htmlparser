import requests
from bs4 import BeautifulSoup
import time
import webbrowser
import time

baseUrl = 'https://mcpedl.com/two-temples-fortunately-sea-amazing-islands/'
vgm_url = baseUrl
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')
print('soup', soup)
time.sleep(3)
html_text = requests.get(vgm_url).text

print('htm', html_text)
webbrowser.open_new_tab(baseUrl)
