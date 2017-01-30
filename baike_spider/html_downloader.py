#coding:utf8
from urllib import request

class HtmlDownloader(object):

	def download(self,url):
		if url is None:
			return None
			
		response = request.urlopen(url)
#		print(url)
		a = response.getcode()
		if a!= 200:
			print(a)
			return  None
#		print('getcode ok!')
		
		html_cont = response.read()
#		print(html_cont)
		return  html_cont