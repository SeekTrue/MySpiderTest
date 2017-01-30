#coding:utf8
from bs4 import BeautifulSoup
import re
import urllib.parse
class HtmlParser(object):

	def parse(self,page_url,html_cont):
		if page_url is None or html_cont is None:
			return
			
		soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
		new_urls = self._get_new_urls(page_url,soup)
		new_data = self._get_new_data(page_url,soup)
		return  new_urls, new_data
		
	def _get_new_urls(self,page_url,soup):
		new_urls = set()
		#/view/123.htm
		links = soup.find_all('a',href = re.compile(r"/view/\d+\.htm"))
		for link in links:
			new_url = link['href']			
			new_full_url = urllib.parse.urljoin(page_url,new_url)
			new_urls.add(new_full_url)
		return new_urls	
		
	def _get_new_data(self,page_url,soup):
		res_data = {}
		
		res_data['url'] = page_url
		
		title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title")
		if title_node == None:
			res_data['title'] = ''
			res_data['summary'] = ''
			return  res_data
		else:
			title_node = title_node.find("h1")
			res_data['title'] = title_node.get_text()
			
#		print(res_data['title'])
		
		summary_node = soup.find('div',class_="lemma-summary")
		if summary_node == None:
			res_data['summary'] = ''
		else:
			res_data['summary'] = summary_node.get_text()
#		print(res_data['summary'])
		
		return res_data