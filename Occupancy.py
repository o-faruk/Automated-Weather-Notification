import requests
from bs4 import *
url = "https://app.safespace.io/api/display/live-occupancy/86fb9e11?view=percent"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find("span", {"class":"text-xl"})
print(price)