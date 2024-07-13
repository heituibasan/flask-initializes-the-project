#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/28 下午9:18
# @FileSpec :

import sys

sys.path.append(".")
import re
import random
import string


def is_valid_email(email: str) -> bool:
    """
    验证电子邮件格式是否正确

    :param email: str, 电子邮件地址
    :return: bool, 格式正确返回 True，否则返回 False
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return re.match(email_regex, email) is not None


def is_password_strong(password: str) -> bool:
    """
    检查密码是否符合强度要求

    :param password: str, 需要检查的密码
    :return: bool, True表示密码符合强度要求，False表示密码过于简单
    """
    if len(password) < 6:
        return False

    if re.search(r"\s", password):  # 检查密码是否包含空格
        return False

    if not re.search("[a-z]", password):
        return False

    if not re.search("[A-Z]", password):
        return False

    if not re.search("[0-9]", password):
        return False

    if not re.search("[@#$%^&+=]", password):
        return False

    return True


def contains_special_characters(content: str) -> bool:
    """
    检查文本是否包含特殊字符

    :param content: str, 需要检查的文本
    :return: bool, True表示包含，False表示不包含
    """
    if not re.search("[@#$%^&+=]", content):
        return False

    return True


def generate_verification_code(length=6) -> str:
    """
    生成包含大写字母和数字（不包含字母O）的随机验证码

    :param length: int, 验证码长度，默认为6
    :return: str, 随机验证码
    """
    characters = (
        string.ascii_uppercase.replace("O", "") + string.digits
    )  # 包含大写字母和数字，去掉字母O
    verification_code = "".join(random.choice(characters) for _ in range(length))
    return verification_code


if __name__ == "__main__":
    print(is_valid_email("1839qq.com"))
    code = generate_verification_code()
    print(f"生成的验证码: {code}")
