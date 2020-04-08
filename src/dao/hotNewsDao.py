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
	@staticmethod
	def get_default_hotnews() -> dict:
		"""
		获取默认领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.news.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'www_www_all_suda_suda',
			'top_time': '20200408',
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

	@staticmethod
	def get_video_hotnews() -> dict:
		"""
		获取视频领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.news.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'video_news_all_by_vv',
			'top_time': '20200407',
			'top_show_num': '50',
			'top_order': 'DESC',
			'js_var': 'video_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)

		# 3.新闻内容格式化
		data = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))

		return data

	@staticmethod
	def get_image_hotnews () -> dict:
		"""
		获取图片领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.news.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'total_slide_suda',
			'top_time': '20200408',
			'top_show_num': '50',
			'top_order': 'DESC',
			'js_var': 'image_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)

		# 3.新闻内容格式化
		data = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))

		return data

	@staticmethod
	def get_china_hotnews () -> dict:
		"""
		获取国内领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.news.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat':  'news_china_suda',
			'top_time': '20200408',
			'top_show_num': '50',
			'top_order': 'DESC',
			'js_var': 'china_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)

		# 3.新闻内容格式化
		data = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))

		return data

	@staticmethod
	def get_world_hotnews () -> dict:
		"""
		获取国际领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.news.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'news_world_suda',
			'top_time': '20200408',
			'top_show_num': '50',
			'top_order': 'DESC',
			'js_var': 'world_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)

		# 3.新闻内容格式化
		data = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))

		return data

	@staticmethod
	def get_society_hotnews () -> dict:
		"""
		获取社会领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.news.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'news_society_suda',
			'top_time': '20200408',
			'top_show_num': '50',
			'top_order': 'DESC',
			'js_var': 'society_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)

		# 3.新闻内容格式化
		data = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))

		return data

	@staticmethod
	def get_sports_hotnews () -> dict:
		"""
		获取体育领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.sports.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'tyxwpl',
			'top_time': '20200407',
			'top_show_num': '50',
			'top_order': 'DESC',
			'js_var': 'sports_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)

		# 3.新闻内容格式化
		data = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))

		return data

	@staticmethod
	def get_finance_hotnews () -> dict:
		"""
		获取财经领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.finance.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'finance_0_suda',
			'top_time': '20200407',
			'top_show_num': '50',
			'top_order': 'DESC',
			'js_var': 'finance_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)

		# 3.新闻内容格式化
		data = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))

		return data

	@staticmethod
	def get_ent_hotnews () -> dict:
		"""
		获取娱乐领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.ent.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'ent_suda',
			'top_time': '20200407',
			'top_show_num': '50',
			'top_order': 'DESC',
			'js_var': 'ent_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)

		# 3.新闻内容格式化
		data = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))

		return data

	@staticmethod
	def get_tech_hotnews () -> dict:
		"""
		获取科技领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.tech.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'tech_news_suda',
			'top_time': '20200407',
			'top_show_num': '50',
			'top_order': 'DESC',
			'js_var': 'tech_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)

		# 3.新闻内容格式化
		data = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))

		return data

	@staticmethod
	def get_mil_hotnews () -> dict:
		"""
		获取军事领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.news.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'news_mil_suda',
			'top_time': '20200408',
			'top_show_num': '50',
			'top_order': 'DESC',
			'js_var': 'mil_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)

		# 3.新闻内容格式化
		data = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))

		return data
