# from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)
doc = BeautifulSoup(html.text, 'html.parser')
print(doc.select('.heading-primary')[0].contents)



# <h1 class="heading-primary color-black color-mobile-white mb-20 animate animate-1s animated fadeInUp" data-animation="fadeInUp" data-animation-delay="0s" style="animation-delay: 0s; opacity: 1;">
# 									Bootcamps Built For The New Tech Industry								</h1>
