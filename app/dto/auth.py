from .base import BaseDTO


class OTPSendPost(BaseDTO):
    phone_number: str


class OTPSendResponse(BaseDTO):
    identifier: str


class OTPVerifyPost(BaseDTO):
    identifier: str
    otp: str


class OTPVerifyResponse(BaseDTO):
    is_verified: bool
