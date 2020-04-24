# coding=utf-8

"""
author: wlc
function: 微博检索业务逻辑层
"""

# 引入外部库

# 引入内部库
from src.dao.weiboDao import *
from src.entity.retrieveResult import *


class WeiboOperator:
	def __init__ (self):
		# 该业务逻辑功能
		self.intent = '微博检索'

		# 该业务逻辑子功能
		self.subintent = {
			0: '微博热搜检索',
			1: '关键字检索'
		}

	def get_realtimehot (self) -> RetrieveResult:
		"""
		获取微博热搜内容
		:return:
		"""
		# 检索对象创建
		data = RetrieveResult(intent=self.intent, subintent=self.subintent[0])

		# 信息检索
		data.set_data(WeiboDao.get_realtimehot_result())

		return data
