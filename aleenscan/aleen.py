#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author:404
#By T00ls.Net
import requests
from bs4 import BeautifulSoup
import re
import jieba
import jieba.analyse

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

def getinfo(url):
    info_url = requests.get(url+"/aleenzzxxxxx.html",headers=headers)
    return info_url.status_code,info_url.content

def gettext(url):
	#一个不存在的页面

	req_url = requests.get(url+"/search/aleenzzz.html",headers=headers)
	req_url.encoding="utf-8"
	bs = BeautifulSoup(req_url.text,"lxml")
	bs = re.split(r'\s+',bs.find("body").get_text())
	text = ''.join(bs)
	return text

def getnot(url,dicturl):
	#这里你的字典
	req_url = requests.get(url+dicturl,headers=headers) 
	req_url.encoding="utf-8"
	bs = BeautifulSoup(req_url.text,"lxml")
	bs = re.split(r'\s+',bs.find("body").get_text())
	dict_text = ''.join(bs)
	return dict_text
 
def getwords(url1, url2):
    word1 = []
    word2 = []
    analyse_tag1 = jieba.analyse.extract_tags(url1, withWeight=True)
    analyse_tag1 = jieba.analyse.extract_tags(url2, withWeight=True)
    tag_dict1 = {i[0]: i[1] for i in analyse_tag1}
    tag_dict2 = {i[0]: i[1] for i in analyse_tag1}
    merged_tag = set(tag_dict1.keys()) | set(tag_dict2.keys())
    for i in merged_tag:
        if i in tag_dict1:
            word1.append(tag_dict1[i])
        else:
            word1.append(0)
        if i in tag_dict2:
            word2.append(tag_dict2[i])
        else:
            word2.append(0)
    return word1, word2
 
 
def getjg(vector1, vector2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return 0
    else:
        return round(dot_product / ((normA**0.5)*(normB**0.5)) * 100,2)

def scanv1(url,dicturl):
    req_url = requests.get(url+dicturl,headers=headers)
    return req_url.status_code,req_url.content

