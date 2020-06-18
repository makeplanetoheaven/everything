# coding=utf-8

"""
author: wlc
function: 百科检索业务逻辑层
"""

# 引入外部库

# 引入内部库
from src.dao.encyclopediaDao import *
from src.entity.retrieveResult import *


class EncyclopediaOperator:
	def __init__ (self):
		# 该业务逻辑功能
		self.intent = '百科检索'

		# 该业务逻辑子功能
		self.subintent = {
			0: '关键字检索',
			1: 'FAQ检索'
		}

		# 关键字百科检索参数
		self.search_method = {
			'标题': 'title',
			'全文': 'all',
			'词条': ''
		}

	def get_search_content(self, keys: list, method: str, nums: int) -> RetrieveResult:
		"""
		获取基于关键字的百科检索结果
		:param keys:
		:param method:
		:param nums:
		:return:
		"""
		# 数据处理

		# 检索对象创建
		data = RetrieveResult(intent=self.intent, subintent=self.subintent[1])

		# 信息检索
		page = 1
		data_list = []
		while len(data_list) < nums:
			news_list = EncyclopediaDao.get_keys_result(key_list=keys, method=self.search_method[method], page=str(page))
			if len(news_list) == 0:
				break
			data_list += news_list
			page += 1
		data.set_data(data_list)

		return data

	def exception_handling(self, reason: str, fn_index: int) -> dict:
		"""
		百科检索异常处理
		:param reason:
		:param fn_index:
		:return:
		"""
		# 检索对象创建
		data = RetrieveResult(intent=self.intent, subintent=self.subintent[fn_index])

		data_dict = data.get_exception_data(reason)

		return data_dict
