#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author:404
#By T00ls.Net
from aleenscan import aleen
import requests
import argparse


def getdict(dict_l):
	f = open(dict_l,"r")
	dictur=[]
	dicturls =f.readlines()
	for dicturl in dicturls:
		dictur.append(dicturl.strip("\n"))
	return dictur
def scan(url,dict_l):
	error_url = aleen.gettext(url)
	dict_urls = getdict(dict_l)
	info_code, info_content = aleen.getinfo(url)
	if info_code == 404:
		print "scan v1"
		for dict_url in dict_urls:
			scan1_code,scan2_content= aleen.scanv1(url,dict_url)
			if scan1_code == 200:
				print url+dict_url+" ======"+('\033[1;31;40m%s\033[0m' % str(scan1_code))
			else:
				print url+dict_url+" ======"+str(scan1_code)

	elif "不存在" in info_content or "404/search_children" in info_content:
		print "scan v2"
		for dict_url in dict_urls:
			scan2_code,scan2_content= aleen.scanv1(url,dict_url)
			if "不存在" in scan2_content or "404/search_children" in scan2_content:
				print url+dict_url+" ======404"
			else:
				print url+dict_url+('\033[1;31;40m%s\033[0m' % 200)
	else:
		print "scan v3"
		for dict_url in dict_urls:
			scandict = aleen.getnot(url,dict_url)
			word1,word2 = aleen.getwords(error_url,scandict)
			nubmer = aleen.getjg(word1,word2)
			if nubmer < 80:
				print url+dict_url+('\033[1;31;40m%s\033[0m' % 'YES')
			else:
				print url+dict_url+"===="+"NO"

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--url','-u',help="your url")
	parser.add_argument('--dict','-d',help='your dict')
	args = parser.parse_args()
	scan(args.url,args.dict)

if __name__ == '__main__':
	main()