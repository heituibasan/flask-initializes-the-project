#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/28 下午9:24
# @FileSpec : 系统配置
import sys
import configparser
import os

sys.path.append(".")


class Config:
    """
    配置类，用于全局文件配置
    """

    current_dir = os.path.dirname(os.path.abspath(__file__))
    CONFIG_FILE_PATH = os.getenv(
        "CONFIG_FILE_PATH", os.path.join(current_dir, "../../config.ini")
    )
    config = configparser.ConfigParser()

    @classmethod
    def load_config(cls):
        if not cls.config.read(cls.CONFIG_FILE_PATH):
            raise FileNotFoundError(f"配置文件 {cls.CONFIG_FILE_PATH} 未找到")
        # TODO MySQL数据库配置信息
        cls.MYSQL_HOST = cls.config.get("DATABASE", "MYSQL_HOST", fallback="localhost")
        cls.MYSQL_DB = cls.config.get("DATABASE", "MYSQL_DB", fallback="default_db")
        cls.MYSQL_USER = cls.config.get("DATABASE", "MYSQL_USER", fallback="root")
        cls.MYSQL_PASSWORD = cls.config.get("DATABASE", "MYSQL_PASSWORD", fallback="")
        cls.MYSQL_PORT = int(cls.config.getint("DATABASE", "MYSQL_PORT", fallback=3306))

        # TODO Redis配置信息
        cls.REDIS_HOST = cls.config.get(
            "DATABASE", "REDIS_HOST", fallback="redis://localhost:6379/0"
        )
        cls.SERVICE_HOST = cls.config.get("SERVICE", "SERVICE_HOST", fallback="0.0.0.0")
        cls.SERVICE_PORT = int(
            cls.config.getint("SERVICE", "SERVICE_PORT", fallback=8000)
        )

        # TODO 文件最大上传大小（KB）
        cls.MAX_CONTENT_LENGTH = int(
            cls.config.getint(
                "SETTING", "MAX_CONTENT_LENGTH", fallback=16 * 1024 * 1024
            )
        )

        # TODO 加密盐
        cls.ENCRYPT_SALT = cls.config.get(
            "SETTING", "ENCRYPT_SALT", fallback="5z0alfcu5v0x85mu"
        )

        # TODO 请求API数据时的密钥
        cls.REQ_SIGN = cls.config.get(
            "SETTING", "REQ_SIGN", fallback="5z0alfcu5v0x85mu"
        )

        # TODO 七牛云空间设置
        cls.QINIU_ACCESS_KEY = os.getenv("QINIU_ACCESS_KEY", "your_access_key")
        cls.QINIU_SECRET_KEY = os.getenv("QINIU_SECRET_KEY", "your_secret_key")
        cls.bucket_name = cls.config.get(
            "QINIU", "bucket_name", fallback="default_bucket"
        )

        # TODO 邮件配置
        cls.SMTP_SERVER = cls.config.get("EMAIL", "SMTP_SERVER", fallback="")
        cls.SMTP_PORT = int(cls.config.getint("EMAIL", "SMTP_PORT", fallback=587))
        cls.SMTP_USERNAME = cls.config.get("EMAIL", "SMTP_USERNAME", fallback="")
        cls.SMTP_PASSWORD = cls.config.get("EMAIL", "SMTP_PASSWORD", fallback="")

        # TODO 密码重置配置
        cls.PASSWORD_RESET_SECRET_KEY = cls.config.get(
            "SETTING",
            "PASSWORD_RESET_SECRET_KEY",
            fallback="d158956447d79eb27061a1bec42c94265d7fe52dd6e1a81d",
        )
        cls.PASSWORD_RESET_SECURITY_PASSWORD_SALT = cls.config.get(
            "SETTING",
            "PASSWORD_RESET_SECURITY_PASSWORD_SALT",
            fallback="d2a28cc709d9a943e9d684b3005e6527d723fc78a7630429",
        )


Config.load_config()
