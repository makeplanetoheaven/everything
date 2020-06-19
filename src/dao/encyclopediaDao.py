# coding=utf-8

"""
author: wlc
function: 百科检索数据层
"""

# 引入外部库
import re
import json

# 引入内部库
from src.util.reptile import *


class EncyclopediaDao:
	@staticmethod
	def get_content_result (key: str) -> list:
		"""
		获取指定关键字的百科内容检索结果
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

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)
		content_list = json.loads(page_content)['query']['search']

		# # 3.新闻内容格式化
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
