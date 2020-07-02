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

	def get_normal_data(self) -> dict:
		"""
		返回正常处理数据
		status_code: 0
		:return:
		"""
		data = {
			'conf': self.conf,
			'data': self.data,
			'status': {   # 状态项
				'code': 0
			}
		}

		return data

	def get_miss_data(self, param: list) -> dict:
		"""
		返回参数缺失数据
		status_code: 1
		:param param:
		:return:
		"""
		data = {
			'conf': self.conf,
			'data': self.data,
			'status': {   # 状态项
				'code': 1,
				'param': param
			}
		}

		return data
