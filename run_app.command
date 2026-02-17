#!/bin/bash
set -e
cd "$(dirname "$0")"

if command -v python3 >/dev/null 2>&1; then
  PYTHON_CMD=python3
elif command -v python >/dev/null 2>&1; then
  PYTHON_CMD=python
else
  echo "Python을 찾을 수 없습니다. Python 3를 설치해 주세요."
  read -n 1 -s -r -p "아무 키나 누르면 종료됩니다..."
  exit 1
fi

if [ ! -x .venv/bin/python ]; then
  echo "[1/4] 가상환경 생성 중..."
  "$PYTHON_CMD" -m venv .venv
fi

echo "[2/4] pip 업데이트 중..."
.venv/bin/python -m pip install --upgrade pip

echo "[3/4] 필요한 패키지 설치 중..."
.venv/bin/python -m pip install -r requirements.txt

echo "[4/4] 앱 실행 중... (브라우저가 자동으로 열립니다)"
if command -v xdg-open >/dev/null 2>&1; then
  xdg-open "http://127.0.0.1:5000" >/dev/null 2>&1 || true
elif command -v open >/dev/null 2>&1; then
  open "http://127.0.0.1:5000" >/dev/null 2>&1 || true
fi

.venv/bin/python app.py
