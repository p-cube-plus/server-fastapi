from typing import Annotated

from fastapi import Depends

from app.core.routing import CustomAPIRouter
from app.dto.auth import OTPSendPost, OTPSendResponse, OTPVerifyPost, OTPVerifyResponse
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


@router.post("/otp/verify", response_model=OTPVerifyResponse)
async def verify_otp(
    otp_verify_post: OTPVerifyPost, service: Annotated[OTPService, Depends()]
):
    response = await service.verify_otp(otp_verify_post, 180)
    return response
