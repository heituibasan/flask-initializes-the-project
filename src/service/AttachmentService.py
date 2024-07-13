#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/7/7 下午10:08
# @FileSpec : 附件服务类


from src.model import AttachmentModel
from src.utils.response import Response
import src.utils.tools as tools
from src.model.UserModel import User
from src.model.AttachmentModel import Attachment
from src.handler.message import AttachmentErrorMessage, ErrorMessage, SuccessMessage
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'path/to/upload/folder'  # 设置上传文件的路径
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}  # 允许的文件扩展名


def get_attachments():
    """
    获取所有附件的信息
    :return:
    """
    attachments = Attachment.get_all()
    return Response.success(message=SuccessMessage.REQUEST_SUCCESS, result=[item.to_dict() for item in attachments])


def get_attachment(attachment_id: int):
    """
    根据ID获取附件
    :param attachment_id: 附件ID
    :return:
    """
    attachment = Attachment.get_by_id(attachment_id)
    if attachment is None:
        return Response.error(AttachmentErrorMessage.ATTACHMENT_NOT_FOUND)
    return Response.success(message=SuccessMessage.REQUEST_SUCCESS, result=attachment.to_dict())


def allowed_file(filename):
    """
    检查文件是否允许上传
    :param filename: 文件名
    :return: bool
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_attachment(file):
    """
    上传文件
    :param file: 文件对象
    :return:
    """
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        attachment = Attachment.create(file_path=file_path, filename=filename)
        return Response.success(message=SuccessMessage.UPLOAD_SUCCESS, result=attachment.to_dict())
    return Response.error(AttachmentErrorMessage.FILE_NOT_ALLOWED)


def get_attachment_path(attachment_id: int):
    """
    获取附件文件路径
    :param attachment_id: 附件ID
    :return: 文件路径
    """
    attachment = Attachment.get_by_id(attachment_id)
    if attachment:
        return attachment.file_path
    return None


def delete_attachment(attachment_id: int):
    """
    删除附件
    :param attachment_id: 附件ID
    :return:
    """
    attachment = Attachment.get_by_id(attachment_id)
    if attachment is None:
        return Response.error(AttachmentErrorMessage.ATTACHMENT_NOT_FOUND)
    os.remove(attachment.file_path)
    attachment.delete()
    return Response.success(message=SuccessMessage.DELETE_SUCCESS)
