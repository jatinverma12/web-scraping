#!/usr/bin/env python
# coding: utf-8

# In[74]:


a=dict()
a={
    'images':[],
    'News':[],
    'Important Points':'',
    'Blog':[]
  }
import requests
import json
from bs4 import BeautifulSoup as bs
url='https://iiitd.ac.in/'
data=requests.get(url)
soup=bs(data.text,'html.parser')
for i in soup.find_all('img'):
    if i.get('src')[0:5]!='https':
        a['images'].append(url+i.get('src'))
    a['images'].append(i.get('src'))
    
#print(a['images'])

a['News']
news=requests.get(url+'research/rsnews')
news1=bs(news.text,'html.parser')
#print(news1.prettify())
for i in news1.find_all('p'):
    a['News'].append(i.getText())
#print(a['News'])

link=soup.select('div#block-block-8.block-block')
for i in link:
    a['Important Points']=i.getText()
    
#print(a['Important Points'])
post=requests.get("https://blog.iiitd.ac.in/")
blog=bs(post.text,'html.parser')
for i in blog.find_all('div',class_='post-container'):
    a['Blog'].append(i.a.get('href'))
#print(a['Blog'])

with open('webscraping.json','w') as f:
    json.dump(a,f,indent=2)

