#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

ROOT_URL = 'https://music.douban.com/top250'
result = []

def getNames(url):
    soup = BeautifulSoup(requests.get(url).text,"html.parser")
    for i in soup.findAll('a',attrs={'class':'nbg'}):
        result.append(i.get('title').encode('utf-8'))
    next = getNextUrl(soup)
    print chr(16),
    if next!=None:
        getNames(next.get('href').encode('utf-8'))

def getNextUrl(soup):
    return soup.find('link',attrs={'rel':'next'})

if __name__ == '__main__':
    print 'start'
    getNames(ROOT_URL)
    f = open('result.txt','w')
    size = len(result)
    for index,i in enumerate(result):
        f.write(str(index+1)+'.'+i)
        if index < size:
            f.write('\n')
    f.close()
    print '\nfinish!'
