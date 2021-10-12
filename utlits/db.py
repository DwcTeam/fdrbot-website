from __future__ import annotations
import typing
from enum import Enum
from pymongo import MongoClient
from random import choice

mongo_url = "mongodb://localhost:27017"

db = MongoClient(mongo_url)
db_client = db["fa-azcrone"]
col_guilds = db_client["guilds"]
col_azkar = db_client["azker"]

print('`connect MongoDB database`')


class GuildUpdateType(Enum):
    prefix = "prefix"
    channel = "channel"
    time = "time"
    anti_spam = "anti_spam"
    embed = "embed"


class Guild(object):
    def __init__(self, guild_id: typing.Any):
        self._guild_id = int(guild_id)

    @property
    def info(self) -> dict:
        return col_guilds.find_one({"_id": self._guild_id})

    def update_where(self, module: GuildUpdateType, value) -> dict:
        col_guilds.update_one({"_id": self._guild_id}, {"$set": {module.value: value}})
        return self.info

    def insert(self) -> dict:
        if self.info:
            return {"msg": "This guild already exists"}
        data = {
            "_id": self._guild_id,
            "prefix": "!",
            "channel": None,
            "time": 3600,
            "anti_spam": False,
            "embed": False
        }
        col_guilds.insert_one(data)
        return self.info

class Azkar(object):
    @property
    def last_id(self) -> int:
        try:
            return col_azkar.find().sort("_id", -1).limit(1)[0].get("_id") + 1
        except:
            return 1

    def add(self, msg: str):
        col_azkar.insert_one({"_id": self.last_id, "msg": msg})

    @staticmethod
    def remove(_id: int):
        col_azkar.delete_one({"_id": _id})

    @staticmethod
    def edit(_id: int, new_msg: str):
        col_azkar.update_one({"_id": _id}, {"$set": {"msg": new_msg}})

    @property
    def random(self) -> dict:
        return choice([i for i in col_azkar.find()])

