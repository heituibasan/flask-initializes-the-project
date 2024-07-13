#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/30 下午5:10
# @FileSpec :


class SuccessMessage:
    """
    常用成功消息类
    """

    OPERATION_SUCCESS = "操作成功"
    REQUEST_SUCCESS = "请求成功"
    UPDATE_SUCCESS = "更新成功"
    ADD_SUCCESS = "新增成功"
    DELETION_SUCCESS = "删除成功"
    REGISTRATION_SUCCESS = "注册成功"
    LOGIN_SUCCESS = "登录成功"
    LOGOUT_SUCCESS = "注销成功"
    PASSWORD_RESET_SUCCESS = "密码重置成功"
    EMAIL_SENT_SUCCESS = "邮件发送成功"
    DATA_SAVE_SUCCESS = "数据保存成功"
    PROFILE_UPDATE_SUCCESS = "个人资料更新成功"
    UPLOAD_SUCCESS = "上传成功"
    DOWNLOAD_SUCCESS = "下载成功"
    PAYMENT_SUCCESS = "支付成功"
    SUBSCRIPTION_SUCCESS = "订阅成功"
    UNSUBSCRIBE_SUCCESS = "取消订阅成功"
    VERIFICATION_SUCCESS = "验证成功"
    AUTHORIZATION_SUCCESS = "授权成功"
    LIKE_SUCCESS = "点赞成功"
    UNLIKE_SUCCESS = "取消点赞成功"
    NOTIFICATION_SENT_SUCCESS = "通知发送成功"
    MESSAGE_SENT_SUCCESS = "消息发送成功"
    ACCOUNT_ACTIVATION_SUCCESS = "账户激活成功"
    DELETE_SUCCESS = "删除成功"


class ErrorMessage:
    """
    错误信息类
    """
    AUTHOR_ID_REQUIRED = "作者ID是必需的"
    INVALID_ID = "无效的ID"
    ID_REQUIRED = "ID是必需的"
    INVALID_REQ_SIGN = "无效请求签名"
    REGISTRATION_FAILED = "注册失败"
    LOGIN_FAILED = "登录失败"
    DATA_SAVE_FAILED = "数据保存失败"
    OPERATION_FAILED = "操作失败"
    PASSWORD_RESET_FAILED = "密码重置失败"
    LOGOUT_FAILED = "注销失败"
    UPDATE_FAILED = "更新失败"
    DELETION_FAILED = "删除失败"
    EMAIL_SEND_FAILED = "邮件发送失败"
    PROFILE_UPDATE_FAILED = "个人资料更新失败"
    SETTINGS_UPDATE_FAILED = "设置更新失败"
    UPLOAD_FAILED = "上传失败"
    DOWNLOAD_FAILED = "下载失败"
    PAYMENT_FAILED = "支付失败"
    SUBSCRIPTION_FAILED = "订阅失败"
    UNSUBSCRIBE_FAILED = "取消订阅失败"
    VERIFICATION_FAILED = "验证失败"
    REQUEST_FAILED = "请求失败"
    CONNECTION_FAILED = "连接失败"
    DISCONNECTION_FAILED = "断开连接失败"
    AUTHENTICATION_FAILED = "认证失败"
    AUTHORIZATION_FAILED = "授权失败"
    ITEM_ADD_FAILED = "项目添加失败"
    ITEM_REMOVE_FAILED = "项目移除失败"
    OPERATION_COMPLETED_FAILED = "操作完成失败"
    COMMENT_POST_FAILED = "评论发布失败"
    COMMENT_DELETE_FAILED = "评论删除失败"
    LIKE_FAILED = "点赞失败"
    UNLIKE_FAILED = "取消点赞失败"
    CONTENT_IS_NULL = "内容为空"


class UserErrorMessage:
    """
    用户错误信息类
    """

    USERNAME_INFO_REQUIRED = "用户信息不完整"
    INVALID_USERNAME_CONTENT = "无效的分类内容，不能包含特殊字符"
    USERNAME_REQUIRED = "用户名不能为空"
    EMAIL_REQUIRED = "电子邮件不能为空"
    CODE_REQUIRED = "验证码不能为空"
    PASSWORD_REQUIRED = "密码不能为空"
    INVALID_EMAIL_FORMAT = "电子邮件格式不正确"
    PASSWORD_TOO_SHORT = "密码长度不能少于6位"
    USER_ALREADY_EXISTS = "用户已存在"
    INVALID_CREDENTIALS = "用户名或密码错误"
    REQUEST_HEADER_ERROR = "请求头错误"
    USER_NOT_FOUND = "用户不存在"
    INVALID_PASSWORD = "密码错误"
    OLD_PASSWORD_REQUIRED = "需要提供旧密码"
    NEW_PASSWORD_REQUIRED = "需要提供新密码"
    INVALID_OLD_PASSWORD = "旧密码错误"
    PASSWORD_TOO_SIMPLE = "密码必须包含大写字母、小写字母、数字和特殊符号"
    PASSWORD_SAME_AS_OLD = "新密码不能与旧密码相同"
    INVALID_RESET_CODE = "验证码无效"
    USER_ID_REQUIRED = "用户ID不能为空"
    PHONE_NUMBER_INVALID = "电话号码格式有误，长度应为11位"


class CategorieErrorMessage:
    """
    分类错误信息类
    """

    CATEGORIE_NOT_FOUND = "分类未找到"
    CATEGORIE_ALREADY_EXISTS = "分类已存在"
    INVALID_CATEGORIE_CONTENT = "无效的分类内容，不能包含特殊字符"
    CATEGORIE_CREATION_FAILED = "分类创建失败"
    CATEGORIE_UPDATE_FAILED = "分类更新失败"
    CATEGORIE_DELETE_FAILED = "分类删除失败"
    CATEGORIE_STATUS_INVALID = "无效的分类状态"
    AUTHOR_ID_REQUIRED = "作者ID是必需的"
    CATEGORIE_STATUS_REQUIRED = "分类状态是必需的"
    CATEGORIE_CONTENT_REQUIRED = "分类内容是必需的"


class TagErrorMessage:
    """
    标签错误信息类
    """

    TAG_NOT_FOUND = "标签未找到"
    TAG_ALREADY_EXISTS = "标签已存在"
    INVALID_TAG_ID = "无效的标签ID"
    INVALID_TAG_CONTENT = "无效的标签内容，不能包含特殊字符"
    TAG_CREATE_FAILED = "标签创建失败"
    TAG_UPDATE_FAILED = "标签更新失败"
    TAG_DELETE_FAILED = "标签删除失败"
    TAG_STATUS_INVALID = "无效的标签状态"
    AUTHOR_ID_REQUIRED = "作者ID是必需的"
    TAG_STATUS_REQUIRED = "标签状态是必需的"
    TAG_ID_REQUIRED = "标签ID是必需的"
    TAG_CONTENT_REQUIRED = "标签内容是必需的"


class SettingErrorMessage:
    """
    设置错误信息类
    """
    SETTING_NOT_FOUND = "该设置项未找到"


class LinkErrorMessage:
    """
    链接错误信息类
    """
    TITLE_REQUIRED = "链接标题是必须的"
    LINK_NOT_FOUND = "链接未找到"


class AttachmentErrorMessage:
    """
    附件错误信息
    """
    ATTACHMENT_NOT_FOUND = "附件未找到"
    FILE_REQUIRED = "文件为空"
    FILE_NOT_ALLOWED = "文件类型不允许"
