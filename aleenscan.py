# -*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup
import re
import jieba.analyse

getvaluenots = []
getvalues = []

def getkeywordnot(url):
	req_url = requests.get(url+"/search/error.html")
	req_url.encoding="utf-8"
	bs = BeautifulSoup(req_url.text,"lxml")
	bs = re.split(r'\s+',bs.find("body").get_text())
	text = ''.join(bs)
	print text
	tfidf = jieba.analyse.extract_tags
	keywords = tfidf(text,topK=20, withWeight=True)
	for keyword in keywords:
		getvaluenots.append(keyword[1])
	return getvaluenots

def getkeyword(url):
	req_url = requests.get(url)
	req_url.encoding="utf-8"
	bs = BeautifulSoup(req_url.text,"lxml")
	bs = re.split(r'\s+',bs.find("body").get_text())
	text = ''.join(bs)
	print text
	tfidf = jieba.analyse.extract_tags
	keywords = tfidf(text,topK=20,withWeight=True)
	for keyword in keywords:
		getvalues.append(keyword[1])
	return getvalues

def getvalue(getvalues,getvaluenots):
	product = 0.0
	numa = 0.0
	numb = 0.0
	print getvalues
	for a,b in zip(getvalues,getvaluenots):
		product += a*b
		numa += a ** 2
		numb += b ** 2
	if numa == 0.0 or numb == 0.0:
		return 0
	else:
		print round(product / ((numa**0.5)*(numb**0.5))*100,2)

def main(urls):
	a = getkeywordnot(urls)
	b = getkeyword(urls)
	getvalue(a,b)

	
if __name__ == '__main__':
	main("https://www.baidu.com/")
