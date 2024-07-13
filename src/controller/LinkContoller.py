#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/7/7 上午10:04
# @FileSpec : 链接接口

from flask import Blueprint, request, jsonify
from src.handler.decorators import check_content_type_json, validate_req_sign
from src.handler.message import ErrorMessage, LinkErrorMessage

from src.utils.response import Response
from src.service import LinkService

links = Blueprint("setting", __name__, url_prefix="/api/links")


@links.route("/", methods=["POST"])
@check_content_type_json
@validate_req_sign
def get_links():
    """
    获取所有链接
    :return:
    """
    return jsonify(LinkService.get_links())


@links.route("/get_link", methods=["POST"])
def get_link():
    """
    根据链接ID查询链接
    :return:
    """
    data = request.get_json()
    if not data.get("id"):
        return Response.error(message=ErrorMessage.ID_REQUIRED)
    link_id = int(data.get("id").strip())
    return jsonify(LinkService.get_link(link_id=link_id))


@links.route("create_link", methods=["POST"])
@check_content_type_json
@validate_req_sign
def create_link():
    """
    创建链接
    :return:
    """
    data = request.get_json()
    if not data.get("title"):
        return jsonify(Response.error(LinkErrorMessage.TITLE_REQUIRED))
    if not data.get("content"):
        return jsonify(Response.error(ErrorMessage.CONTENT_IS_NULL))
    if not data.get("author_id"):
        return jsonify(Response.error(ErrorMessage.AUTHOR_ID_REQUIRED))
    title = data.get("title").strip()
    content = data.get("content").strip()
    author_id = int(data.get("author_id").strip())
    return jsonify(LinkService.create_link(title=title, content=content, author_id=author_id))


@links.route("/set_link", methods=["POST"])
@check_content_type_json
@validate_req_sign
def set_link():
    """
    根据ID更改链接数据
    :return:
    """
    data = request.get_json()
    if not data.get("id"):
        return jsonify(Response.error(ErrorMessage.ID_REQUIRED))
    link_id = int(data.get("id").strip())
    title = None
    content = None
    status = None
    if data.get("title"):
        title = data.get("title").strip()
    if data.get("content"):
        content = data.get("content").strip()
    if data.get("status"):
        status = int(data.get("status").strip())

    return jsonify(
        LinkService.set_link(
            link_id=link_id, title=title, content=content, status=status
        )
    )


@links.route("/delete_link", methods=["POST"])
@check_content_type_json
@validate_req_sign
def delete_link():
    """
    删除链接
    :return:
    """
    data = request.get_json()
    if not data.get("id"):
        return jsonify(Response.error(ErrorMessage.ID_REQUIRED))
    link_id = int(data.get("id").strip())
    return jsonify(LinkService.delete_link(link_id=link_id))
