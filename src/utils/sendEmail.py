#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/30 下午5:04
# @FileSpec : 邮件发送模块

import sys

sys.path.append(".")
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Template
from src.config.config import Config as config


def read_html_template(file_path: str) -> str:
    """
    读取HTML模板文件内容

    :param file_path: str, HTML模板文件路径
    :return: str, HTML模板文件内容
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        template_content = file.read()
    return template_content


def render_html_template(template_content: str, context: dict) -> str:
    """
    填充HTML模板中的占位符

    :param template_content: str, HTML模板内容
    :param context: dict, 填充HTML模板的上下文数据
    :return: str, 渲染后的HTML内容
    """
    template = Template(template_content)
    return template.render(context)


def send_email(subject: str, to_email: str, html_content: str) -> None:
    """
    发送HTML邮件

    :param subject: str, 邮件主题
    :param to_email: str, 收件人邮箱
    :param html_content: str, HTML格式的邮件内容
    :return: None
    """
    smtp_server = config.SMTP_SERVER
    smtp_port = config.SMTP_PORT
    smtp_username = config.SMTP_USERNAME
    smtp_password = config.SMTP_PASSWORD

    from_email = config.SMTP_USERNAME  # 发件人邮箱
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    mime_text = MIMEText(html_content, 'html')
    msg.attach(mime_text)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())


if __name__ == "__main__":
    # HTML模板文件路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_template_path = os.path.join(current_dir, "../../files/assets/email/UserTemplate/register.html")

    # 填充占位符的内容
    context = {
        'text': '这是替换后的内容',
        'username': '张三',
        'date': '2024-06-30'
    }

    # 读取并填充HTML模板
    template_content = read_html_template(html_template_path)
    html_content = render_html_template(template_content, context)

    # 邮件配置信息
    subject = '这是邮件的主题'
    to_email = 'm18212153903@163.com'

    # 发送邮件
    send_email(subject, to_email, html_content)
