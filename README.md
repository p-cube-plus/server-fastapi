# 개발 유의사항

## 개요

개발 관련 정보 작성 중...

## Git Hooks 경로 변경

아래 명령어 입력 후 커밋 시 자동으로 포매팅 수행됨.

```bash
git config core.hooksPath .githooks
```

## 프로젝트 최초 다운로드 시 설정

프로젝트의 root 경로에서 진행할 것.

### poetry 설치

사용 중인 OS에 따라 적절히 설치

### python3.12 설치 (pyenv 이용)

(다른 방법으로 python3.12를 설치했다면 이 부분은 건너뛸 것)

```bash
# pyenv로 python3.12 설치
pyenv install 3.12

# 다음 명령어 입력 시 .python-version 파일이 자동 생성됨.
pyenv local 3.12
```

### poetry로 가상 환경 생성 및 패키지 설치

```bash
# pyenv로 python3.12를 설치한 경우
poetry env use $(pyenv which python)
# OS에 직접 설치한 경우
poetry env use $(which python3.12)

# 패키지 설치
poetry install
```

### 가상 환경 실행

```bash
poetry shell
```

### 프로젝트 실행

```bash
python -m app.main
```

### 가상 환경 종료
```bash
deactivate
```

## Docker Compose 이용한 서버 실행 방법

### docker container 실행

프로젝트 경로에서 아래 명령어 실행

```bash
sudo docker compose up -d

# 프로젝트 변경 사항 반영하여 실행할 시 다음 명령어 대신 실행
sudo docker compose up -d --build
```

컨테이너 종료

```bash
sudo docker compose down
```

컨테이너 재시작

```bash
sudo docker compose restart
```