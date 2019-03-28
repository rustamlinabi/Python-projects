import json
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import requests
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

prez="Heydər Əliyev"

linklist=[]
n=0
months=["Yanvar","Fevral","Mart","Aprel","May","İyun","İyul","Avqust","Sentyabr","Oktyabr","Noyabr","Dekabr"]
list18={}
artcount={}
for m in months:
    list18[m.encode("utf-8")]=0
    artcount[m.encode("utf-8")]=0
def find_substring(substring, string):
    index = -1
    n=0
    while True:
        index = string.find(substring, index + 1)
        if index == -1:
            break
        else:
            n+=1
    return n

while n<400:
    url="https://az.trend.az/azerbaijan/politics/page"+str(n)+"/"
    templist=[]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    for x in soup.find_all("div", {"class:","media-heading"}):
        for t in x.find_all("a"):
            templist.append(t["href"])
    for to in templist:
        linklist.append(to)
    n+=3
articles=[]
for urls in linklist:
    article=[0,0]
    html = urllib.request.urlopen(urls, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    parlist=[]
    for x in soup.find_all("p"):
        t=x.text
        parlist.append(t)
    article[0]=" ".join(parlist)
    time=[]
    for x in soup.find_all(class_="date-created"):
        t=x.text
        l=t.encode("utf-8")
        time.append(l)
    article[1]=time[0]
    articles.append(article)

for z in articles:
    t=find_substring(prez,z[0])
    for m in months:
        if m.encode("utf-8") in z[1]:
            list18[m.encode("utf-8")]+=int(t)
            artcount[m.encode("utf-8")]+=1

print(artcount)
print(list18)
print(len(articles))
