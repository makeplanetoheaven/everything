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

news_controller_url = Blueprint('new_controller', __name__, url_prefix='/news')


class NewsController:
	@staticmethod
	@news_controller_url.route('hotnews/', methods=['GET'])
	def hotnews ():
		"""
		热点新闻检索功能实现，参数可全为空
		{
		'domain': string,
		'date': string,
		'period': string,
		'nums': string
		}
		:return:
		"""
		# 参数获取
		param = request.get_json()
		req_domain = param['domain']
		req_date = param['date']
		req_period = param['period']
		req_nums = param['nums']

		# 参数预处理
		if req_domain == '':
			req_domain = 'default'
		if req_date == '' and req_period == '':
			req_date = time.strftime('%Y%m%d',time.localtime(time.time()))
		if req_nums == '':
			req_nums = '10'

		# 功能调用
		news_dict = NewsOperator().get_domain_hotnews(domain=req_domain, date=req_date, period=req_period,
		                                              nums=req_nums)

		return news_dict
