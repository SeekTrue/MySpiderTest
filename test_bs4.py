#coding utf8
import re
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')

print('获取所有的链接')
links = soup.find_all('a')
for link in links:
    print(link.name,link['href'],link.get_text())

print('获取lacie的链接')
link_node = soup.find_all('a',href='http://example.com/lacie')
for link in link_node:
    print(link.name,link['href'],link.get_text())



print('使用正则表达式获取elsie的链接')
link_node1 = soup.find_all('a',href=re.compile("elsie"))
for link in link_node1:
    print(link.name,link['href'],link.get_text())

print('获取p段落文字')
link_node2 = soup.find_all('p',class_=re.compile("title"))
for link in link_node2:
    print(link.name,link['class'],link.get_text())
