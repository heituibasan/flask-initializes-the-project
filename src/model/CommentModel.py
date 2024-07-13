#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/29 下午6:23
# @FileSpec : 评论表模型

from datetime import datetime
from src.extensions import db


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.String(255), nullable=True, comment="该评论所属用户ID")
    article_id = db.Column(db.String(255), nullable=True, comment="该评论所属文章的ID")
    father_id = db.Column(db.String(255), nullable=True, comment="该评论所属父级的ID")
    title = db.Column(db.String(255), nullable=True, comment="评论标题")
    content = db.Column(db.Text, nullable=True, comment="评论内容")
    like_num = db.Column(db.Integer, default=0, comment="评论点赞数")
    comment_num = db.Column(db.Integer, default=0, comment="评论数量")
    create_time = db.Column(db.TIMESTAMP, default=datetime.utcnow, comment="评论创建时间")
    create_ip = db.Column(db.String(255), nullable=True, comment="评论创建时的IP地址")
    status = db.Column(
        db.Integer,
        default=0,
        comment="评论状态，一个泛型，0：发布，1：隐藏，2：删除（不显示到前端），默认0",
    )
    auditing_status = db.Column(
        db.Integer,
        default=0,
        comment="审核状态，一个泛型，0：未审核，1：已审核，默认0",
    )

    def __repr__(self):
        return (
            f"<Comment(id={self.id}, author_id='{self.author_id}', article_id='{self.article_id}', "
            f"father_id='{self.father_id}', title='{self.title}', content='{self.content}', "
            f"like_num={self.like_num}, comment_num={self.comment_num}, create_time={self.create_time}, "
            f"create_ip='{self.create_ip}', status={self.status}, auditing_status={self.auditing_status})>"
        )

    @classmethod
    def create(cls, **kwargs) -> bool:
        """
        插入数据到数据库当中

        :param kwargs:
        :return: Comment创建的实例
        """

        kwargs["create_time"] = datetime.now()
        comment = instance = cls(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return comment

    @classmethod
    def get_by_id(cls, comment_id):
        """
        根据ID查询评论

        :param comment_id: int, 评论ID
        :return: Comment创建的实例 or None, 查询到的实例或None
        """
        return cls.query.get(comment_id)

    @classmethod
    def get_by_author_id(cls, author_id):
        """
        根据用户ID查询评论

        :param author_id: int, 作者ID
        :return: list, 查询到的实例列表
        """
        return cls.query.filter_by(author_id=author_id).all()

    @classmethod
    def get_by_article_id(cls, article_id):
        """
        根据文章ID查询评论

        :param article_id: int, 文章ID
        :return: list, 查询到的实例列表
        """
        return cls.query.filter_by(article_id=article_id).all()

    @classmethod
    def get_by_father_id(cls, father_id):
        """
        根据父级ID查询评论

        :param father_id: int, 父级ID
        :return: list, 查询到的实例列表
        """
        return cls.query.filter_by(father_id=father_id).all()

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
    def delete_by_id(cls, comment_id):
        """
        根据评论id删除内容

        :param comment_id: int, 评论ID
        :return: bool, 删除是否成功
        """
        comment = cls.query.get(comment_id)
        if comment:
            db.session.delete(comment)
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
        comments = cls.query.filter_by(author_id=author_id).all()
        if comments:
            for comment in comments:
                db.session.delete(comment)
            db.session.commit()
            return True
        return False

    @classmethod
    def delete_by_article_id(cls, article_id):
        """
        根据文章id删除内容

        :param article_id: int, 文章ID
        :return: bool, 删除是否成功
        """
        comments = cls.query.filter_by(article_id=article_id).all()
        if comments:
            for comment in comments:
                db.session.delete(comment)
            db.session.commit()
            return True
        return False

    @classmethod
    def delete_by_father_id(cls, father_id):
        """
        根据父级id删除内容

        :param father_id: int, 父级ID
        :return: bool, 删除是否成功
        """
        comments = cls.query.filter_by(father_id=father_id).all()
        if comments:
            for comment in comments:
                db.session.delete(comment)
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
            author_id=data.get("author_id"),
            article_id=data.get("article_id"),
            father_id=data.get("father_id"),
            title=data.get("title"),
            content=data.get("content"),
            like_num=data.get("like_num"),
            comment_num=data.get("comment_num"),
            create_time=data.get("create_time"),
            create_ip=data.get("create_ip"),
            status=data.get("status"),
            auditing_status=data.get("auditing_status"),
        )

    def to_dict(self):
        """
        将数据转换为字典类型
        :return:
        """
        return {
            "id": self.id,
            "author_id": self.author_id,
            "article_id": self.article_id,
            "father_id": self.father_id,
            "title": self.title,
            "content": self.content,
            "like_num": self.like_num,
            "comment_num": self.comment_num,
            "create_time": self.create_time,
            "create_ip": self.create_ip,
            "status": self.status,
            "auditing_status": self.auditing_status,
        }
