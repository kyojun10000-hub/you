from __future__ import annotations

import threading
import time
import webbrowser

from app import app


def _run_server() -> None:
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)


def main() -> None:
    server_thread = threading.Thread(target=_run_server, daemon=True)
    server_thread.start()

    time.sleep(1)

    try:
        import webview

        webview.create_window("YouTube Downloader Pro", "http://127.0.0.1:5000", width=1200, height=800)
        webview.start()
    except Exception:
        webbrowser.open("http://127.0.0.1:5000")
        while True:
            time.sleep(1)


if __name__ == "__main__":
    main()
