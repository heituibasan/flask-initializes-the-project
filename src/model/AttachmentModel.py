#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/29 下午6:23
# @FileSpec : 附件表模型

from datetime import datetime
from src.extensions import db


class Attachment(db.Model):
    __tablename__ = "attachments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.String(255), nullable=True, comment="附件上传者ID")
    network_url = db.Column(db.String(255), nullable=True, comment="外部访问的URL地址")
    local_url = db.Column(db.String(255), nullable=True, comment="存储在本地的地址")
    preview_url = db.Column(db.String(255), nullable=True, comment="文件在外部预览地址")
    size = db.Column(db.Integer, nullable=True, comment="附件文件大小，单位KB")
    status = db.Column(
        db.Integer,
        default=0,
        comment="附件状态，一个泛型，0：发布，1：隐藏，2：删除（不显示到前端），默认0",
    )
    create_time = db.Column(
        db.TIMESTAMP, default=datetime.utcnow, comment="附件上传时间"
    )
    create_ip = db.Column(db.String(255), nullable=True, comment="附件上传者IP地址")

    def __repr__(self):
        return (
            f"<Attachment(id={self.id}, author_id='{self.author_id}', network_url='{self.network_url}', "
            f"local_url='{self.local_url}', preview_url='{self.preview_url}', size={self.size}, "
            f"status={self.status}, create_time={self.create_time}, create_ip='{self.create_ip}')>"
        )

    @classmethod
    def create(cls, **kwargs) -> bool:
        """
        插入数据到数据库当中

        :param kwargs:
        :return: Attachment创建的实例
        """

        kwargs["create_time"] = datetime.now()
        attachment = instance = cls(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return attachment

    @classmethod
    def get_by_id(cls, attachment_id):
        """
        根据ID查询附件

        :param attachment_id: int, 附件ID
        :return: Attachment创建的实例 or None, 查询到的实例或None
        """
        return cls.query.get(attachment_id)

    @classmethod
    def get_by_author_id(cls, author_id):
        """
        根据用户ID查询附件

        :param author_id: int, 作者ID
        :return: list, 查询到的实例列表
        """
        return cls.query.filter_by(author_id=author_id).all()

    @classmethod
    def get_by_network_url(cls, network_url):
        """
        根据外部访问的URL地址查询附件

        :param network_url: str, 外部访问的URL地址
        :return: list, 查询到的实例列表
        """
        return cls.query.filter_by(network_url=network_url).all()

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
    def delete_by_id(cls, attachment_id):
        """
        根据附件id删除内容

        :param attachment_id: int, 附件ID
        :return: bool, 删除是否成功
        """
        attachment = cls.query.get(attachment_id)
        if attachment:
            db.session.delete(attachment)
            db.session.commit()
            return True
        return False

    @classmethod
    def delete_by_network_url(cls, network_url):
        """
        根据外部访问的URL地址删除内容

        :param network_url: str, 外部访问的URL地址
        :return: bool, 删除是否成功
        """
        attachments = cls.query.filter_by(network_url=network_url).all()
        if attachments:
            for attachment in attachments:
                db.session.delete(attachment)
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
        attachments = cls.query.filter_by(author_id=author_id).all()
        if attachments:
            for attachment in attachments:
                db.session.delete(attachment)
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
            network_url=data.get("network_url"),
            local_url=data.get("local_url"),
            preview_url=data.get("preview_url"),
            size=data.get("size"),
            status=data.get("status"),
            create_time=data.get("create_time"),
            create_ip=data.get("create_ip"),
        )

    def to_dict(self):
        """
        将数据转换为字典类型
        :return:
        """
        return {
            "id": self.id,
            "author_id": self.author_id,
            "network_url": self.network_url,
            "local_url": self.local_url,
            "preview_url": self.preview_url,
            "size": self.size,
            "status": self.status,
            "create_time": self.create_time,
            "create_ip": self.create_ip,
        }
