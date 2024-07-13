#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/7/4 下午3:48
# @FileSpec : 设置服务接口


from src.model.SettingModel import Setting
from src.handler.message import SettingErrorMessage, SuccessMessage
from src.utils.response import Response


def get_all_settings():
    """
    获取设置中所有内容
    :return:
    """
    settings = Setting.get_all()
    return Response.success(message=SuccessMessage.REQUEST_SUCCESS, result=[item.to_dict() for item in settings])


def update(setting_id: int, setting_value: str):
    """
    更新数据
    :param setting_id: 索引id
    :param setting_value: 需要更新的数据
    :return:
    """
    setting = Setting.get_by_id(setting_id)
    if not setting:
        return Response.error(message=SettingErrorMessage.SETTING_NOT_FOUND)
    setting.update(setting_id=setting_id, setting_value=setting_value)
    return Response.success(message=SuccessMessage.UPDATE_SUCCESS)


def get_setting(setting_id: int):
    """
    根据设置ID获取单个ID
    :param setting_id:
    :return:
    """
    setting = Setting.get_by_id(setting_id)
    if not setting:
        return Response.error(message=SettingErrorMessage.SETTING_NOT_FOUND)
    return Response.success(message=SuccessMessage.REQUEST_SUCCESS, result=setting.to_dict())
