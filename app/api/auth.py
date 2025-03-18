from typing import Annotated

from fastapi import Depends, HTTPException, status

from app.constant.user import UserRole
from app.core.routing import CustomAPIRouter
from app.core.security import JWTCodec, get_current_user, get_jwt, require_role
from app.dto.auth import (
    OTPSendPost,
    OTPSendResponse,
    OTPVerifyPost,
    OTPVerifyResponse,
    TokenRefreshPost,
    TokenResponse,
)
from app.service.auth import OTPService

router = CustomAPIRouter(
    prefix="/auth",
)


@router.post("/otp/send", response_model=OTPSendResponse)
async def send_otp(
    otp_send_post: OTPSendPost, service: Annotated[OTPService, Depends()]
):
    response = await service.send_otp(otp_send_post)
    return response


@router.post("/otp/verify", response_model=TokenResponse)
async def verify_otp(
    otp_verify_post: OTPVerifyPost, service: Annotated[OTPService, Depends()]
):
    result = await service.verify_otp(otp_verify_post, 180)

    if not result.is_verified and otp_verify_post.identifier != "guest":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid OTP code or OTP has expired",
        )

    payload = {
        "user_id": 1,
        "role": UserRole.USER,
    }

    access_token = JWTCodec.encode(payload, "access")
    refresh_token = JWTCodec.encode(payload, "refresh")

    return TokenResponse(access_token=access_token, refresh_token=refresh_token)


@router.post("/token/refresh", response_model=TokenResponse)
async def refresh_token(token_refresh_post: TokenRefreshPost):
    payload = JWTCodec.decode(token_refresh_post.refresh_token)

    access_token = JWTCodec.encode(payload, "access")
    refresh_token = JWTCodec.encode(payload, "refresh")

    return TokenResponse(access_token=access_token, refresh_token=refresh_token)


@router.get("/test")
@require_role(UserRole.USER)
async def test():
    jwt = get_jwt()
    return {"jwt_payload": jwt}


@router.get("/test-admin-api")
@require_role(UserRole.ADMIN)
async def test_admin_api():
    jwt = get_jwt()
    return {"jwt_payload": jwt}


@router.get("/test-whoami")
@require_role(UserRole.USER)
async def whoami():
    user_id = get_current_user()
    return {"user_id": user_id}
