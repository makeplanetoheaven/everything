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
			1: 'FAQ检索',
			2: 'KG检索'
		}

		# 关键字百科检索参数
		self.search_method = {
			'内容': EncyclopediaDao.get_key_content,
			'标题': EncyclopediaDao.get_key_title
		}

	def get_search_key(self, key: str, method: str) -> RetrieveResult:
		"""
		获取基于关键字的百科检索结果
		:param key:
		:param method:
		:return:
		"""
		# 检索对象创建
		data = RetrieveResult(intent=self.intent, subintent=self.subintent[0])

		# 信息检索
		data.set_data(self.search_method[method](key=key))

		return data

	def get_search_faq(self, query: str, nums: int) -> RetrieveResult:
		"""
		获取基于faq的百科检索结果
		:param query:
		:param nums:
		:return:
		"""
		# 检索对象创建
		data = RetrieveResult(intent=self.intent, subintent=self.subintent[1])

		# 信息检索
		page = 1
		data_list = []
		while len(data_list) < nums:
			faq_list = EncyclopediaDao.get_faq_content(query=query, page=str(page))
			if len(faq_list) == 0:
				break
			data_list += faq_list
			page += 1

		# 索引构建
		for index, entry in enumerate(data_list):
			entry['index'] = index
		data.set_data(data_list[:nums])

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
