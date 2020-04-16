# coding=utf-8

"""
author: 王黎成
function: 全局变量使用模块
"""

# 引入外部库

# 引入内部库

# 全局变量
__global_dict = {}


def _init_ ():
	"""
	全局变量的初始化
	全局变量中，大写KEY是内部接口，小写KEY是外部接口
	:return:
	"""
	global __global_dict

	# <editor-fold desc="数据接口">
	__global_dict['io_date'] = '%Y-%m-%d'
	__global_dict['io_time'] = '%H:%M:%S'
	# </editor-fold>

	pass


def set_value (key, value):
	"""
	全局变量的添加及修改
	:param key: 关键字
	:param value: 需要修改或添加的值
	:return:
	"""
	global __global_dict

	if key not in __global_dict:
		__global_dict[key] = value
	else:
		__global_dict[key] += value


def get_value (key, def_value=None):
	"""
	全局变量的获取
	:param key: 关键字
	:param def_value:默认值
	:return:
	"""
	global __global_dict

	try:
		return __global_dict[key]
	except KeyError:
		return def_value
