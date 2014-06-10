#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

ddg_url = "https://duckduckgo.com/html/"

keyword = 'cars'

def main():
    r = requests.get(ddg_url, params={'q': keyword})
    r.raise_for_status()

    soup = BeautifulSoup(r.text)
    for result in soup.findAll('div', class_='results_links'):
        print(result.find(class_='large').text)
        print(result.find(class_='snippet').text)
        print()

if __name__ == "__main__":
    main()
