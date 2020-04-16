#!/usr/bin/env python3
# coding=utf-8

"""
author: wlc
function: everything启动脚本
"""

# 引入外部库
from flask_script import Manager
from gevent.pywsgi import WSGIServer
import sys

# 引入内部库
from src.controller import create_controller
from src.util import globalArgs


if __name__ == '__main__':
	# 参数处理
	if len(sys.argv) > 1:
		port = sys.argv[1]
	else:
		port = 18080

	# 系统初始化
	globalArgs._init_()

	# sever启动
	controller = create_controller()
	http_server = WSGIServer(('', port), controller)
	http_server.serve_forever()
