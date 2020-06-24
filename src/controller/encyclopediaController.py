# coding=utf-8

"""
author: wlc
function: 百科检索控制层
"""

# 引入外部库
from flask import Blueprint
from flask import request

# 引入内部库
from src.service.encyclopediaOperator import *
from src.util import globalArgs

encyclopedia_controller_url = Blueprint('encyclopedia_controller', __name__, url_prefix='/encyclopedia')


class EncyclopediaController:
	@staticmethod
	@encyclopedia_controller_url.route('search_key/', methods=['POST'])
	def search_key() -> dict:
		"""
		基于关键字百科检索功能实现
		{
		'key': string 必填
		'method': string 可空
		}
		:return:
		"""
		# 参数获取
		param = request.get_json()
		req_key = param['key']
		req_method = param['method']

		# 对象创建
		service = EncyclopediaOperator()

		# 参数预处理
		if len(req_key) == 0:
			return service.exception_handling(reason='缺失搜索关键字参数！', fn_index=0)
		if req_method == '':
			req_method = '内容'

		# 功能调用
		data_object = service.get_search_key(key=req_key, method=req_method)
		data_dict = data_object.get_dict_data()

		return data_dict

	@staticmethod
	@encyclopedia_controller_url.route('search_faq/', methods=['POST'])
	def search_faq() -> dict:
		"""
		基于faq百科检索功能实现
		{
		'query': string 必填
		'nums': int 可空
		}
		:return:
		"""
		# 参数获取
		param = request.get_json()
		req_query = param['query']
		req_nums = param['nums']

		# 对象创建
		service = EncyclopediaOperator()

		# 参数预处理
		if len(req_query) == 0:
			return service.exception_handling(reason='缺失搜索问题参数！', fn_index=1)
		if req_nums == -1:
			req_nums = 5

		# 功能调用
		data_object = service.get_search_faq(query=req_query, nums=req_nums)
		data_dict = data_object.get_dict_data()

		return data_dict
