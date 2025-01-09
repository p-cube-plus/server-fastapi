import base64
import os
import random
from datetime import datetime

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from fastapi import HTTPException

from app.core.config import get_settings
from app.dto.auth import OTPSendPost, OTPSendResponse, OTPVerifyPost, OTPVerifyResponse
from app.external.sms import send_sms
from app.service.base import BaseService


class OTPService(BaseService):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OTPService, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return
        self.aesgcm = AESGCM(get_settings()["otp"]["key"].encode())
        self.__initialized = True

    async def send_otp(self, post: OTPSendPost) -> OTPSendResponse:
        otp = self.generate_otp()
        identifier = self.create_identifier(post.phone_number, otp)

        message = f"[PCube+]\n인증번호는 {otp}입니다."

        response = await send_sms(post.phone_number, message)
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="SMS 발송 실패")

        return OTPSendResponse(identifier=identifier)

    async def verify_otp(
        self, post: OTPVerifyPost, valid_duration: int = 180
    ) -> OTPVerifyResponse:
        try:
            raw = base64.urlsafe_b64decode(post.identifier.encode())
            nonce, ciphertext = raw[:12], raw[12:]

            decrypted = self.aesgcm.decrypt(nonce, ciphertext, None).decode()
            phone_number, otp, timestamp = decrypted.split(":")

            current_time = int(datetime.now().timestamp())
            if current_time - int(timestamp) > valid_duration:
                return OTPVerifyResponse(is_verified=False)

            is_verified = otp == post.otp
            return OTPVerifyResponse(is_verified=is_verified)

        except Exception:
            return OTPVerifyResponse(is_verified=False)

    def generate_otp(self) -> str:
        return f"{random.randint(0, 999999):06d}"

    def create_identifier(self, phone_number: str, otp: str) -> str:
        nonce = os.urandom(12)
        timestamp = int(datetime.now().timestamp())
        payload = f"{phone_number}:{otp}:{timestamp}"

        ciphertext = self.aesgcm.encrypt(nonce, payload.encode(), None)
        return base64.urlsafe_b64encode(nonce + ciphertext).decode()
