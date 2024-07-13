#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/28 上午9:50
# @FileSpec : 标签服务接口

from src.utils.response import Response
import src.utils.tools as tools
from src.model.UserModel import User
from src.model.TagModel import Tag
from src.handler.message import TagErrorMessage, UserErrorMessage, SuccessMessage


def get_tags():
    """
    获取所有标签

    :return: Response, 查询的响应结果
    """
    tags = Tag.get_all()
    return Response.success(message=SuccessMessage.REQUEST_SUCCESS, result=[item.to_dict() for item in tags])


def get_tag(tag_id: int):
    """
    根据ID获取标签

    :param tag_id: int, 标签ID
    :return: Response, 查询的响应结果
    """
    tag = Tag.get_by_id(tag_id)
    if not tag:
        return Response.error(message=TagErrorMessages.TAG_NOT_FOUND)
    return Response.success(message=SuccessMessage.REQUEST_SUCCESS, result=tag.to_dict())


def create_tag(content: str, author_id: int):
    """
    创建标签

    :param content: str, 标签内容
    :param author_id: int, 作者ID
    :return: Response, 创建的响应结果
    """
    # 检查标签文本是否包含特殊字符
    if tools.contains_special_characters(content=content):
        return Response.error(message=TagErrorMessages.INVALID_TAG_CONTENT)

    # 检查作者是否存在与数据库
    if not User.get_by_id(author_id):
        return Response.error(message=UserErrorMessages.USER_NOT_FOUND)

    # 创建标签
    Tag.create(
        content=content,
        author_id=author_id,
        status=0,
    )
    return Response.success(message=SuccessMessage.OPERATION_SUCCESS)


def set_tag(tag_id: int, content: str, status: int):
    """
    更新标签

    :param tag_id: int, 标签ID
    :param content: str, 标签内容
    :param status: int, 状态
    :return: Response, 更新的响应结果
    """
    # 检查标签文本是否包含特殊字符
    if tools.contains_special_characters(content=content):
        return Response.error(message=TagErrorMessages.INVALID_TAG_CONTENT)

    # 查询是否有该标签
    tag = Tag.get_by_id(tag_id)
    if not tag:
        return Response.error(message=TagErrorMessages.TAG_NOT_FOUND)

    # 更新数据
    tag.update(
        tag_id=tag_id,
        content=content,
        status=status,
    )

    return Response.success(message=SuccessMessage.OPERATION_SUCCESS)


def delete_tag(tag_id: int):
    """
    根据ID删除标签

    :param tag_id: int, 标签ID
    :return: Response, 删除的响应结果
    """
    #  查询是否有该标签
    if not Tag.get_by_id(tag_id):
        return Response.error(message=TagErrorMessages.TAG_NOT_FOUND)

    # 删除数据
    Tag.delete_by_id(tag_id=tag_id)

    return Response.success(message=SuccessMessage.OPERATION_SUCCESS)
