from __future__ import annotations

import os
import re
import uuid
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, send_from_directory, url_for
from yt_dlp import YoutubeDL

BASE_DIR = Path(__file__).resolve().parent
DOWNLOAD_DIR = BASE_DIR / "downloads"
DOWNLOAD_DIR.mkdir(exist_ok=True)

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY", "change-me-in-production")

QUALITY_MAP = {
    "best": "bestvideo*+bestaudio/best",
    "1080p": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
    "720p": "bestvideo[height<=720]+bestaudio/best[height<=720]",
    "480p": "bestvideo[height<=480]+bestaudio/best[height<=480]",
    "360p": "bestvideo[height<=360]+bestaudio/best[height<=360]",
    "audio_best": "bestaudio/best",
}

EXT_OPTIONS = {"mp4", "webm", "mp3", "m4a"}


def _safe_filename(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9가-힣._ -]", "", value).strip()
    return value or "video"


def _download_video(url: str, quality: str, ext: str) -> str:
    file_id = uuid.uuid4().hex[:8]
    output_template = str(DOWNLOAD_DIR / f"%(title)s-{file_id}.%(ext)s")

    ydl_opts = {
        "outtmpl": output_template,
        "noplaylist": True,
        "quiet": True,
        "merge_output_format": "mp4" if ext == "mp4" else None,
    }

    if ext in {"mp3", "m4a"}:
        ydl_opts["format"] = "bestaudio/best"
        ydl_opts["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": ext,
                "preferredquality": "192",
            }
        ]
    else:
        ydl_opts["format"] = QUALITY_MAP.get(quality, QUALITY_MAP["best"])
        ydl_opts["postprocessors"] = [
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": ext,
            }
        ]

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        raw_title = info.get("title", "video")

    prefix = f"{_safe_filename(raw_title)}-{file_id}"
    candidates = sorted(DOWNLOAD_DIR.glob(f"{prefix}*"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not candidates:
        raise FileNotFoundError("다운로드 파일을 찾을 수 없습니다.")

    return candidates[0].name


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/download")
def download():
    url = request.form.get("url", "").strip()
    quality = request.form.get("quality", "best")
    ext = request.form.get("ext", "mp4")

    if not url:
        flash("유튜브 URL을 입력해 주세요.", "error")
        return redirect(url_for("index"))

    if ext not in EXT_OPTIONS:
        flash("지원되지 않는 확장자입니다.", "error")
        return redirect(url_for("index"))

    try:
        filename = _download_video(url, quality, ext)
    except Exception as exc:
        flash(f"다운로드 실패: {exc}", "error")
        return redirect(url_for("index"))

    flash("다운로드 완료! 파일을 저장해 주세요.", "success")
    return redirect(url_for("file_download", filename=filename))


@app.get("/files/<path:filename>")
def file_download(filename: str):
    return send_from_directory(DOWNLOAD_DIR, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
