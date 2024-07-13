#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/28 上午9:39
# @FileSpec : 标签接口

from flask import Blueprint, request, jsonify
from src.handler.decorators import check_content_type_json, validate_req_sign
from src.handler.message import TagErrorMessage, ErrorMessage
from src.utils.response import Response
from src.service import TagService

tags = Blueprint("tags", __name__, url_prefix="/api/tags")


@tags.route("/", methods=["POST"])
@check_content_type_json
@validate_req_sign
def get_tags():
    """
    获取所有标签

    :return: Response, 包含所有标签的响应
    """
    return jsonify(TagService.get_tags())


@tags.route("/get_tag", methods=["POST"])
@check_content_type_json
@validate_req_sign
def get_tag():
    """
    获取指定ID的标签

    :return: Response, 包含指定标签的响应
    """
    data = request.get_json()
    if not data.get("id"):
        return jsonify(Response.error(ErrorMessage.ID_REQUIRED))
    tag_id = int(data.get("id").strip())
    return jsonify(TagService.get_tag(tag_id))


@tags.route("/create_tag", methods=["POST"])
@check_content_type_json
@validate_req_sign
def create_tag():
    """
    创建新的标签

    :return: Response, 创建标签的结果
    """
    data = request.get_json()
    if not data.get("content"):
        return jsonify(
            Response.error(ErrorMessage.CONTENT_IS_NULL)
        )
    if not data.get("author_id"):
        return jsonify(Response.error(ErrorMessage.AUTHOR_ID_REQUIRED))

    content = data.get("content").strip()
    author_id = int(data.get("author_id").strip())
    return jsonify(TagService.create_tag(content=content, author_id=author_id))


@tags.route("/set_tag", methods=["POST"])
@check_content_type_json
@validate_req_sign
def set_tag():
    """
    更新指定ID的标签

    :return: Response, 更新标签的结果
    """
    data = request.get_json()
    if not data.get("id"):
        return jsonify(Response.error(ErrorMessage.ID_REQUIRED))
    tag_id = int(data.get("id").strip())
    content = None
    status = None
    if data.get("content"):
        content = data.get("content").strip()
    if data.get("status"):
        status = int(data.get("status").strip())

    return jsonify(
        TagService.set_tag(
            tag_id=tag_id, content=content, status=status
        )
    )


@tags.route("/delete_tag", methods=["POST"])
@check_content_type_json
@validate_req_sign
def delete_tag():
    """
    删除指定ID的标签

    :return: Response, 删除标签的结果
    """
    data = request.get_json()
    if not data.get("id"):
        return jsonify(Response.error(ErrorMessage.ID_REQUIRED))
    tag_id = int(data.get("id").strip())
    return jsonify(TagService.delete_tag(tag_id=tag_id))
