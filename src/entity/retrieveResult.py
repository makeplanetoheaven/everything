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
		:param domain:
		"""
		self.conf = {
			'intent': intent,
			'subintent': subintent,
		}
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
			'data': self.data
		}

		return data
