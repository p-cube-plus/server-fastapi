from typing import Any, ClassVar, Dict

from sqlalchemy.engine.url import URL


class MySQLURL:
    DRIVER: ClassVar[str] = "mysql+aiomysql"

    def __new__(cls, settings: Dict[str, Any]) -> URL:
        return URL.create(
            drivername=cls.DRIVER,
            username=settings["user"],
            password=settings["password"],
            host=settings["host"],
            port=int(settings["port"]),
            database=settings["db"],
        )


class SQLiteURL:
    DRIVER: ClassVar[str] = "sqlite+aiosqlite"

    def __new__(cls, settings: Dict[str, Any]) -> URL:
        return str(
            URL.create(drivername=cls.DRIVER, database=settings.get("db", ":memory:"))
        )
