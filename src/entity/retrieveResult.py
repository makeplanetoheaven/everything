# coding=utf-8

"""
author: wlc
function: 信息检索结果实体
"""

# 引入外部库

# 引入内部库


class RetrieveResult:
	def __init__(self, intent: str, subintent: str):
		"""
		数据初始化
		:param intent:
		:param subintent:
		"""
		# 配置项
		self.conf = {
			'intent': intent,
			'subintent': subintent,
		}

		# 数据项
		self.data = []

	def set_data(self, data_list: list) -> None:
		"""
		添加检索数据
		:param data_list:
		:return:
		"""
		self.data += data_list

	def get_dict_data(self) -> dict:
		"""
		返回数据的JSON格式
		:return:
		"""
		data = {
			'conf': self.conf,
			'data': self.data,
			'status': 1
		}

		return data

	def get_exception_data(self, reason) -> dict:
		"""
		异常检索数据构建
		:param reason:
		:return:
		"""
		data = {
			'conf': self.conf,
			'data': self.data,
			'status': 0,
			'reason': reason
		}

		return data
