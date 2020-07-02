# coding=utf-8

"""
author: wlc
function: 新闻检索控制层
"""

# 引入外部库
from flask import Blueprint
from flask import request

# 引入内部库
from src.service.newsOperator import *
from src.util import globalArgs

news_controller_url = Blueprint('new_controller', __name__, url_prefix='/news')


class NewsController:
	@staticmethod
	@news_controller_url.route('hotnews/', methods=['POST'])
	def hotnews () -> dict:
		"""
		热点新闻检索功能实现
		{
		'domain': list, [d1, d2, ...] 可空
		'date': list, [pre, las] 可空
		'nums': int 可空
		}
		:return:
		"""
		# 参数获取
		param = request.get_json()
		req_domain = param['domain']
		req_date = param['date']
		req_nums = param['nums']

		# 对象创建
		service = NewsOperator()

		# 参数预处理
		if len(req_domain) == 0:
			req_domain = ['默认']
		if len(req_date) == 0:
			cur_t = time.strftime(globalArgs.get_value('io_date'), time.localtime(time.time()))
			req_date = [cur_t, cur_t]
		if req_nums == -1:
			req_nums = 10

		# 功能调用
		data_object = service.get_domain_hotnews(domain=req_domain, date=req_date, nums=req_nums)
		data_dict = data_object.get_normal_data()

		return data_dict

	@staticmethod
	@news_controller_url.route('search/', methods=['POST'])
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

		# 对象创建
		service = NewsOperator()

		# 参数预处理
		if len(req_keys) == 0:
			return service.exception_handling(param=['keys'], code=1, index=1)
		if req_method == '':
			req_method = '标题'
		if len(req_date) == 0:
			req_date = ['', '']
		if req_nums == -1:
			req_nums = 20

		# 功能调用
		data_object = service.get_search_news(keys=req_keys, method=req_method, date=req_date, nums=req_nums)
		data_dict = data_object.get_normal_data()

		return data_dict
