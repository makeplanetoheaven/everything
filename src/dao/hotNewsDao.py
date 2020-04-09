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
	def get_default_hotnews (date: str, nums: str) -> list:
		"""
		获取默认领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.news.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'www_www_all_suda_suda',
			'top_time': date,
			'top_show_num': nums,
			'top_order': 'DESC',
			'js_var': 'default_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)
		news_list = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))["data"]

		# 3.新闻内容格式化
		data = []
		for item in news_list:
			hotnews = {
				'domain': 'default',
				'author': item['author'],
				'create_date': item['create_date'],
				'create_time': item['create_time'],
				'id': item['id'],
				'media': item['media'],
				'title': item['title'],
				'url': item['url'],
			}
			data.append(hotnews)

		return data

	@staticmethod
	def get_video_hotnews (date: str, nums: str) -> list:
		"""
		获取视频领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.news.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'video_news_all_by_vv',
			'top_time': date,
			'top_show_num': nums,
			'top_order': 'DESC',
			'js_var': 'video_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)
		news_list = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))["data"]

		# 3.新闻内容格式化
		data = []
		for item in news_list:
			hotnews = {
				'domain': 'video',
				'author': item['author'],
				'create_date': item['create_date'],
				'create_time': item['create_time'],
				'id': item['id'],
				'media': item['media'],
				'title': item['title'],
				'url': item['url'],
			}
			data.append(hotnews)

		return data

	@staticmethod
	def get_image_hotnews (date: str, nums: str) -> list:
		"""
		获取图片领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.news.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'total_slide_suda',
			'top_time': date,
			'top_show_num': nums,
			'top_order': 'DESC',
			'js_var': 'image_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)
		news_list = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))["data"]

		# 3.新闻内容格式化
		data = []
		for item in news_list:
			hotnews = {
				'domain': 'image',
				'author': item['author'],
				'create_date': item['create_date'],
				'create_time': item['create_time'],
				'id': item['id'],
				'media': item['media'],
				'title': item['title'],
				'url': item['url'],
			}
			data.append(hotnews)

		return data

	@staticmethod
	def get_china_hotnews (date: str, nums: str) -> list:
		"""
		获取国内领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.news.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat':  'news_china_suda',
			'top_time': date,
			'top_show_num': nums,
			'top_order': 'DESC',
			'js_var': 'china_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)
		news_list = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))["data"]

		# 3.新闻内容格式化
		data = []
		for item in news_list:
			hotnews = {
				'domain': 'china',
				'author': item['author'],
				'create_date': item['create_date'],
				'create_time': item['create_time'],
				'id': item['id'],
				'media': item['media'],
				'title': item['title'],
				'url': item['url'],
			}
			data.append(hotnews)

		return data

	@staticmethod
	def get_world_hotnews (date: str, nums: str) -> list:
		"""
		获取国际领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.news.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'news_world_suda',
			'top_time': date,
			'top_show_num': nums,
			'top_order': 'DESC',
			'js_var': 'world_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)
		news_list = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))["data"]

		# 3.新闻内容格式化
		data = []
		for item in news_list:
			hotnews = {
				'domain': 'world',
				'author': item['author'],
				'create_date': item['create_date'],
				'create_time': item['create_time'],
				'id': item['id'],
				'media': item['media'],
				'title': item['title'],
				'url': item['url'],
			}
			data.append(hotnews)

		return data

	@staticmethod
	def get_society_hotnews (date: str, nums: str) -> list:
		"""
		获取社会领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.news.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'news_society_suda',
			'top_time': date,
			'top_show_num': nums,
			'top_order': 'DESC',
			'js_var': 'society_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)
		news_list = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))["data"]

		# 3.新闻内容格式化
		data = []
		for item in news_list:
			hotnews = {
				'domain': 'society',
				'author': item['author'],
				'create_date': item['create_date'],
				'create_time': item['create_time'],
				'id': item['id'],
				'media': item['media'],
				'title': item['title'],
				'url': item['url'],
			}
			data.append(hotnews)

		return data

	@staticmethod
	def get_sports_hotnews (date: str, nums: str) -> list:
		"""
		获取体育领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.sports.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'tyxwpl',
			'top_time': date,
			'top_show_num': nums,
			'top_order': 'DESC',
			'js_var': 'sports_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)
		news_list = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))["data"]

		# 3.新闻内容格式化
		data = []
		for item in news_list:
			hotnews = {
				'domain': 'sports',
				'author': item['author'],
				'create_date': item['create_date'],
				'create_time': item['create_time'],
				'id': item['id'],
				'media': item['media'],
				'title': item['title'],
				'url': item['url'],
			}
			data.append(hotnews)

		return data

	@staticmethod
	def get_finance_hotnews (date: str, nums: str) -> list:
		"""
		获取财经领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.finance.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'finance_0_suda',
			'top_time': date,
			'top_show_num': nums,
			'top_order': 'DESC',
			'js_var': 'finance_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)
		news_list = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))["data"]

		# 3.新闻内容格式化
		data = []
		for item in news_list:
			hotnews = {
				'domain': 'finance',
				'author': item['author'],
				'create_date': item['create_date'],
				'create_time': item['create_time'],
				'id': item['id'],
				'media': item['media'],
				'title': item['title'],
				'url': item['url'],
			}
			data.append(hotnews)

		return data

	@staticmethod
	def get_ent_hotnews (date: str, nums: str) -> list:
		"""
		获取娱乐领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.ent.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'ent_suda',
			'top_time': date,
			'top_show_num': nums,
			'top_order': 'DESC',
			'js_var': 'ent_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)
		news_list = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))["data"]

		# 3.新闻内容格式化
		data = []
		for item in news_list:
			hotnews = {
				'domain': 'ent',
				'author': item['author'],
				'create_date': item['create_date'],
				'create_time': item['create_time'],
				'id': item['id'],
				'media': item['media'],
				'title': item['title'],
				'url': item['url'],
			}
			data.append(hotnews)

		return data

	@staticmethod
	def get_tech_hotnews (date: str, nums: str) -> list:
		"""
		获取科技领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.tech.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'tech_news_suda',
			'top_time': date,
			'top_show_num': nums,
			'top_order': 'DESC',
			'js_var': 'tech_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)
		news_list = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))["data"]

		# 3.新闻内容格式化
		data = []
		for item in news_list:
			hotnews = {
				'domain': 'tech',
				'author': item['author'],
				'create_date': item['create_date'],
				'create_time': item['create_time'],
				'id': item['id'],
				'media': item['media'],
				'title': item['title'],
				'url': item['url'],
			}
			data.append(hotnews)

		return data

	@staticmethod
	def get_mil_hotnews (date: str, nums: str) -> list:
		"""
		获取军事领域热点新闻
		:return:
		"""
		# 1.参数设置
		url = 'http://top.news.sina.com.cn/ws/GetTopDataList.php?'
		parm = {
			'top_type': 'day',
			'top_cat': 'news_mil_suda',
			'top_time': date,
			'top_show_num': nums,
			'top_order': 'DESC',
			'js_var': 'mil_hotnews'
		}

		# 2.新闻内容获取
		reptile = Reptile()
		page_content = reptile.get_page_content(url + '&'.join([key + '=' + parm[key] for key in parm]), timeout=3)
		news_list = json.loads(page_content.replace('var ' + parm['js_var'] + ' = ', '').rstrip(';\n'))["data"]

		# 3.新闻内容格式化
		data = []
		for item in news_list:
			hotnews = {
				'domain': 'mil',
				'author': item['author'],
				'create_date': item['create_date'],
				'create_time': item['create_time'],
				'id': item['id'],
				'media': item['media'],
				'title': item['title'],
				'url': item['url'],
			}
			data.append(hotnews)

		return data
