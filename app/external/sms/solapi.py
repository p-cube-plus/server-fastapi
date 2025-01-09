import configparser
import datetime
import hashlib
import hmac
import platform
import time
import uuid

import httpx

from app.core.config import get_settings

__all__ = ["send_sms"]

_config = get_settings()["sms"]

_url = _config["url"]
_api_key = _config["api_key"]
_api_secret = _config["api_secret"]
_from_number = _config["from_number"]


# 식별자 얻기
def _unique_id():
    return str(uuid.uuid1().hex)


# 시간 얻기
def _get_iso_datetime():
    utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
    utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
    return (
        datetime.datetime.now()
        .replace(tzinfo=datetime.timezone(offset=utc_offset))
        .isoformat()
    )


# 시그니처 생성
def _get_signature(key, msg):
    return hmac.new(key.encode(), msg.encode(), hashlib.sha256).hexdigest()


# 헤더 얻기
def _get_headers():
    date = _get_iso_datetime()
    salt = _unique_id()
    headers = {
        "Authorization": f"HMAC-SHA256 ApiKey={_api_key}, Date={date}, salt={salt}, signature={_get_signature(_api_secret, date + salt)}",
        "Content-Type": "application/json; charset=utf-8",
    }
    return headers


# Body 얻기
def _get_body(to_number, message):
    body = {
        "messages": [
            {
                "type": "SMS",  # SMS 타입에 한글 45자, 영자 90자 이상 입력되면 오류 발생
                "to": to_number,
                "from": _from_number,
                "text": message,
            }
        ],
        "agent": {
            "sdkVersion": "python/3.11.2",
            "osPlatform": f"{platform.platform()} | {platform.python_version()}",
        },
    }
    return body


# SMS 발송
async def send_sms(to_number, message):
    async with httpx.AsyncClient() as client:
        res = await client.post(
            _url, json=_get_body(to_number, message), headers=_get_headers()
        )
    return res
