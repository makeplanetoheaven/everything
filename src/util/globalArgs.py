# coding=utf-8

"""
author: 王黎成
function: 全局变量使用模块
"""

# 引入外部库
from pathlib import Path
import json

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
		# <editor-fold desc="Interface">
		print('loading Interface STD IO')
		__global_dict['OUTPUT'] = print
		__global_dict['INPUT'] = input

		print('loading Interface SCRIPT IO')
		__global_dict['SCRIPT_IO'] = Jar()
		__global_dict['SCRIPT_IO'].start(__global_dict['SCRIPT_JAR_PATH'],
		                                 [__global_dict['udid'], __global_dict['package_name'], './Cache/TestTemp'])

		print('loading BERT ARGS')
		bert_args = BertArgs()
		__global_dict['BERT_ARGS'] = bert_args.set_args()

		print('loading PRETRAINED_MODEL PARAMETERS')
		parameters = load_parameters_to_cpu(__global_dict.get('BERT_ARGS'))
		__global_dict['NEW_STATE_DICT'] = parameters.load()
		# </editor-fold>
		# <editor-fold desc="Object">
		print('loading PREDICT_NEXT_SENTENCE_MODEL')
		__global_dict['PREDICT_NEXT_SENTENCE_MODEL'] = PredictModel()

		print('loading SIM_NET_MODEL')
		with open('./SimNet/DSSM/Word2Vec/CharactersEmbedding.json', 'r', encoding='utf-8') as file_object:
			embedding_dict = json.load(file_object)
		char_dict = {}
		vec_set = []
		i = 0
		for key in embedding_dict:
			char_dict[key] = i
			vec_set.append(embedding_dict[key][0])
			i += 1
		__global_dict['SIM_NET_MODEL'] = TransformerDSSM(dict_set=char_dict, vec_set=vec_set, is_train=False)
		__global_dict['SIM_NET_MODEL'].build_graph_by_cpu()
		__global_dict['SIM_NET_MODEL'].start_session()
		# __global_dict['SIM_NET_MODEL'] = PretrainedVector('./SimNet/Model/sgns.baidubaike.bigram-char')
		# </editor-fold >
		# <editor-fold desc="Param">
		print('loading verify_text')
		__global_dict['verify_text'] = ['请输入短信验证码', '请输入短信密码', '请输入验证码', '输入动态密码']
		print('loading mask_content')
		mask_content = ['¥', '￥']
		if 'mask_content' in __global_dict:
			__global_dict['mask_content'] += mask_content
		else:
			__global_dict['mask_content'] = mask_content

		print('loading expect_result')
		expect_result = ['点击密码输入错误', '点击登录密码修改成功']
		if 'expect_result' in __global_dict:
			__global_dict['expect_result'] += expect_result
		else:
			__global_dict['expect_result'] = expect_result
		# </editor-fold >

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
