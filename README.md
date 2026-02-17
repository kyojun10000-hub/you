# YouTube Downloader Pro

화질/확장자 선택이 가능한 YouTube 다운로드 웹 앱입니다.

## 기능
- YouTube URL 입력
- 화질 선택: 최고, 1080p, 720p, 480p, 360p, 오디오 최고
- 확장자 선택: mp4, webm, mp3, m4a
- 가독성 높은 다크 테마 UI

## ZIP 다운로드 후 바로 실행 (더블클릭)
압축을 푼 뒤, 운영체제에 맞는 실행 파일을 **더블클릭**하면 자동으로 실행됩니다.

- **Windows**: `run_app.bat`
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

## 참고
- mp3/m4a 또는 포맷 변환에는 `ffmpeg` 설치가 필요합니다.
- 다운로드 대상의 저작권 및 플랫폼 이용약관을 준수해 주세요.
