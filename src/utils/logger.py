#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/29 上午9:27
# @FileSpec : 日志文件

import logging
import os
from datetime import datetime

# 获取日志文件目录
log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'logs')

# 确保日志目录存在
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 获取当前日期并格式化为日志文件名
log_filename = datetime.now().strftime("%Y-%m-%d") + '.log'
log_file = os.path.join(log_dir, log_filename)

# 配置日志系统
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)


def get_logger(name):
    """
    获取一个新的 logger 实例
    :param name: logger 的名称
    :return: logger 实例
    """
    return logging.getLogger(name)


if __name__ == "__main__":
    logger = get_logger(__name__)
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
