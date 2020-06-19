# coding=utf-8

"""
author: wlc
function: 基于关键字新闻检索数据层
"""

# 引入外部库
import re
from bs4 import BeautifulSoup

# 引入内部库
from src.util.reptile import *


class SearchNewsDao:
	@staticmethod
	def get_search_result (key_list: list, method: str, stime: str, etime: str, page: str) -> list:
		"""
		获取指定关键字的新闻
		:param key_list:
		:param method:
		:param stime:
		:param etime:
		:param page:
		:return:
		"""
		# 1.参数设置
		url = 'https://search.sina.com.cn/?'
		parm = {
			'q': '+'.join(key_list),
			'c': 'news',
			'range': method,
			'stime': stime,
			'etime': etime,
			'size': '10',
			'sort': 'time',
			'page': page
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)
		bs = BeautifulSoup(page_content, "html.parser")
		news_list = bs.body.find_all("div", {'class': 'box-result'})

		# # 3.新闻内容格式化
		data = []
		for item in news_list:
			author, date, time = re.sub('[\n,\t]', '', str(item.span.contents[0])).split(' ')
			a = item.a
			news = {
				'author': author,
				'create_date': date,
				'create_time': time,
				'title': re.sub('[<font clr="red">,</font>]', '', ''.join(map(str, a.contents))),
				'url': a.get('href'),
			}
			data.append(news)

		return data
