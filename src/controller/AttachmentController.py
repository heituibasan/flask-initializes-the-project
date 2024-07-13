#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/7/7 下午10:07
# @FileSpec : 附件路由


from flask import Blueprint, request, jsonify, send_file
from src.handler.decorators import check_content_type_json, validate_req_sign
from src.handler.message import AttachmentErrorMessage, ErrorMessage
from src.utils.response import Response
from src.service import AttachmentService
import os

attachments = Blueprint("attachments", __name__, url_prefix="/api/attachments")


@attachments.route("/", methods=["POST"])
@check_content_type_json
@validate_req_sign
def get_attachments():
    """
    获取所有附件的信息
    :return:
    """
    return AttachmentService.get_attachments()


@attachments.route("/get_attachment", methods=["POST"])
@check_content_type_json
@validate_req_sign
def get_attachment():
    """
    根据ID获取附件信息
    :return:
    """
    data = request.get_json()
    if not data.get("id"):
        return jsonify(Response.error(ErrorMessage.ID_REQUIRED))
    attachment_id = int(data.get("id").strip())
    return jsonify(AttachmentService.get_attachment(attachment_id=attachment_id))


# 上传文件
@attachments.route("/upload", methods=["POST"])
@validate_req_sign
def upload_attachment():
    """
    上传文件
    :return:
    """
    if 'file' not in request.files:
        return jsonify(Response.error(AttachmentErrorMessage.FILE_REQUIRED))
    file = request.files['file']
    return jsonify(AttachmentService.upload_attachment(file))


@attachments.route("/download/<int:attachment_id>", methods=["GET"])
@validate_req_sign
def download_attachment(attachment_id):
    """
    下载文件
    :param attachment_id: 附件ID
    :return:
    """
    file_path = AttachmentService.get_attachment_path(attachment_id)
    if not file_path or not os.path.exists(file_path):
        return jsonify(Response.error(AttachmentErrorMessage.ATTACHMENT_NOT_FOUND))
    return send_file(file_path, as_attachment=True)


@attachments.route("/preview/<int:attachment_id>", methods=["GET"])
@validate_req_sign
def preview_attachment(attachment_id):
    """
    预览文件
    :param attachment_id: 附件ID
    :return:
    """
    file_path = AttachmentService.get_attachment_path(attachment_id)
    if not file_path or not os.path.exists(file_path):
        return jsonify(Response.error(AttachmentErrorMessage.ATTACHMENT_NOT_FOUND))
    return send_file(file_path)


@attachments.route("/delete", methods=["POST"])
@check_content_type_json
@validate_req_sign
def delete_attachment():
    """
    删除文件
    :return:
    """
    data = request.get_json()
    if not data.get("id"):
        return jsonify(Response.error(ErrorMessage.ID_REQUIRED))
    attachment_id = int(data.get("id").strip())
    return jsonify(AttachmentService.delete_attachment(attachment_id=attachment_id))
