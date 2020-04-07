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
		self.domain_hotnews = {'default': HotNewsDao().get_default_hotnews}

	def get_domain_hotnews (self, domain='default') -> dict:
		"""
		获取指定领域的热点新闻
		:param domain:
		:return:
		"""


		return self.domain_hotnews[domain]()
