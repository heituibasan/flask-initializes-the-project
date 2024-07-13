#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/28 下午9:25
# @FileSpec : 用于接口返回数据

import sys

sys.path.append(".")
from datetime import datetime


class Response:
    """
    返回响应信息
    error失败信息
    success成功信息
    """

    def __init__(self):
        self.status = None
        self.result = None

    @staticmethod
    def error(message: str, code=200, result=None):
        """
        响应失败消息
        :param message  返回消息
        :param code 返回代码
        :param result   返回结果
        :return: dict
        """
        return {
            "status": "error",
            "code": code,
            "message": str(message),
            "result": result,
            "timestamp": int(datetime.now().timestamp()),
        }

    @staticmethod
    def success(message: str, code=200, result=None):
        """
        响应成功消息
        :param message  返回消息
        :param code 返回代码
        :param result   返回结果
        :return: dict
        """
        return {
            "status": "success",
            "code": code,
            "message": str(message),
            "result": result,
            "timestamp": int(datetime.now().timestamp()),
        }
