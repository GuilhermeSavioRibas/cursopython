import urllib.request
import webbrowser
import requests
from bs4 import BeautifulSoup

# get_url = urllib.request.urlopen('https://www.google.com/')
get_url = webbrowser.open('https://www.google.com/')
# webbrowser.open_new('https://globo.com')


print('Response Status: ', str(get_url))





