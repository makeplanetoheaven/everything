# coding=utf-8

"""
author: wlc
function: 知乎检索业务逻辑层
"""

# 引入外部库

# 引入内部库
from src.dao.zhihuDao import *
from src.entity.retrieveResult import *


class ZhihuOperator:
	def __init__ (self):
		# 该业务逻辑功能
		self.intent = '知乎'

		# 该业务逻辑子功能
		self.subintent = {
			0: '知乎热榜检索',
			1: '关键字检索'
		}

	def get_billboard (self) -> RetrieveResult:
		"""
		获取知乎热榜内容
		:return:
		"""
		# 检索对象创建
		data = RetrieveResult(intent=self.intent, subintent=self.subintent[0])

		# 信息检索
		data.set_data(zhihuDao.get_billboard_result())

		return data
