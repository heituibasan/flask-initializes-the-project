#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/29 上午11:13
# @FileSpec : 用户表模型

import time
from datetime import datetime
from src.extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(
        db.String(255), nullable=False, comment="用户在系统中展示的名称"
    )
    email = db.Column(
        db.String(255), nullable=False, unique=True, comment="用于用户登录的账户"
    )
    password = db.Column(
        db.String(255), nullable=False, comment="用户登录密码（存储加密过后的密码）"
    )
    code = db.Column(db.String(255), comment="用户注册时创建的验证码")
    avatar = db.Column(db.String(255), comment="用户头像，是一个url链接")
    phone = db.Column(db.Integer, comment="用户绑定电话，后期可用于发送信息")
    qq = db.Column(db.Integer(), comment="用户绑定QQ，后期可用于联系")
    role = db.Column(
        db.String(255), comment="用户角色，一个泛型，0：普通用户，1：游客，2：管理员"
    )
    create_time = db.Column(db.TIMESTAMP, comment="用户创建时的时间")
    last_login_time = db.Column(db.TIMESTAMP, comment="用户最后登录的时间")
    create_mac = db.Column(db.String(255), comment="用户创建时的MAC地址")
    create_ip = db.Column(db.String(255), comment="用户创建时的IP地址")
    last_login_ip = db.Column(db.String(255), comment="用户最后登录时的IP地址")
    address = db.Column(db.String(255), comment="用户具体居住地址")
    city = db.Column(db.String(255), comment="用户所属城市")
    status = db.Column(
        db.Integer,
        default=0,
        comment="用户状态，一个泛型，0：未激活，1：激活，2：删除，默认0",
    )

    def __repr__(self):
        return (
            f"<User(id={self.id}, username='{self.username}', email='{self.email}', "
            f"password='{self.password}', code='{self.code}', phone={self.phone}, qq='{self.qq}', "
            f"role='{self.role}', create_time={self.create_time}, last_login_time={self.last_login_time}, "
            f"create_mac='{self.create_mac}', create_ip='{self.create_ip}', last_login_ip='{self.last_login_ip}', "
            f"address='{self.address}', city='{self.city}', status={self.status})>"
        )

    @classmethod
    def create(cls, **kwargs) -> bool:
        """
        插入数据到数据库当中

        :param kwargs:
        :return: User创建的实例
        """

        kwargs["create_time"] = datetime.now()
        user = instance = cls(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return user

    @classmethod
    def get_by_id(cls, user_id):
        """
        根据用户ID查询用户

        :param user_id: int, 用户ID
        :return: User or None, 查询到的实例或None
        """
        return cls.query.get(user_id)

    @classmethod
    def get_by_email(cls, user_email):
        """
        根据用户邮箱查询用户

        :param user_email: int, 用户ID
        :return: User or None, 查询到的实例或None
        """
        return cls.query.filter_by(email=user_email).first()

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
    def delete(cls, user_id):
        """
        删除文章

        :param user_id: int, 用户ID
        :return: bool, 删除是否成功
        """
        user = cls.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False

    @classmethod
    def get_all(cls):
        """
        获取所有的数据

        :return: list, 所有数据列表
        """
        return cls.query.all()

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

    def to_dict(self):
        """
        将用户对象转换为字典
        """
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "code": self.code,
            "phone": self.phone,
            "qq": self.qq,
            "role": self.role,
            "create_time": self.create_time.isoformat() if self.create_time else None,
            "last_login_time": (
                self.last_login_time.isoformat() if self.last_login_time else None
            ),
            "create_mac": self.create_mac,
            "create_ip": self.create_ip,
            "last_login_ip": self.last_login_ip,
            "address": self.address,
            "city": self.city,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            username=data.get("username"),
            email=data.get("email"),
            password=data.get("password"),
            code=data.get("code"),
            phone=data.get("phone"),
            qq=data.get("qq"),
            role=data.get("role"),
            create_time=(
                datetime.fromisoformat(data.get("create_time"))
                if data.get("create_time")
                else None
            ),
            last_login_time=(
                datetime.fromisoformat(data.get("last_login_time"))
                if data.get("last_login_time")
                else None
            ),
            create_mac=data.get("create_mac"),
            create_ip=data.get("create_ip"),
            last_login_ip=data.get("last_login_ip"),
            address=data.get("address"),
            city=data.get("city"),
            status=data.get("status"),
        )
