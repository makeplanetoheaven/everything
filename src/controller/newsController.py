# coding=utf-8

"""
author: wlc
function: 新闻检索控制层
"""

# 引入外部库
from flask import Blueprint

# 引入内部库
from src.service.newsOperator import *


news_controller_url = Blueprint('new_controller', __name__, url_prefix='/news')
class NewsController:
	@staticmethod
	@news_controller_url.route('hotnews/', methods=['GET'])
	def hotnews ():
		"""
		热点新闻获取检索功能实现
		:return:
		"""
		# 参数获取及预处理

		news_dict = NewsOperator().get_domain_hotnews()

		return news_dict
