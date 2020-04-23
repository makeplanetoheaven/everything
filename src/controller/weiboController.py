# coding=utf-8

"""
author: wlc
function: 微博检索控制层
"""

# 引入外部库
from flask import Blueprint
from flask import request

# 引入内部库
from src.service.weiboOperator import *
from src.util import globalArgs

weibo_controller_url = Blueprint('weibo_controller', __name__, url_prefix='/weibo')


class WeiboController:
	@staticmethod
	@weibo_controller_url.route('realtimehot/', methods=['GET'])
	def realtimehot () -> dict:
		"""
		微博热搜检索功能实现
		{
		}
		:return:
		"""
		# 功能调用
		data_object = WeiboOperator().get_realtimehot()
		data_dict = data_object.get_dict_data()

		return data_dict
