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
	@encyclopedia_controller_url.route('search_keys/', methods=['GET'])
	def search_keys() -> dict:
		"""
		基于关键字百科检索功能实现
		{
		'keys': list, [k1, k2, ...] 必填
		'method': string 可空
		'nums': int 可空
		}
		:return:
		"""
		# 参数获取
		param = request.get_json()
		req_keys = param['keys']
		req_method = param['method']
		req_nums = param['nums']

		# 对象创建
		service = EncyclopediaOperator()

		# 参数预处理
		if len(req_keys) == 0:
			return service.exception_handling(reason='缺失搜索关键字参数！', fn_index=0)
		if req_method == '':
			req_method = '标题'
		if req_nums == -1:
			req_nums = 20

		# 功能调用
		data_object = service.get_search_content(keys=req_keys, method=req_method, nums=req_nums)
		data_dict = data_object.get_dict_data()

		return data_dict
