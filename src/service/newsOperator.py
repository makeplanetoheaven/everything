# coding=utf-8

"""
author: wlc
function: 新闻检索业务逻辑层
"""

# 引入外部库

# 引入内部库
from src.dao.hotNewsDao import *
from src.dao.searchNewsDao import *
from src.entity.retrieveResult import *


class NewsOperator:
	def __init__ (self):
		# 领域热点新闻调用接口
		self.domain_hotnews = {
			'default': HotNewsDao().get_default_hotnews,
			'video': HotNewsDao().get_video_hotnews,
			'image': HotNewsDao().get_image_hotnews,
			'china': HotNewsDao().get_china_hotnews,
			'world': HotNewsDao().get_world_hotnews,
			'society': HotNewsDao().get_society_hotnews,
			'sports': HotNewsDao().get_sports_hotnews,
			'finance': HotNewsDao().get_finance_hotnews,
			'ent': HotNewsDao().get_ent_hotnews,
			'tech': HotNewsDao().get_tech_hotnews,
			'mil': HotNewsDao().get_mil_hotnews,
		}

	def get_domain_hotnews (self, domain: str, date: str, nums: str) -> RetrieveResult:
		"""
		获取指定领域的热点新闻
		:param domain:
		:param date:
		:param nums:
		:return:
		"""
		# 数据处理
		d_list = domain.split('-')
		pre_date, las_date = map(int, date.split('-'))

		# 检索对象创建
		data = RetrieveResult(intent='news', subintent='hotnews')

		# 信息检索
		for i in range(pre_date, las_date + 1):
			for d in d_list:
				data.set_data(self.domain_hotnews[d](date=str(i), nums=nums))

		return data

	def get_search_newsrsult(self):
		"""
		获取基于关键字的新闻检索结果
		:return:
		"""
		SearchNewsDao.get_search_news()
