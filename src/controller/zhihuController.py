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
