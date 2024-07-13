#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/7/4 下午3:47
# @FileSpec : 设置接口

from flask import Blueprint, request, jsonify
from src.handler.decorators import check_content_type_json, validate_req_sign
from src.handler.message import ErrorMessage

from src.utils.response import Response
from src.service import SettingService

settings = Blueprint("settings", __name__, url_prefix="/api/settings")


@settings.route("/get_setting", methods=["POST"])
@check_content_type_json
@validate_req_sign
def get_setting():
    data = request.get_json()
    if not data.get("id"):
        return jsonify(Response.error(ErrorMessage.ID_REQUIRED))
    setting_id = int(data.get("id").strip())
    return jsonify(SettingService.get_setting(setting_id=setting_id))


@settings.route("/", methods=["POST"])
@check_content_type_json
@validate_req_sign
def get_settings():
    return jsonify(SettingService.get_all_settings())


@settings.route("/update", methods=["POST"])
@check_content_type_json
@validate_req_sign
def update():
    """
    更新设置表中内容
    :return:
    """
    data = request.get_json()
    if not data.get("id"):
        return jsonify(Response.error(ErrorMessage.ID_REQUIRED))
    setting_id = int(data.get("id").strip())
    setting_value = data.get("value").strip()
    if setting_value is None:
        return jsonify(Response.error(ErrorMessage.CONTENT_IS_NULL))
    return jsonify(SettingService.update(setting_id=setting_id, setting_value=setting_value))
