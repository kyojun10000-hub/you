@echo off
setlocal
cd /d "%~dp0"

where py >nul 2>&1
if %errorlevel%==0 (
    set "PYTHON_CMD=py"
) else (
    set "PYTHON_CMD=python"
)

if not exist ".venv\Scripts\python.exe" (
    echo [1/4] 가상환경 생성 중...
    %PYTHON_CMD% -m venv .venv
    if errorlevel 1 goto :error
)

echo [2/4] pip 업데이트 중...
".venv\Scripts\python.exe" -m pip install --upgrade pip
if errorlevel 1 goto :error

echo [3/4] 필요한 패키지 설치 중...
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto :error

echo [4/4] 앱 실행 중... (브라우저가 자동으로 열립니다)
start "" "http://127.0.0.1:5000"
".venv\Scripts\python.exe" app.py
if errorlevel 1 goto :error

exit /b 0

:error
echo.
echo 실행 중 오류가 발생했습니다. 위 메시지를 확인해 주세요.
pause
exit /b 1
