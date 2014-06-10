#!/usr/bin/env python3

# ddg-scrape - DuckDuckGo search engine webscrapper
# Copyright (C) 2014  Aleksander Nitecki
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
