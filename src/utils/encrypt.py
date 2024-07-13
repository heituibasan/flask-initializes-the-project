#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/30 下午5:34
# @FileSpec :

import sys

sys.path.append(".")

import hashlib
import os
from src.config.config import Config
from src.utils.response import Response

config = Config()

# 加密盐
salt = config.ENCRYPT_SALT


def hash_password(password: str) -> str:
    """
    使用PBKDF2算法对密码进行哈希加密
    :param password: 需要进行哈希加密的密码
    :return: str,加密后的密码
    """

    result = None
    hash_str = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt.encode("utf-8"), 100000
    )
    return hash_str.hex()


def verify_password(stored_password: str, provided_password: str) -> bool:
    """
    对哈希密码和原始密码进行对比

    :param stored_password: 加密以后的哈希密码
    :param provided_password: 原始密码（明文）
    :return: bool
    """

    if stored_password == hash_password(provided_password):
        return True
    return False


if __name__ == "__main__":
    ha = hash_password(password="xiaocilx20021118")
    print(ha)
    print(verify_password(ha, "xiaocilx20021118"))
