#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : 黑腿欧巴桑
# @Time     : 2024/6/30 下午3:34
# @FileSpec : Redis缓存
import sys
import json

sys.path.append(".")
from src.extensions import redis, db
from src.model import ArticleModel, AttachmentModel, CategorieModel, CommentModel, LinkModel, SettingModel, TagModel, \
    UserModel


class Cache:
    def __init__(self):
        self.model_mapping = {
            UserModel.User.__tablename__: UserModel.User,
            ArticleModel.Article.__tablename__: ArticleModel.Article,
        }
        pass

    def __get_cache_key(self, tablename: str, record_id: int = None):
        if record_id:
            return f"{tablename}:{record_id}"
        return f"{tablename}_ids"

    def __get_ids_list_key(self, tablename: str):
        return f"{tablename}_ids"

    def add_to_cache(self, tablename: str, record):
        """
        插入缓存数据到Redis
        :param tablename:
        :param record:
        :return:
        """
        # 获取该条数据对应的key
        record_id = record.get("id")
        key = self.__get_cache_key(tablename=tablename, record_id=record_id)

        # 插入到Redis
        redis.set(key, json.dumps(record))

        # 获取数据对应的ID列表
        ids_list = self.__get_ids_list_key(tablename=tablename)
        # 将ID插入该列表记录插入的key
        redis.rpush(ids_list, record_id)

        return True

    def get_from_cache(self, tablename: str, record_id: int) -> None | dict:
        """
        获取Redis缓存当中的数据
        :param tablename: 数据库表名
        :param record_id: 记录值id
        :return: 缓存当中的数据，如果没有返回None
        """
        key = self.__get_cache_key(tablename=tablename, record_id=record_id)
        cached_record = redis.get(key)

        # redis当中存在数据
        if cached_record:
            return json.loads(cached_record.decode("utf-8"))

        # 如果缓存没有，从数据库查询并插入
        if not self.model_mapping:
            raise ValueError(f"没有名为 {tablename} 的模型类")
        record = (
            self.model_mapping.get(tablename.lower()).get_by_id(record_id).to_dict()
        )

        if record:
            self.add_to_cache(tablename=tablename, record=record)
            return record
        return None

    def remove_from_cache(self, tablename: str, record_id: int):
        """
        从Redis缓存当中删除数据
        :param tablename: 数据库表名
        :param record_id: 记录值id
        :return: 操作成功 True
        """
        key = self.__get_cache_key(tablename=tablename, record_id=record_id)
        redis.delete(key)

        ids_list = self.__get_ids_list_key(tablename=tablename)
        redis.lrem(ids_list, 0, record_id)

        return True

    def update_cache(self, tablename: str, record):
        """
        更新Redis缓存当中的数据
        :param tablename: 数据库表名
        :param record: 需要更新的数据
        :return: 操作成功 True；操作失败 False
        """
        record_id = record.get("id")
        key = self.__get_cache_key(tablename=tablename, record_id=record_id)

        if redis.exists(key):
            redis.set(key, json.dumps(record))
            return True
        return False

    def get_all_from_cache(self, tablename: str):
        """
        从Redis缓存当中获取所有数据
        :param tablename: 数据库表名
        :return: 缓存当中的所有数据
        """
        ids_list = self.__get_ids_list_key(tablename=tablename)
        record_ids = redis.lrange(ids_list, 0, -1)
        records = []

        # 根据ids获取所有的数据
        for record_id in record_ids:
            cached_record = self.get_from_cache(
                tablename=tablename, record_id=int(record_id)
            )
            if cached_record:
                records.append(cached_record)
        # 如果缓存为空，从数据库获取所有数据并添加到缓存
        if not records:
            records = db.session.query(eval(tablename.capitalize())).all()
            for record in records:
                self.add_to_cache(tablename=tablename, record=record)
            return [str(record) for record in records]
        return records

    def clear_all_cache(self):
        """
        删除Redis当中的所有缓存数据
        :return: 操作成功 True
        """
        keys = redis.keys("*")
        if keys:
            redis.delete(*keys)
        return True
