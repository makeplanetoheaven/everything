# coding=utf-8

"""
author: wlc
function: 新闻检索业务逻辑层
"""

# 引入外部库

# 引入内部库
from src.dao.hotNewsDao import *


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

	def get_domain_hotnews (self, domain: str, date: str, period: str, nums: str) -> dict:
		"""
		获取指定领域的热点新闻
		:param domain:
		:param date:
		:param period: 'pre-las'
		:param nums:
		:return:
		"""
		if date != '':
			return self.domain_hotnews[domain](date=date, nums=nums)
		else:
			data = None
			pre_date, las_date = map(int, period.split('-'))
			for i in range(pre_date, las_date + 1):
				if data:
					data['data'] += self.domain_hotnews[domain](date=str(i), nums=nums)['data']
				else:
					data = self.domain_hotnews[domain](date=str(i), nums=nums)

			return data
