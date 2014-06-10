#!/usr/bin/env python3

import sys

import requests
from bs4 import BeautifulSoup

ddg_url = "https://duckduckgo.com/html/"

def search(query):
    r = requests.get(ddg_url, params={'q': query})
    r.raise_for_status()

    soup = BeautifulSoup(r.text)
    for result in soup.findAll('div', class_='results_links'):
        link = result.find('a', class_='large')
        print(link.text)
        print(link['href'])
        print(result.find(class_='snippet').text)
        print()

if __name__ == "__main__":
    search(sys.argv[1])
