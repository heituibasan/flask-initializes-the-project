#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/28 下午10:12
# @FileSpec : 用户接口

from flask import Blueprint, current_app, render_template, jsonify, request
from src.handler.decorators import check_content_type_json, validate_req_sign
from src.handler.message import UserErrorMessage
from src.utils.response import Response
from src.service import UserService

users = Blueprint("users", __name__, url_prefix="/api/users")


@users.route("/login", methods=["POST"])
@check_content_type_json
@validate_req_sign
def login():
    """
    登录用户

    :return: Response, 登录的结果
    """
    data = request.get_json()
    if not data.get("email"):
        return jsonify(Response.error(UserErrorMessage.EMAIL_REQUIRED))
    if not data.get("password"):
        return jsonify(Response.error(UserErrorMessage.PASSWORD_REQUIRED))

    email = data.get("email").strip()
    password = data.get("password").strip()
    return UserService.login(
        email=email, password=password, last_login_ip=request.remote_addr
    )


@users.route("/register", methods=["POST"])
@check_content_type_json
@validate_req_sign
def register():
    """
    注册用户

    :return: Response, 注册的结果
    """
    data = request.get_json()
    if not data.get("username"):
        return jsonify(Response.error(UserErrorMessage.USERNAME_REQUIRED))
    if not data.get("email"):
        return jsonify(Response.error(UserErrorMessage.EMAIL_REQUIRED))
    if not data.get("password"):
        return jsonify(Response.error(UserErrorMessage.PASSWORD_REQUIRED))

    email = data.get("email").strip()
    password = data.get("password").strip()
    username = data.get("username").strip()
    return UserService.register(
        email=email, password=password, username=username, create_ip=request.remote_addr
    )


@users.route("/reset_password", methods=["POST"])
@check_content_type_json
@validate_req_sign
def reset_password():
    """
    重置用户密码的视图函数

    :return: Response, 重置密码的结果
    """
    data = request.get_json()
    if not data.get("email"):
        return jsonify(Response.error(UserErrorMessage.EMAIL_REQUIRED))
    if not data.get("old_password"):
        return jsonify(Response.error(UserErrorMessage.OLD_PASSWORD_REQUIRED))
    if not data.get("new_password"):
        return jsonify(Response.error(UserErrorMessage.NEW_PASSWORD_REQUIRED))

    email = data.get("email")
    old_password = data.get("old_password").strip()
    new_password = data.get("new_password").strip()

    return UserService.reset_password(
        email=email, old_password=old_password, new_password=new_password
    )


@users.route("/send_code", methods=["POST"])
@check_content_type_json
@validate_req_sign
def request_password_reset():
    """
    请求密码重置令牌的视图函数

    :return: Response, 生成密码重置验证码的结果
    """
    data = request.get_json()
    if not data.get("email"):
        return jsonify(Response.error(UserErrorMessage.EMAIL_REQUIRED))

    email = data.get("email").strip()
    return UserService.send_password_reset_email(email=email)


@users.route("/forgot_password", methods=["POST"])
@check_content_type_json
@validate_req_sign
def forgot_password():
    """
    接收验证码，对密码进行重置

    :return: Response, 密码重置的结果
    """
    data = request.get_json()
    if not data.get("email"):
        return jsonify(Response.error(UserErrorMessage.EMAIL_REQUIRED))
    if not data.get("code"):
        return jsonify(Response.error(UserErrorMessage.CODE_REQUIRED))
    if not data.get("password"):
        return jsonify(Response.error(UserErrorMessage.NEW_PASSWORD_REQUIRED))
    email = data.get("email").strip()
    code = data.get("code").strip()
    password = data.get("password").strip()
    return UserService.forgot_password(
        email=email, code=code, password=password, last_login_ip=request.remote_addr
    )


@users.route("/update", methods=["POST"])
@check_content_type_json
@validate_req_sign
def update():
    """
    接收用户数据，对用户信息进行更新

    :return: Response, 密码更新的结果
    """
    data = request.get_json()
    if not data.get("email"):
        return jsonify(Response.error(UserErrorMessage.EMAIL_REQUIRED))
    username = data.get("username").strip()
    email = data.get("email").strip()
    password = data.get("password").strip()
    phone = int(data.get("phone").strip())
    qq = int(data.get("qq").strip())
    address = data.get("address").strip()
    city = data.get("city").strip()
    return jsonify(
        UserService.update(
            username=username,
            email=email,
            password=password,
            phone=phone,
            qq=qq,
            address=address,
            city=city,
        )
    )
