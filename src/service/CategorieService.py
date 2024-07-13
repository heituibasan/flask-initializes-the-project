#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/28 下午7:40
# @FileSpec : 分类服务接口


from src.utils.response import Response
import src.utils.tools as tools
from src.model.UserModel import User
from src.model.CategorieModel import Categorie
from src.handler.message import CategorieErrorMessage, UserErrorMessage, SuccessMessage


def get_categories():
    """
    获取所有分类

    :return: Response, 查询的响应结果
    """
    categories = Categorie.get_all()
    return Response.success(message=SuccessMessage.REQUEST_SUCCESS, result=[item.to_dict() for item in categories])


def get_categorie(categorie_id: int):
    """
    根据ID获取分类

    :param categorie_id: int, 分类ID
    :return: Response, 查询的响应结果
    """
    categorie = Categorie.get_by_id(categorie_id)
    if not categorie:
        return Response.error(message=CategorieErrorMessages.CATEGORIE_NOT_FOUND)
    return Response.success(message=SuccessMessage.REQUEST_SUCCESS, result=categorie.to_dict())


def create_categorie(content: str, author_id: int):
    """
    创建分类

    :param content: str, 分类内容
    :param author_id: int, 作者ID
    :return: Response, 创建的响应结果
    """
    # 检查分类文本是否包含特殊字符
    if tools.contains_special_characters(content=content):
        return Response.error(message=CategorieErrorMessages.INVALID_CATEGORIE_CONTENT)

    # 检查作者是否存在与数据库
    if not User.get_by_id(author_id):
        return Response.error(message=UserErrorMessages.USER_NOT_FOUND)

    # 创建分类
    Categorie.create(
        content=content,
        author_id=author_id,
        status=0,
    )
    return Response.success(message=SuccessMessage.OPERATION_SUCCESS)


def set_categorie(categorie_id: int, content: str, status: int):
    """
    更新分类

    :param categorie_id: int, 分类ID
    :param content: str, 分类内容
    :param status: int, 状态
    :return: Response, 更新的响应结果
    """
    # 检查分类文本是否包含特殊字符
    if tools.contains_special_characters(content=content):
        return Response.error(message=CategorieErrorMessages.INVALID_CATEGORIE_CONTENT)

    # 查询是否有该分类
    categorie = Categorie.get_by_id(categorie_id)
    if not categorie:
        return Response.error(message=CategorieErrorMessages.CATEGORIE_NOT_FOUND)

    # 更新数据
    categorie.update(
        content=content,
        status=status,
    )

    return Response.success(message=SuccessMessage.OPERATION_SUCCESS)


def delete_categorie(categorie_id: int):
    """
    根据ID删除分类

    :param categorie_id: int, 分类ID
    :return: Response, 删除的响应结果
    """
    #  查询是否有该分类
    if not Categorie.get_by_id(categorie_id):
        return Response.error(message=CategorieErrorMessages.CATEGORIE_NOT_FOUND)

    # 删除数据
    Categorie.delete_by_id(categorie_id=categorie_id)

    return Response.success(message=SuccessMessage.OPERATION_SUCCESS)
