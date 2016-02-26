#! /usr/bin/env python

import pinyin
import urllib
import urllib2
import re

def match(html):
	pattern = re.compile(r'About (\d{1,3})(,\d{3})*')
	res = pattern.search(html)
	# res = pattern.match('44,784,121,211')
	if res:
		return res.group().split()[-1]
	else:
		print 'RE NOT MATCHED!'
		exit()



def query(mentor):
	url = 'https://www.google.com.hk/search?hl=en&%s'

	py_n = pinyin.get(mentor, delimiter=' ', format='strip').split()
	py_n = ''.join(py_n[1:] + [' ', py_n[0]])
	get_arg = {'q': '%s tsinghua' % py_n}

	key_words = urllib.urlencode(get_arg)
	url = url % key_words

	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = {'User-Agent': user_agent}

	request = urllib2.Request(url, None, headers)
	response = urllib2.urlopen(request)
	html = response.read()

	return match(html)


def main():
	with open(r'.\roster') as f:
		mentors = f.read().decode('utf-8').split()

	rank = {}
	for m in mentors:
		rank[m] = int(query(m).replace(',', ''))

	for m, r in sorted(rank.items(), None, lambda t: t[1], True):
		print m, r

	
if __name__ == '__main__':
	main()