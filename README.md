# 개발 유의사항

## 개요

개발 관련 정보 작성 중...

## Git Hooks 경로 변경

아래 명령어 입력 후 커밋 시 자동으로 포매팅 수행됨.

```bash
git config core.hooksPath .githooks
```

## 서버 실행 방법

### main.py 직접 실행

```bash
python -m app.main
```

### docker container 실행

프로젝트 경로에서 아래 명령어 실행

```bash
sudo docker compose up -d
```

컨테이너 종료

```bash
sudo docker compose down
```

컨테이너 재시작

```bash
sudo docker compose restart
```

만약 수정 사항 반영 안 될 시 아래 명령어를 대신 실행

```bash
sudo docker compose up -d --build
```