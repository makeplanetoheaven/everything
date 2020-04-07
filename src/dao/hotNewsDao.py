# coding=utf-8

"""
author: wlc
function: 热点新闻检索数据层
"""

# 引入外部库
import json

# 引入内部库
from src.util.reptile import *


class HotNewsDao:
	def get_default_hotnews(self) -> dict:
		"""
		获取默认领域热点新闻
		:param domain:
		:return:
		"""
		# 1.参数设置
		url = 'http://top.news.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'www_www_all_suda_suda',
			'top_time': '20200407',
			'top_show_num': '100',
			'top_order': 'DESC',
			'js_var': 'default_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)

		# 3.新闻内容格式化
		data = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))

		return data
