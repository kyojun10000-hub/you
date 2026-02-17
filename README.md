# YouTube Downloader Pro

화질/확장자 선택이 가능한 YouTube 다운로드 웹 앱입니다.

## 기능
- YouTube URL 입력
- 화질 선택: 최고, 1080p, 720p, 480p, 360p, 오디오 최고
- 확장자 선택: mp4, webm, mp3, m4a
- 가독성 높은 다크 테마 UI

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
