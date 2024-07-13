#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/29 下午6:23
# @FileSpec : 链接表模型

from datetime import datetime
from src.extensions import db


class Link(db.Model):
    __tablename__ = "links"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=True, comment="链接标题")
    content = db.Column(db.Text, nullable=True, comment="链接内容")
    author_id = db.Column(
        db.Integer, nullable=True, comment="该链接创建者ID，可通过该ID查找到作者"
    )
    status = db.Column(
        db.Integer,
        default=0,
        comment="链接状态，一个泛型，0：发布，1：隐藏，2：删除（不显示到前端），默认0",
    )
    create_time = db.Column(
        db.TIMESTAMP, default=datetime.utcnow, comment="链接创建时间"
    )

    def __repr__(self):
        return (
            f"<Link(id={self.id}, title='{self.title}', content='{self.content}', "
            f"author_id='{self.author_id}', status={self.status}, create_time={self.create_time})>"
        )

    @classmethod
    def create(cls, **kwargs) -> bool:
        """
        插入数据到数据库当中

        :param kwargs:
        :return: Link创建的实例
        """

        kwargs["create_time"] = datetime.now()
        link = instance = cls(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return link

    @classmethod
    def get_by_id(cls, link_id):
        """
        根据ID查询链接

        :param link_id: int, 链接ID
        :return: Link创建的实例 or None, 查询到的实例或None
        """
        return cls.query.get(link_id)

    @classmethod
    def get_by_author_id(cls, author_id):
        """
        根据用户ID查询链接

        :param author_id: int, 作者ID
        :return: list, 查询到的实例列表
        """
        return cls.query.filter_by(author_id=author_id).all()

    @classmethod
    def get_by_title(cls, title):
        """
        根据链接的标题查询链接

        :param title: str, 链接标题
        :return: list, 查询到的实例列表
        """
        return cls.query.filter_by(title=title).all()

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
    def delete_by_id(cls, link_id):
        """
        根据链接id删除内容

        :param link_id: int, 链接ID
        :return: bool, 删除是否成功
        """
        link = cls.query.get(link_id)
        if link:
            db.session.delete(link)
            db.session.commit()
            return True
        return False

    @classmethod
    def delete_by_title(cls, title):
        """
        根据链接标题删除内容

        :param title: str, 链接标题
        :return: bool, 删除是否成功
        """
        links = cls.query.filter_by(title=title).all()
        if links:
            for link in links:
                db.session.delete(link)
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
        links = cls.query.filter_by(author_id=author_id).all()
        if links:
            for link in links:
                db.session.delete(link)
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
            title=data.get("title"),
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
            "title": self.title,
            "content": self.content,
            "author_id": self.author_id,
            "status": self.status,
            "create_time": self.create_time,
        }
