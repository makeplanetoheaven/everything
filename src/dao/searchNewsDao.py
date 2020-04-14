# coding=utf-8

"""
author: wlc
function: 基于关键字新闻检索数据层
"""

# 引入外部库
import json

# 引入内部库
from src.util.reptile import *


class SearchNewsDao:
	@staticmethod
	def get_search_news () -> list:
		"""
		获取默认领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'https://search.sina.com.cn/?'
		parm = {
			'q': '人工智能',
			'c': 'news',
			'range': 'title',
			'stime': '',
			'etime': '',
			'size': '10',
			'sort': 'time',
			'page': ''
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)
		print(page_content)

		# # 3.新闻内容格式化
		# data = []
		# for item in news_list:
		# 	hotnews = {
		# 		'domain': 'default',
		# 		'author': item['author'],
		# 		'create_date': item['create_date'],
		# 		'create_time': item['create_time'],
		# 		'id': item['id'],
		# 		'media': item['media'],
		# 		'title': item['title'],
		# 		'url': item['url'],
		# 	}
		# 	data.append(hotnews)

		return []
