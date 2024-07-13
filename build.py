#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/29 上午9:16
# @FileSpec : 构建前端代码

import subprocess
import os
from src.utils import logger

logger = logger.get_logger(__name__)


def run_command(command, cwd):
    """运行 shell 命令并返回其输出和错误信息"""
    result = subprocess.run(command, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = result.stdout.decode('utf-8', errors='ignore')
    stderr = result.stderr.decode('utf-8', errors='ignore')
    return stdout, stderr


def build_frontend():
    """在 frontend 文件夹中运行打包命令"""
    frontend_dir = os.path.join(os.path.dirname(__file__), 'frontend')
    logger.info("正在安装所需依赖...")
    # 安装依赖
    out, err = run_command('npm install', frontend_dir)
    print(out)
    if err:
        print(err)
    # 构建程序
    logger.info("正在构建程序...")
    out, err = run_command('npx run-p type-check "build-only {@}" --', frontend_dir)
    print(out)
    if err:
        print(err)


if __name__ == "__main__":
    build_frontend()
