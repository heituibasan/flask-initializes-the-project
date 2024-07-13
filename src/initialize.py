#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/28 下午9:36
# @FileSpec : 初始化flask应用

import os

from flask import Flask
from flask_cors import CORS

import build
from src.config.config import Config as config
from src.extensions import db, redis
from src.utils import logger
from .controller import CategorieController
from .controller import ErrorController
from .controller import SettingController
from .controller import TagController
from .controller import UserController
from .controller import LinkContoller

logger = logger.get_logger(__name__)


def build_frontend():
    # 检查是否已经构建过前端项目
    if not os.getenv('FRONTEND_BUILT'):
        build.build_frontend()
        os.environ['FRONTEND_BUILT'] = 'True'  # 设置环境变量
        logger.info("构建完成！")


def create_app():
    #  构建vue前端代码
    # build_frontend()

    # 配置Flask
    current_dir = os.path.dirname(os.path.abspath(__file__))
    templates_path = os.path.join(current_dir, "../static/")
    static_path = os.path.join(current_dir, "../static/assets")
    app = Flask(__name__, template_folder=templates_path, static_folder=static_path)
    # CORS(app, resources={r"/api/*": {"origins": "*"}})
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['CORS_PROTOCOL'] = 'http'
    app.config['CORS_ORIGIN'] = '*'
    app.config['CORS_ALLOWED_ORIGIN'] = '*'
    app.config['CORS_PREFERRED_URL_SCHEME'] = 'https'

    #  SQLALCHEMY_DATABASE_URI 配置
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = f'mysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_HOST}:{config.MYSQL_PORT}/{config.MYSQL_DB}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    #  Redis 配置
    app.config['REDIS_URL'] = config.REDIS_HOST
    redis.init_app(app)

    #  注册蓝图
    app.register_blueprint(ErrorController.error)
    app.register_blueprint(UserController.users)
    app.register_blueprint(CategorieController.categories)
    app.register_blueprint(TagController.tags)
    app.register_blueprint(SettingController.settings)
    app.register_blueprint(LinkContoller.links)
    return app


def __initialize():
    """
    初始化
    1、下载项目依赖
    2、打包前端项目
    3、创建数据库
    4、插入数据表

    :return:
    """
