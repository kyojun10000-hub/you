# YouTube Downloader Pro

화질/확장자 선택이 가능한 YouTube 다운로드 웹 앱입니다.

## 기능
- YouTube URL 입력
- 화질 선택: 최고, 1080p, 720p, 480p, 360p, 오디오 최고
- 확장자 선택: mp4, webm, mp3, m4a
- 가독성 높은 다크 테마 UI

## ZIP 다운로드 후 바로 실행 (더블클릭)
압축을 푼 뒤, 운영체제에 맞는 실행 파일을 **더블클릭**하면 자동으로 실행됩니다.

- **Windows (콘솔창 방식)**: `run_app.bat`
- **Windows (화면 앱 방식, 콘솔 숨김)**: `run_app_gui.bat`
- **macOS / Linux**: `run_app.command`

실행 파일은 아래를 자동으로 처리합니다.
1. 가상환경 생성 (`.venv`)
2. 의존성 설치 (`pip install -r requirements.txt`)
3. 브라우저 열기 (`http://127.0.0.1:5000`)
4. 앱 실행

> 참고: 최초 1회는 패키지 설치로 시간이 조금 걸릴 수 있습니다. (Python 3 설치 필요)

## 실행 방법
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

브라우저에서 `http://localhost:5000` 접속.

## 화면(데스크톱 창)으로 실행하기 (Windows)
`run_app_gui.bat`를 더블클릭하면 Flask 서버를 백그라운드로 띄운 뒤,
브라우저가 아니라 별도 앱 창(pywebview)으로 화면이 열립니다.

> 만약 pywebview 창을 띄우지 못하는 환경이면 자동으로 기본 브라우저를 엽니다.

## 참고
- mp3/m4a 또는 포맷 변환에는 `ffmpeg` 설치가 필요합니다.
- 다운로드 대상의 저작권 및 플랫폼 이용약관을 준수해 주세요.
