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
# 가상 환경 생성 시 프로젝트 경로 내부에 생성 (.venv 디렉터리가 생성됨)
# 필수 설정은 아니나, 간혹 IDE에서 가상 환경의 인터프리터를 찾지 못하는 경우가 있어
# 아래 명령어를 실행하는 것을 추천
poetry config virtualenvs.in-project true

# pyenv로 python3.12를 설치한 경우
poetry env use $(pyenv which python)
# OS에 직접 설치한 경우 (필요 시 괄호 안의 값을 알맞은 경로로 대체할 것)
poetry env use $(which python3.12)

# 패키지 설치
poetry install
```

### 가상 환경 실행

```bash
poetry shell

# shell 커맨드를 설치해야 한다고 출력되는 경우 아래 명령어 대신 실행
eval $(poetry env activate)
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