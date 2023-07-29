
from datetime import datetime
import os
from unicodedata import name
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup
from xml.dom import minidom
from distutils.dir_util import copy_tree
import os.path
from os import path
import chardet

url='https://thegamesdb.net'
hdr = {'User-Agent': 'Mozilla/5.0'}
metadata = {}

def scrap(name,platform):
    print(name)
    req = url+'/search.php?name={0}'.format(name.replace(' ','+'))
    page = requests.get(req,headers=hdr)
    soup = BeautifulSoup(page.content, 'html.parser')
    coding = chardet.detect(page.content).get('encoding')
    detail = None
    results = soup.find_all('p',{'class','text-muted'})
    for r in results:
        if r.text.lower() == platform['name']:
            d = r
            continue

    url_detail = url + (d).parent.parent.parent['href']
    detail = requests.get(url_detail,headers=hdr)
    soup_detail = BeautifulSoup(detail.content, 'html.parser')
    coding = chardet.detect(detail.content).get('encoding')

    cover =  soup_detail.find_all('img',{'class','card-img-top'})[0]
    metadata['cover'] = cover['src']
    
