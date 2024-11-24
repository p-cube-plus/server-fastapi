# base python image
FROM python:3.12-alpine

# working directory 지정
WORKDIR /src

# pyproject.toml 및 poetry.lock 복사
COPY pyproject.toml poetry.lock ./

# poetry 및 python 패키지 설치
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --without dev

# 전체 코드 복사
COPY . .

# FastAPI 서버 실행
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.main:app", "--worker-class", "uvicorn.workers.UvicornWorker", "--workers", "2"]