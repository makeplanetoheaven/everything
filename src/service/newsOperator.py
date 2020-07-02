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
		# 该业务逻辑功能
		self.intent = '新闻检索'

		# 该业务逻辑子功能
		self.subintent = {
			0: '热点新闻检索',
			1: '关键字检索'
		}

		# 领域热点新闻调用接口
		self.domain_hotnews = {
			'默认': HotNewsDao.get_default_hotnews,
			'视频': HotNewsDao.get_video_hotnews,
			'图片': HotNewsDao.get_image_hotnews,
			'国内': HotNewsDao.get_china_hotnews,
			'国际': HotNewsDao.get_world_hotnews,
			'社会': HotNewsDao.get_society_hotnews,
			'体育': HotNewsDao.get_sports_hotnews,
			'财经': HotNewsDao.get_finance_hotnews,
			'娱乐': HotNewsDao.get_ent_hotnews,
			'科技': HotNewsDao.get_tech_hotnews,
			'军事': HotNewsDao.get_mil_hotnews,
		}

		# 关键字新闻检索参数
		self.search_method = {
			'标题': 'title',
			'内容': 'all'
		}

	def get_domain_hotnews (self, domain: list, date: list, nums: int) -> RetrieveResult:
		"""
		获取指定领域的热点新闻
		:param domain:
		:param date:
		:param nums:
		:return:
		"""
		# 数据处理
		pre_date, las_date = date
		pre_date = int(pre_date.replace('-', ''))
		las_date = int(las_date.replace('-', ''))

		# 检索对象创建
		data = RetrieveResult(intent=self.intent, subintent=self.subintent[0])

		# 信息检索
		data_list = []
		for i in range(pre_date, las_date + 1):
			for d in domain:
				data_list += self.domain_hotnews[d](date=str(i), nums=str(nums))

		# 索引构建
		for index, entry in enumerate(data_list):
			entry['index'] = index
		data.set_data(data_list)


		return data

	def get_search_news(self, keys: list, method: str, date: list, nums: int) -> RetrieveResult:
		"""
		获取基于关键字的新闻检索结果
		:param keys:
		:param method:
		:param date:
		:param nums:
		:return:
		"""
		# 数据处理
		sdate, edate = date
		stime = sdate + ('+' + '00:00:00') if sdate != '' else ''
		etime = edate + ('+' + '23:59:59') if edate != '' else ''

		# 检索对象创建
		data = RetrieveResult(intent=self.intent, subintent=self.subintent[1])

		# 信息检索
		page = 1
		data_list = []
		while len(data_list) < nums:
			news_list = SearchNewsDao.get_search_result(key_list=keys, method=self.search_method[method], stime=stime,
			                                            etime=etime, page=str(page))
			if len(news_list) == 0:
				break
			data_list += news_list
			page += 1

		# 索引构建
		for index, entry in enumerate(data_list):
			entry['index'] = index
		data.set_data(data_list[:nums])

		return data

	def exception_handling(self, param, code: int, index: int) -> dict:
		"""
		新闻检索异常处理
		:param param:
		:param code: 异常类型
		:param index: 子意图索引
		:return:
		"""
		# 检索对象创建
		data = RetrieveResult(intent=self.intent, subintent=self.subintent[index])
		exception_fn = {
			1: data.get_miss_data
		}

		# 异常数据处理
		data_dict = exception_fn[code](param)

		return data_dict
