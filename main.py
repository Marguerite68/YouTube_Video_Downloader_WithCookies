import subprocess
import os
import time
import threading


# 检测 Cookie 文件更新的线程
def monitor_cookie_file(cookie_file, reset_event, warn_event, interval=200):#这里设置默认倒计时为18分钟
    """
    监控 Cookie 文件的修改时间，并重置倒计时。

    参数:
        cookie_file (str): Cookie 文件路径。
        reset_event (threading.Event): 用于重置计时器的事件。
        warn_event (threading.Event): 用于发出警告的事件。
        interval (int): 倒计时总时间（秒）。
    """
    last_modified = os.path.getmtime(cookie_file)
    countdown = interval

    while True:
        time.sleep(1)
        current_modified = os.path.getmtime(cookie_file)

        # 检测文件修改时间是否变化
        if current_modified != last_modified:
            print("[INFO] 检测到 Cookie 文件更新，重置计时器。")
            reset_event.set()
            last_modified = current_modified

        # 检查倒计时状态
        countdown -= 1
        if countdown <= 180:  # 剩余3分钟时发出警告
            warn_event.set()

        if reset_event.is_set():
            reset_event.clear()
            countdown = interval
            warn_event.clear()

        if countdown <= 0:
            print("[ERROR] Cookie 文件可能已过期，请及时更新！")
            break


def download_youtube_video_or_playlist(url, output_dir="downloads", start_video=None):
    """
    下载单个 YouTube 视频或整个播放列表的视频。

    参数:
        url (str): 视频或播放列表链接。
        output_dir (str): 视频存储的目录。
        start_video (int): 如果是播放列表，指定从第 n 个视频开始下载。
    """
    # 检查默认 Cookie 文件是否存在
    cookie_file = "cookies.txt"
    if not os.path.isfile(cookie_file):
        print(f"错误: 无法找到默认的 Cookie 文件 ({cookie_file})。请确保文件存在！")
        return

    # 创建存储目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # yt-dlp 命令
    command = [
        "yt-dlp",
        "--cookies", cookie_file,  # 使用默认 Cookie 文件进行授权
        "-f", "bestvideo[height<=1080]+bestaudio/best[height<=1080]",  # 下载 1080p 或更低清晰度的视频和音频
        "-o", os.path.join(output_dir, "%(title)s.%(ext)s"),  # 设置输出文件名
    ]

    # 如果指定了起始视频编号，则添加播放列表相关参数
    if start_video is not None:
        command += ["--yes-playlist", "--playlist-start", str(start_video)]

    # 添加 URL
    command.append(url)

    print(f"开始下载：{url}")
    subprocess.run(command)  # 执行 yt-dlp 命令
    print(f"下载完成！")


if __name__ == "__main__":
    # 用户输入链接
    url = input("请输入 YouTube 视频或播放列表链接: ").strip()

    # 判断是否是播放列表，并询问用户是否指定起始视频编号
    is_playlist = input("这是播放列表吗？(y/n): ").strip().lower() == "y"
    start_video = None
    if is_playlist:
        start_video = int(input("请输入从第几个视频开始下载（数字，默认1）: ").strip() or 1)

    # 启动 Cookie 文件监控线程
    cookie_file = "cookies.txt"
    reset_event = threading.Event()
    warn_event = threading.Event()
    monitor_thread = threading.Thread(target=monitor_cookie_file, args=(cookie_file, reset_event, warn_event))
    monitor_thread.daemon = True
    monitor_thread.start()

    # 主下载逻辑
    download_youtube_video_or_playlist(url, start_video=start_video if is_playlist else None)

    print("[INFO] 程序运行完成。")
