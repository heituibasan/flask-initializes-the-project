#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/29 下午6:23
# @FileSpec : 设置表模型

import time
from datetime import datetime
from src.extensions import db


class Setting(db.Model):
    __tablename__ = "settings"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    setting_key = db.Column(db.String(255), nullable=True,
                            comment="设置的键，唯一标识具体的设置项，设置前缀为sys/web分别是系统设置和网站设置")
    setting_value = db.Column(db.String(255), nullable=True, comment="设置的值，可以存储各种设置项的具体值")

    def __repr__(self):
        return (f"<Setting(id={self.id}, setting_key='{self.setting_key}', setting_value='{self.setting_value}'")

    @classmethod
    def create(cls, **kwargs) -> bool:
        """
        插入数据到数据库当中

        :param kwargs:
        :return: Setting创建的实例
        """

        setting = instance = cls(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return setting

    @classmethod
    def get_by_id(cls, tag_id):
        """
        根据ID查询标签

        :param tag_id: int, 标签ID
        :return: Tag创建的实例 or None, 查询到的实例或None
        """
        return cls.query.get(tag_id)

    @classmethod
    def get_all(cls):
        """
        获取所有的数据

        :return: list, 所有数据列表
        """
        return cls.query.all()

    def update(self, **kwargs):
        """
        修改数据

        :param kwargs:
        :return:
        """
        for key, value in kwargs.items():

            if value is not None:
                print(f"{key}: {value}")
                setattr(self, key, value)
        db.session.commit()

    def to_dict(self):
        """
        将用户对象转换为字典
        """
        return {
            "id": self.id,
            "setting_key": self.setting_key,
            "setting_value": self.setting_value,

        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            setting_key=data.get("setting_key"),
            setting_value=data.get("setting_value"),
        )
