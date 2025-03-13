from contextvars import ContextVar
from datetime import datetime, timedelta
from typing import Literal, Optional

import jwt
from fastapi import HTTPException, Request, Response, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.config import get_settings

_config = get_settings()["jwt"]

_jwt_context = ContextVar("jwt_context")


class JWTCodec:
    algorithm: str = _config["algorithm"]
    secret_key: str = _config["secret_key"]
    access_token_expire_minutes: int = int(_config["access_token_expire_minutes"])
    refresh_token_expire_days: int = int(_config["refresh_token_expire_days"])

    @staticmethod
    def _create_access_token(payload: dict) -> str:
        exp = datetime.now() + timedelta(minutes=JWTCodec.access_token_expire_minutes)
        encoded_payload = {**payload, "exp": exp, "token_type": "access"}

        return jwt.encode(
            encoded_payload, JWTCodec.secret_key, algorithm=JWTCodec.algorithm
        )

    @staticmethod
    def _create_refresh_token(payload: dict) -> str:
        exp = datetime.now() + timedelta(days=JWTCodec.refresh_token_expire_days)
        encoded_payload = {**payload, "exp": exp, "token_type": "refresh"}

        return jwt.encode(encoded_payload, JWTCodec.secret_key, algorithm="HS256")

    @staticmethod
    def encode(payload: dict, token_type: Literal["access", "refresh"]) -> str:
        if token_type == "access":
            return JWTCodec._create_access_token(payload)
        else:
            return JWTCodec._create_refresh_token(payload)

    @staticmethod
    def decode(token: str) -> Optional[dict]:
        try:
            return jwt.decode(token, JWTCodec.secret_key, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
        except jwt.InvalidSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token signature",
                headers={"WWW-Authenticate": "Bearer"},
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token format",
                headers={"WWW-Authenticate": "Bearer"},
            )


class JWT:
    def __init__(self, payload: dict):
        self.payload = payload


class JWTAuthenticator(HTTPBearer):
    def __init__(self, *, access_level: int, auto_error: bool = True):
        super().__init__(auto_error=auto_error)
        self.access_level = access_level

    async def __call__(self, request: Request):
        cred: HTTPAuthorizationCredentials = await super().__call__(request)
        payload: dict = JWTCodec.decode(cred.credentials)
        return JWT(payload)


class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        token = _jwt_context.set({})
        try:
            auth_header = request.headers.get("Authorization")

            if auth_header and auth_header.startswith("Bearer "):
                token_str = auth_header.replace("Bearer ", "")
                try:
                    payload = JWTCodec.decode(token_str)
                    _jwt_context.set(payload)
                except Exception:
                    pass
            response = await call_next(request)
            return response
        finally:
            _jwt_context.reset(token)


def get_jwt() -> dict:
    return _jwt_context.get()


def get_current_user() -> int:
    jwt: dict = _jwt_context.get()
    return jwt.get("user_id")
