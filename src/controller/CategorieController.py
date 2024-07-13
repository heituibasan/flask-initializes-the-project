#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/28 下午7:32
# @FileSpec : 分类接口

from flask import Blueprint, request, jsonify
from src.handler.decorators import check_content_type_json, validate_req_sign
from src.handler.message import CategorieErrorMessage, ErrorMessage
from src.utils.response import Response
from src.service import CategorieService

categories = Blueprint("categories", __name__, url_prefix="/api/categories")


@categories.route("/", methods=["POST"])
@check_content_type_json
@validate_req_sign
def get_categories():
    """
    获取所有分类

    :return: Response, 包含所有分类的响应
    """
    return jsonify(CategorieService.get_categories())


@categories.route("/get_categorie", methods=["POST"])
@check_content_type_json
@validate_req_sign
def get_categorie():
    """
    获取指定ID的分类

    :return: Response, 包含指定分类的响应
    """
    data = request.get_json()
    if not data.get("id"):
        return jsonify(Response.error(ErrorMessage.ID_REQUIRED))
    categorie_id = int(data.get("id").strip())
    return jsonify(CategorieService.get_categorie(categorie_id))


@categories.route("/create_categorie", methods=["POST"])
@check_content_type_json
@validate_req_sign
def create_categorie():
    """
    创建新的分类

    :return: Response, 创建分类的结果
    """
    data = request.get_json()
    if not data.get("content"):
        return jsonify(Response.error(CategorieErrorMessage.CATEGORIE_CONTENT_REQUIRED))
    if not data.get("author_id"):
        return jsonify(Response.error(ErrorMessage.AUTHOR_ID_REQUIRED))

    content = data.get("content").strip()
    author_id = int(data.get("author_id").strip())
    return jsonify(
        CategorieService.create_categorie(content=content, author_id=author_id)
    )


@categories.route("/set_categorie", methods=["POST"])
@check_content_type_json
@validate_req_sign
def set_categorie():
    """
    更新指定ID的分类

    :return: Response, 更新分类的结果
    """
    data = request.get_json()
    if not data.get("id"):
        return jsonify(Response.error(ErrorMessage.ID_REQUIRED))
    categorie_id = int(data.get("id").strip())
    content = None
    status = None
    if data.get("content"):
        content = data.get("content").strip()
    if data.get("status"):
        status = int(data.get("status").strip())

    return jsonify(
        CategorieService.set_categorie(
            categorie_id=categorie_id, content=content, status=status
        )
    )


@categories.route("/delete_categorie", methods=["POST"])
@check_content_type_json
@validate_req_sign
def delete_categorie():
    """
    删除指定ID的分类

    :return: Response, 删除分类的结果
    """
    data = request.get_json()
    if not data.get("id"):
        return jsonify(Response.error(ErrorMessage.ID_REQUIRED))
    categorie_id = int(data.get("id").strip())
    return jsonify(CategorieService.delete_categorie(categorie_id=categorie_id))
