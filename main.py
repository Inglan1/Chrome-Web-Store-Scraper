try:
  from bs4 import BeautifulSoup
  import requests
except:
  from os import system
  system('pip install bs4')


def extDetails(id):
  soup = BeautifulSoup(
    requests.get('https://chrome.google.com/webstore/detail/' + id).text,
    'html.parser')
  out = {}
  out['name'] = (soup.find("meta", property="og:title")['content'])
  out['offered'] = soup.find("a", {"class": "e-f-y"}).string
  out['desc'] = soup.find("div", {
    "class": "C-b-p-j-Pb",
    "itemprop": "description"
  }).string + ' ' + soup.find("pre", {
    'class': 'C-b-p-j-Oa'
  }).string
  out['shortdesc'] = soup.find("div", {
    "class": "C-b-p-j-Pb",
    "itemprop": "description"
  }).string
  return (out)
