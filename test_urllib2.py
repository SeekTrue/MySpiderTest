# coding:utf8

from urllib import request
import http.cookiejar
# url  = "http://www.baidu.com"
url = "http://baike.baidu.com/view/21087.htm"
print("第一种方法")
response1 = request.urlopen(url)

print(response1.getcode())

html_doc = response1.read();
print(len(html_doc))

import re
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')

summary_node = soup.find('div',class_="lemma-summary")

print(summary_node.get_text())
# print("第二种方法")
# req = request.Request(url)
# req.add_header("user-agent","Mozilla/5.0")
# response2 = request.urlopen(req)
# print(response2.getcode())
# print(len(response2.read()))

# print("第三种方法")
# cj = http.cookiejar.CookieJar()
# opener = request.build_opener(request.HTTPCookieProcessor(cj))
# request.install_opener(opener)
# response3 = request.urlopen(url)
# print(response3.getcode())
# print(cj)
# print(response3.read())
