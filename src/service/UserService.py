#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/30 下午4:58
# @FileSpec :

import os
from datetime import datetime
from src.utils.response import Response
import src.utils.jwtEncode as jwt
import src.utils.encrypt as encrypt
import src.utils.tools as tools
from src.model.UserModel import User
from src.handler.message import UserErrorMessage, SuccessMessage
import src.utils.sendEmail as sendEmail
from src.extensions import redis

# HTML模板文件路径
current_dir = os.path.dirname(os.path.abspath(__file__))
html_template_path = os.path.join(current_dir, "../../files/assets/email/UserTemplate/")


def register(username: str, email: str, password: str, create_ip: str, role=0):
    """
    注册用户

    :param username: str, 用户名
    :param email: str, 电子邮件地址
    :param password: str, 密码
    :param create_ip: str, 创建用户时的IP地址
    :param role: int, 用户角色，默认值为0
    :return: Response, 注册结果的响应
    """
    # 验证邮箱格式
    if not tools.is_valid_email(email):
        return Response.error(message=UserErrorMessages.INVALID_EMAIL_FORMAT)

    # 检查用户名是否包含特殊字符
    if tools.contains_special_characters(content=username):
        return Response.error(message=UserErrorMessages.INVALID_USERNAME_CONTENT)

    # 检查用户是否已经存在
    if User.get_by_email(email):
        return Response.error(message=UserErrorMessages.USER_ALREADY_EXISTS)
    # 验证密码复杂性
    if not tools.is_password_strong(password):
        return Response.error(message=UserErrorMessages.PASSWORD_TOO_SIMPLE)

    # 对密码进行加密
    password = encrypt.hash_password(password)

    # 创建用户
    User.create(
        username=username,
        email=email,
        password=password,
        role=role,
        create_ip=create_ip,
    )

    # 读取、填充HTML模板并发送邮件{email,username,date}
    context = {
        "username": username,
        "email": email,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    template_content = sendEmail.read_html_template(
        html_template_path + "register.html"
    )
    html_content = sendEmail.render_html_template(template_content, context)
    sendEmail.send_email(subject="注册成功", to_email=email, html_content=html_content)

    return Response.success(message=SuccessMessage.REGISTRATION_SUCCESS)


def login(email: str, password: str, last_login_ip: str):
    """
    登录用户

    :param email: str, 电子邮件地址
    :param password: str, 密码
    :param last_login_ip: str,用户登录IP
    :return: Response, 登录结果的响应
    """
    # 验证邮箱格式
    if not tools.is_valid_email(email):
        return Response.error(message=UserErrorMessages.INVALID_EMAIL_FORMAT)

    # 检查用户是否存在
    user = User.get_by_email(user_email=email)

    if not user:
        return Response.error(message=UserErrorMessages.USER_NOT_FOUND)

    # 验证密码是否正确
    if not encrypt.verify_password(user.password, password):
        return Response.error(message=UserErrorMessages.INVALID_PASSWORD)

    # 更新用户的最后登录时间和最后登录IP
    user.update(last_login_time=datetime.now(), last_login_ip=last_login_ip)

    # 返回jwt数据
    user = user.to_dict()
    del user['password']
    del user['code']
    return Response.success(message=SuccessMessage.LOGIN_SUCCESS, result=jwt.encode(user))


def reset_password(email: str, old_password: str, new_password: str):
    """
    重置用户密码

    :param email: str, 用户的电子邮件地址
    :param old_password: str, 用户的旧密码
    :param new_password: str, 用户的新密码
    :return: Response, 重置密码的结果
    """
    # 检查用户是否存在
    user = User.query.filter_by(email=email).first()
    if not user:
        return Response.error(message=UserErrorMessages.USER_NOT_FOUND)

    # 验证旧密码是否正确
    if not encrypt.verify_password(user.password, old_password):
        return Response.error(message=UserErrorMessages.INVALID_OLD_PASSWORD)

    # 检查新密码是否与旧密码不同
    if encrypt.verify_password(user.password, new_password):
        return Response.error(message=UserErrorMessages.PASSWORD_SAME_AS_OLD)

    # 验证新密码复杂性
    if not tools.is_password_strong(new_password):
        return Response.error(message=UserErrorMessages.PASSWORD_TOO_SIMPLE)

    # 对新密码进行加密
    new_password_hashed = encrypt.hash_password(new_password)

    # 更新用户密码
    user.update(password=new_password_hashed, last_login_time=datetime.now())
    # 发送验证码信息到邮箱{email,username,date}
    context = {
        "email": email,
        "username": user.username,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    template_content = sendEmail.read_html_template(
        html_template_path + "reset_password.html"
    )
    html_content = sendEmail.render_html_template(template_content, context)
    sendEmail.send_email(
        subject="密码已重置", to_email=email, html_content=html_content
    )
    return Response.success(message=SuccessMessage.PASSWORD_RESET_SUCCESS)


def send_password_reset_email(email: str):
    """
    生成用于密码重置的令牌

    :param email: str, 用户的电子邮件地址
    :return: Response, 生成令牌的响应
    """
    # 检查用户是否已经存在
    user = User.get_by_email(email)
    if not user:
        return Response.error(message=UserErrorMessages.USER_NOT_FOUND)

    # 生成用户找回密码的验证码
    reset_code = tools.generate_verification_code()

    # 将令牌保存到 Redis，设置过期时间为1小时
    redis.set(f"password_reset_code:{email}", reset_code, ex=60 * 5)  # 令牌有效期1小时

    # 发送验证码信息到邮箱{code}
    context = {"username": email, "code": reset_code}
    template_content = sendEmail.read_html_template(html_template_path + "code.html")
    html_content = sendEmail.render_html_template(template_content, context)
    sendEmail.send_email(subject="验证码", to_email=email, html_content=html_content)

    return Response.success(message=SuccessMessage.EMAIL_SENT_SUCCESS)


def forgot_password(email: str, code: str, password: str, last_login_ip: str):
    """
    收到用户的验证码以后，对用户密码进行重置

    :param email: str, 用户的电子邮件地址
    :param code: str, 用户收到的验证码
    :param password: str, 用户设置的新密码
    :return: Response, 重置结果
    """
    # 检查用户是否已经存在
    user = User.get_by_email(email)
    if not user:
        return Response.error(message=UserErrorMessages.USER_NOT_FOUND)

    # 检查在Redis当中是否存在用户验证码
    stored_code = redis.get(f"password_reset_code:{email}")
    if not stored_code or stored_code.decode("utf-8") != code:
        return Response.error(message=UserErrorMessages.INVALID_RESET_CODE)

    # 验证密码强度
    if not tools.is_password_strong(password):
        return Response.error(message=UserErrorMessages.PASSWORD_TOO_SIMPLE)
    # 对新密码进行加密
    encrypted_password = encrypt.hash_password(password)
    # 更新用户密码
    user.password = encrypted_password
    user.update(last_login_time=datetime.now(), last_login_ip=last_login_ip)
    # 删除 Redis 中的验证码
    redis.delete(f"password_reset_code:{email}")
    return Response.success(message=SuccessMessage.PASSWORD_RESET_SUCCESS)


def update(
        username: str,
        email: str,
        password: str,
        phone: int,
        qq: int,
        address: str,
        city: str,
):
    """
    接收用户数据，对于用户数据进行更新

    :param username: str, 用户在系统中展示的名称
    :param email: str, 用户的电子邮件地址
    :param password: str, 用户登录密码
    :param phone: str, 用户绑定电话
    :param qq: str, 用户绑定QQ
    :param address: str, 用户具体居住地址
    :param city: str, 用户所属城市
    :return: Response, 更新结果
    """
    # 检查用户名是否包含特殊字符
    if tools.contains_special_characters(content=username):
        return Response.error(message=UserErrorMessages.INVALID_USERNAME_CONTENT)

    # 检查电话长度是否合格
    if phone is not None:
        if len(phone) != 11:
            return Response.error(message=UserErrorMessages.PHONE_NUMBER_INVALID)

    # 检查用户是否已经存在
    user = User.get_by_email(email)
    if not user:
        return Response.error(message=UserErrorMessages.USER_NOT_FOUND)
    # 更新数据
    user.update(
        username=username,
        password=password,
        phone=phone,
        qq=qq,
        address=address,
        city=city,
    )
    return Response.success(message=SuccessMessage.UPDATE_SUCCESS)
