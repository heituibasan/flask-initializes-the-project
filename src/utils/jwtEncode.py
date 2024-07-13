#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/28 下午9:24
# @FileSpec :
import sys

sys.path.append(".")
import jwt
from datetime import datetime, timedelta
from jwt import ExpiredSignatureError, InvalidSignatureError, DecodeError
from src.utils.response import Response

# 秘钥
secret = 'yuassistant'
# 登录有效时间 默认为24小时
effective_time = timedelta(hours=24)
# 加密算法
algorithm = 'HS256'


def encode(info: any):
    """
    JWT加密
    :param info   需要JWT加密的内容
    """
    payload = {
        'info': info,
        'exp': datetime.utcnow() + effective_time
    }
    return jwt.encode(payload, secret, algorithm=algorithm)
    # return jwt.encode(payload, secret, algorithm=algorithm).decode('utf-8')


def decode(encode: str):
    """
    JWT解密
    :param encode   需要JWT解密的内容
    """
    try:
        return jwt.decode(encode, secret, algorithms=algorithm)
    except ExpiredSignatureError:
        return '令牌已过期'
    except InvalidSignatureError:
        return '无效签名。令牌的签名与预期的签名不匹配'
    except DecodeError as err:
        print(err)
        return '解码错误。由于格式或标头信息错误，无法对令牌进行解码'
    except Exception as err:
        return '发生意外错误'
    except jwt.ExpiredSignatureError:
        return '令牌已过期'


if __name__ == '__main__':
    info = {
        "username": "zhangsan",
        "email": "2131@qq.com",
        "password": "<PASSWORD>",
    }
    encoded = encode(info)
    # 加密
    print(encoded)
    # 解密
    print(decode(encoded))
