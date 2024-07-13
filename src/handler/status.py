#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/7/4 下午4:10
# @FileSpec : 状态


def user_status(status: str | int) -> None | int | str:
    """
    用户状态信息
    """
    status_num = {
        0: "普通用户",
        1: "游客",
        2: "管理员",
    }
    if status in dict([list(item)[::-1] for item in status_num.items()]):
        return dict([list(item)[::-1] for item in status_num.items()]).get(status)
    try:
        if int(status) in status_num.keys():
            return status_num.get(status)
    except Exception as err:
        return None
