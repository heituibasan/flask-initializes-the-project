#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/28 下午9:15
# @FileSpec :


from flask import request, jsonify, render_template, send_from_directory, current_app
from src import initialize
from src.config.config import Config as config
from src.utils import logger
from src.utils.response import Response

logger = logger.get_logger(__name__)
app = initialize.create_app()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')  # 匹配所有路径，用于 Vue Router 处理
def index(path=None):
    if path and path.startswith('api/'):
        return jsonify(Response.error(message="页面不存在", code=404, result=None))
    else:
        return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.template_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    host = config.SERVICE_HOST
    port = config.SERVICE_PORT
    app.run(host=host, port=port, debug=True, threaded=True)
