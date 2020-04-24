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


class WeiboDao:
	@staticmethod
	def get_realtimehot_result () -> list:
		"""
		获取微博热搜搜索结果
		:return:
		"""
		# 1.参数设置
		url = 'https://s.weibo.com/top/summary?cate=realtimehot'

		# 2.内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url, is_ua=True, timeout=3)
		content = BeautifulSoup(page_content, "html.parser")
		hot_data = content.find('div', id='pl_top_realtimehot')
		tr_list = hot_data.find('tbody').findAll('tr')

		# 3.内容格式化
		data = []
		prefix = 'https://s.weibo.com'
		for index, tr in enumerate(tr_list):
			td_list = tr.findAll('td')
			hot = {
				'index': index,
				'title': td_list[1].a.text,
				'url': prefix + td_list[1].a.get('href'),
				'heat': 'None' if td_list[1].span is None else td_list[1].span.text,
				'emotion': 'None' if td_list[1].img is None else td_list[1].img.get('title'),
				'type': 'None' if td_list[2].i is None else td_list[2].i.text,
			}
			data.append(hot)

		return data