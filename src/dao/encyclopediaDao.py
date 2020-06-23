# coding=utf-8

"""
author: wlc
function: 百科检索数据层
"""

# 引入外部库
import json
import re
import requests

# 引入内部库
from src.util.reptile import *


class EncyclopediaDao:
	@staticmethod
	def get_key_content (key: str) -> list:
		"""
		获取指定关键字的百科内容检索内容
		:param key:
		:return:
		"""
		# 1.参数设置
		url = 'https://zh.wikipedia.org/w/api.php?'
		parm = {
			'action': 'query',
			'list': 'search',
			'srsearch': key,
			'format': 'json',
			'formatversion': '2'
		}

		# 2.百科内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)
		content_list = json.loads(page_content)['query']['search']

		# 3.百科内容格式化
		data = []
		prefix = 'https://zh.wikipedia.org/wiki/'
		for index, item in enumerate(content_list):
			date, time = item['timestamp'].rstrip('Z').split('T')
			entry = {
				'id': item['pageid'],
				'index': index,
				'create_date': date,
				'create_time': time,
				'title': item['title'],
				'abstract': re.sub('[<span class=\"searchmatch\">,</span>]', '', item['snippet']),
				'url': prefix + item['title'],
			}
			data.append(entry)

		return data

	@staticmethod
	def get_key_title(key: str) -> list:
		"""
		获取指定关键字的百科内容检索标题
		:param key:
		:return:
		"""
		# 1.参数设置
		url = 'https://zh.wikipedia.org/w/api.php?'
		parm = {
			'action': 'opensearch',
			'search': key,
			'format': 'json',
			'formatversion': '2'
		}

		# 2.百科内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)
		content_list = json.loads(page_content)[1]

		# 3.百科内容格式化
		data = []
		prefix = 'https://zh.wikipedia.org/wiki/'
		for index, item in enumerate(content_list):
			entry = {
				'index': index,
				'title': item,
				'url': prefix + item,
			}
			data.append(entry)

		return data

	@staticmethod
	def get_faq_content(query: str, page: str) -> list:
		"""
		获取指定query的faq检索内容
		:param query:
		:param page:
		:return:
		"""
		# 1.参数设置
		url = 'https://zhidao.baidu.com/search?'
		parm = {
			'lm': '0',
			'rn': '5',
			'pn': page,
			'fr': 'search',
			'is': 'utf8',
			'word': query
		}

		# 2.百科内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)
		content_list = json.loads(page_content)['query']['search']

		# 3.百科内容格式化
		data = []
		prefix = 'https://zh.wikipedia.org/wiki/'
		for index, item in enumerate(content_list):
			date, time = item['timestamp'].rstrip('Z').split('T')
			entry = {
				'id': item['pageid'],
				'index': index,
				'create_date': date,
				'create_time': time,
				'title': item['title'],
				'abstract': re.sub('[<span class=\"searchmatch\">,</span>]', '', item['snippet']),
				'url': prefix + item['title'],
			}
			data.append(entry)

		return data
