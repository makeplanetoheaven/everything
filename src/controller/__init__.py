# coding=utf-8

"""
author: wlc
function: url注册函数
"""

# 引入外部库
from flask import Flask

# 引入内部库
from src.controller.newsController import news_controller_url
from src.controller.zhihuController import zhihu_controller_url


def create_controller ():
	controller = Flask(__name__)

	# news controller
	controller.register_blueprint(blueprint=news_controller_url)

	# zhihu controller
	controller.register_blueprint(blueprint=zhihu_controller_url)

	return controller
