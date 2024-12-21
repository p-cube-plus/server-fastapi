from .base import BaseDatabase, DatabaseConnection
from .url import SQLiteURL


class SQLiteDatabase(BaseDatabase):
    _connection = DatabaseConnection(SQLiteURL, {})
