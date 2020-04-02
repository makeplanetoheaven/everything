# coding=utf-8

"""
author: wlc
function: 新闻检索控制器
"""

# 引入外部库
from flask import Blueprint


# 引入内部库


new_controller_url = Blueprint('new_controller', __name__, url_prefix='/news')
class NewsController:
	@new_controller_url.route('/hotnews', methods=['POST', 'GET'])
	def search_hotnews (self):
		pass
