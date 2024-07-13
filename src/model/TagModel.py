#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/29 下午6:23
# @FileSpec : 标签表模型

import time
from datetime import datetime
from src.extensions import db


class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(255), nullable=True, comment="标签内容")
    author_id = db.Column(
        db.Integer, nullable=True, comment="该标签创建者ID，可通过该ID查找到作者"
    )
    status = db.Column(
        db.Integer,
        default=0,
        comment="标签状态，一个泛型，0：发布，1：隐藏，2：删除（不显示到前端），默认0",
    )
    create_time = db.Column(
        db.TIMESTAMP, default=datetime.utcnow, comment="该标签创建时间"
    )

    def __repr__(self):
        return (
            f"<Tag(id={self.id}, content='{self.content}', author_id='{self.author_id}', "
            f"status={self.status}, create_time={self.create_time})>"
        )

    @classmethod
    def create(cls, **kwargs) -> bool:
        """
        插入数据到数据库当中

        :param kwargs:
        :return: Tag创建的实例
        """

        kwargs["create_time"] = datetime.now()
        tag = instance = cls(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return tag

    @classmethod
    def get_by_id(cls, tag_id):
        """
        根据ID查询标签

        :param tag_id: int, 标签ID
        :return: Tag创建的实例 or None, 查询到的实例或None
        """
        return cls.query.get(tag_id)

    @classmethod
    def get_by_author_id(cls, author_id):
        """
        根据用户ID查询标签

        :param author_id: int, 作者ID
        :return: Tag创建的实例 or None, 查询到的实例或None
        """
        return cls.query.get(author_id)

    @classmethod
    def get_by_content(cls, content):
        """
        根据标签的内容查询标签

        :param content: str, 标签内容
        :return: Tag创建的实例 or None, 查询到的实例或None
        """
        return cls.query.get(content)

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
                setattr(self, key, value)
        db.session.commit()

    @classmethod
    def delete_by_id(cls, tag_id):
        """
        根据标签id删除内容

        :param tag_id: int, 标签ID
        :return: bool, 删除是否成功
        """
        user = cls.query.get(tag_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False

    @classmethod
    def delete_by_content(cls, content):
        """
        根据标签内容删除内容

        :param content: str,标签内容
        :return: bool, 删除是否成功
        """
        user = cls.query.get(content)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False

    @classmethod
    def delete_by_author_id(cls, author_id):
        """
        根据作者id删除内容

        :param author_id: int, 作者ID
        :return: bool, 删除是否成功
        """
        user = cls.query.get(author_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False

    @classmethod
    def paginate_all(cls, page=None, per_page=None):
        """
        分页查询所有数据

        :param page: int or None, 当前页码，None表示不分页，返回所有数据
        :param per_page: int or None, 每页显示数量，None表示不分页，返回所有数据
        :return: Pagination or list, 分页查询结果对象或所有数据列表
        """
        if page is None or per_page is None:
            return cls.query.all()
        return cls.query.paginate(page, per_page, error_out=False)

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            content=data.get("content"),
            author_id=data.get("author_id"),
            status=data.get("status"),
            create_time=data.get("create_time"),
        )

    def to_dict(self):
        """
        将数据转换为字典类型
        :return:
        """
        return {
            "id": self.id,
            "content": self.content,
            "author_id": self.author_id,
            "status": self.status,
            "create_time": self.create_time,
        }
