# coding=utf-8

"""
author: 王黎成
function: 全局变量使用模块
"""

# 引入外部库
from pathlib import Path
import json
import os

# 引入内部库

# 全局变量
__global_dict = {}


class GlobalArgs:
	def __init__ (self):
		"""
		全局变量的初始化
		全局变量中，大写KEY是内部接口，小写KEY是外部接口
		:return:
		"""
		global __global_dict

		# <editor-fold desc="Dir">
		print('loading Dir SCRIPT_JAR_PATH')
		__global_dict['SCRIPT_JAR_PATH'] = './Util/Data/Jar/chinese_script_executor.jar'

		print('loading Dir PREDICT_NEXT_SENTENCE_PATH PATH')
		__global_dict[
			'PREDICT_NEXT_SENTENCE_MODEL PATH'] = './NLI/ModelMemory/PredictNextSentenceBert/model/checkpoints/bert_predict_next_sentence.pth'

		print('loading Dir PYTORCH_PRETRAINED_BERT_CACHE')
		__global_dict['PYTORCH_PRETRAINED_BERT_CACHE'] = Path(
			os.getenv('PYTORCH_PRETRAINED_BERT_CACHE', './NLI/ModelMemory/PretrainedBertCache/.pytorch_pretrained_bert'))
		# </editor-fold>

		pass

	def set_value (self, key, value):
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

	def get_value (self,key, def_value=None):
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
