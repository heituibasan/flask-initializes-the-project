#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/30 下午4:53
# @FileSpec : 装饰器

from functools import wraps
from flask import request, jsonify
from src.utils.response import Response
from src.handler.message import ErrorMessage
from src.config.config import Config as config


def check_content_type_json(func):
    """
    检查请求头的装饰器函数，确保 Content-Type 是 application/json。

    :param func: 被装饰的视图函数
    :return: 装饰后的视图函数
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        在调用视图函数之前检查请求头。

        如果请求头不是 application/json，则返回错误响应。

        :param args: 视图函数的位置参数
        :param kwargs: 视图函数的关键字参数
        :return: 视图函数的返回结果或错误响应
        """
        if request.headers.get("Content-Type") != "application/json":
            return jsonify(Response.error("请求头错误", result=None))
        return func(*args, **kwargs)

    return wrapper


def validate_req_sign(func):
    """
    检查请求中的 req_sign 参数是否正确的装饰器函数。

    :param func: 被装饰的视图函数
    :return: 装饰后的视图函数
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        在调用视图函数之前检查 req_sign 参数。

        如果请求中没有或者 req_sign 参数与配置不匹配，则返回错误响应。

        :param args: 视图函数的位置参数
        :param kwargs: 视图函数的关键字参数
        :return: 视图函数的返回结果或错误响应
        """
        req_sign = request.get_json().get("req_sign")
        if not req_sign or req_sign != config.REQ_SIGN:
            return jsonify(Response.error(ErrorMessage.INVALID_REQ_SIGN))
        return func(*args, **kwargs)

    return wrapper
