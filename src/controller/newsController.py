# coding=utf-8

"""
author: wlc
function: 新闻检索控制器
"""

# 引入外部库
from flask import Blueprint

# 引入内部库
from src.service.newsOperator import *


new_controller_url = Blueprint('new_controller', __name__, url_prefix='/news')
class NewsController:
	@new_controller_url.route('/hotnews', methods=['POST', 'GET'])
	def hotnews (self):
		"""

		:return:
		"""
		news_dict = NewsOperator().get_domain_hotnews()

		return news_dict
