# coding=utf-8

"""
author: wlc
function: 知乎检索控制层
"""

# 引入外部库
from flask import Blueprint
from flask import request

# 引入内部库
from src.service.zhihuOperator import *
from src.util import globalArgs

zhihu_controller_url = Blueprint('zhihu_controller', __name__, url_prefix='/zhihu')


class ZhihuController:
	@staticmethod
	@zhihu_controller_url.route('billboard/', methods=['GET'])
	def billboard () -> dict:
		"""
		知乎热榜检索功能实现
		{
		}
		:return:
		"""
		# 功能调用
		data_object = ZhihuOperator().get_billboard()
		data_dict = data_object.get_dict_data()

		return data_dict

	@staticmethod
	@zhihu_controller_url.route('search/', methods=['GET'])
	def search() -> dict:
		"""
		基于关键字新闻检索功能实现
		{
		'keys': list, [k1, k2, ...] 必填
		'method': string 可空
		'date': list, [pre, las] 可空
		'nums': int 可空
		}
		:return:
		"""
		# 参数获取
		param = request.get_json()
		req_keys = param['keys']
		req_method = param['method']
		req_date = param['date']
		req_nums = param['nums']

		# 参数预处理
		if len(req_keys) == 0:
			return NewsOperator().exception_handling(reason='缺失搜索关键字参数！', fn_index=1)
		if req_method == '':
			req_method = '标题'
		if len(req_date) == 0:
			req_date = ['', '']
		if req_nums == -1:
			req_nums = 20

		# 功能调用
		data_object = NewsOperator().get_search_news(keys=req_keys, method=req_method, date=req_date, nums=req_nums)
		data_dict = data_object.get_dict_data()

		return data_dict
