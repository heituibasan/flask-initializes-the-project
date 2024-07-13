#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/7/7 上午10:05
# @FileSpec :

from src.utils.response import Response
from src.model.UserModel import User
from src.model.LinkModel import Link
from src.handler.message import UserErrorMessage, SuccessMessage, LinkErrorMessage


def get_links():
    """
    获取所有链接信息
    :return:
    """
    links = Link.get_all()
    return Response.success(message=SuccessMessage.REQUEST_SUCCESS, result=[item.to_dict() for item in links])


def get_link(link_id: int):
    """
    根据链接ID查询链接
    :param link_id: 链接ID
    :return:
    """
    link = Link.get_by_id(link_id)
    if link is None:
        return Response.error(LinkErrorMessage.LINK_NOT_FOUND)
    return Response.success(message=SuccessMessage.REQUEST_SUCCESS, result=link.to_dict())


def create_link(title: str, content: str, author_id: int):
    """
    创建链接
    :param title: 标题
    :param content: 内容
    :param author_id: 作者ID
    :return:
    """
    # 检查作者是否存在与数据库
    if not User.get_by_id(author_id):
        return Response.error(message=UserErrorMessages.USER_NOT_FOUND)

    # 创建
    Link.create(title=title,
                content=content,
                author_id=author_id,
                status=0,
                )

    return Response.success(message=SuccessMessage.OPERATION_SUCCESS)


def set_link(link_id: int, title: str, content: str, status: int):
    """
    更新链接内容
    :param link_id: 链接ID
    :param title: 标题
    :param content: 内容
    :param status: 状态
    :return:
    """
    # 查询是否有该链接
    link = Link.get_by_id(link_id)
    if not link:
        return Response.error(message=LinkErrorMessage.LINK_NOT_FOUND)
        # 更新数据
    link.update(
        title=title,
        content=content,
        status=status,
    )

    return Response.success(message=SuccessMessage.OPERATION_SUCCESS)


def delete_link(link_id):
    """
    根据ID删除链接
    :param link_id: 链接ID
    :return:
    """
    # 查询是否有该链接
    if not Link.get_by_id(link_id):
        return Response.error(message=LinkErrorMessage.LINK_NOT_FOUND)
    # 删除数据
    Link.delete_by_id(link_id)
    return Response.success(message=SuccessMessage.OPERATION_SUCCESS)
