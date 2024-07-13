#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/7/4 下午3:42
# @FileSpec : 网站配置
import sys

sys.path.append(".")
from src.extensions import db  # 数据库对象，flask
from src.model.SettingModel import Setting
# 查询数据库获取数据库setting的内容
settings = Setting.query.all()
for setting in settings:
    print(f"Key: {setting.setting_key}, Value:")
