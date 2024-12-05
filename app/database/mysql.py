from app.core.config import get_settings

from .base import BaseDatabase, DatabaseConnection
from .url import MySQLURL


class MySQLDatabase(BaseDatabase):
    _connection = DatabaseConnection(MySQLURL, get_settings()["database"])
