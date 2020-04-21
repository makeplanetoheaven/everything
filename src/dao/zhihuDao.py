# coding=utf-8

"""
author: wlc
function: 知乎检索数据层
"""

# 引入外部库
import json
from bs4 import BeautifulSoup

# 引入内部库
from src.util.reptile import *


class zhihuDao:
	@staticmethod
	def get_billboard_result () -> list:
		"""
		获取默认领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'https://www.zhihu.com/billboard'

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url, is_ua=False, timeout=3)
		content = BeautifulSoup(page_content, "html.parser")
		hot_data = content.find('script', id='js-initialData').string
		hot_json = json.loads(hot_data)
		hot_list = hot_json['initialState']['topstory']['hotList']

		# 3.新闻内容格式化
		data = []
		for item in hot_list:
			hot = {
				'id': item['id'],
				'title': item['target']['titleArea']['text'],
				'abstract': item['target']['excerptArea']['text'],
				'url': item['target']['link']['url'],
				'heat': item['target']['metricsArea']['text'],
				'imgae': item['target']['imageArea']['url']
			}
			data.append(hot)

		return data