import sys

sys.path.append(".")
from flask import Blueprint, jsonify
from src.utils.response import Response

error = Blueprint("error", __name__)


@error.app_errorhandler(400)
def error_400(page):
    return jsonify(Response.error(message="请求错误", code=400, result=None))


@error.app_errorhandler(403)
def error_403(page):
    return jsonify(Response.error(message="禁止访问", code=403, result=None))


@error.app_errorhandler(404)
def error_404(page):
    return jsonify(Response.error(message="页面不存在", code=404, result=None))


@error.app_errorhandler(405)
def error_405(page):
    return jsonify(Response.error(message="方法不被允许", code=405, result=None))


@error.app_errorhandler(413)
def error_413(page):
    return jsonify(Response.error(message="文件大小过大", code=415, result=None))


@error.app_errorhandler(415)
def error_415(page):
    return jsonify(Response.error(message="不支持的媒体类型", code=415, result=None))


@error.app_errorhandler(500)
def error_500(page):
    return jsonify(Response.error(message="服务器错误", code=500, result=None))
