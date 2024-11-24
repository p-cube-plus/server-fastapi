import configparser
from functools import lru_cache

from pydantic_settings import BaseSettings

config = configparser.ConfigParser()
config.read("config/config.ini")


class Settings(BaseSettings):
    def __getitem__(self, key):
        return config[key]


@lru_cache
def get_settings():
    return Settings()
