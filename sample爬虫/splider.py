from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://image.baidu.com/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E7%99%BE%E5%BA%A6%E5%9B%BE%E7%89%87%E7%BE%8E%E5%A5%B3&hs=0&oriquery=%25E7%2599%25BE%25E5%25BA%25A6%25E5%259B%25BE%25E7%2589%2587&ofr=%25E7%2599%25BE%25E5%25BA%25A6%25E5%259B%25BE%25E7%2589%2587')
obj = BeautifulSoup(html,'html.parser')
urls = re.findall(r'"objURL":"(.*?)"',str(obj))
for url in urls:
	print (url)