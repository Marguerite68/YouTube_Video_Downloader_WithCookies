Have you grown tired of wasting time on search engines trying to find a truly free YouTube video downloader? Frustrated with bugs in high-star GitHub projects? Don’t want to pay, and don’t want to wait for authors to respond to issues? Encounter problems downloading age-restricted videos or bulk playlists? Don’t worry! This tutorial will walk you through how to download **99.99% of YouTube videos**, free from restrictions on resolution, quantity, or limitations.

> ⚠️ **Note**: This tutorial assumes **basic programming knowledge and computer skills**. It’s not intended for complete beginners. However, all steps are explained clearly and accessibly — as long as you follow them carefully, you should encounter minimal issues.

---

## **Preparation**

* A reasonably capable computer running Windows 10 or later
* An IDE with Python 3.12 or later already configured (e.g., PyCharm or VS Code — as long as it can run `.py` files)
* A YouTube account
* Google Chrome browser
* That’s it!

---

## **Environment Setup & Plugin Configuration**

### 1) Set Up `ffmpeg`

* Go to the [official FFmpeg website](https://ffmpeg.org/download.html) and download the Windows version: `ffmpeg-7.0.2-essentials_build.zip`
* Extract the zip file to a directory such as `C:\ffmpeg`
* Add the `ffmpeg` `bin` directory to your system’s **Environment Variables**:

  * Right-click **This PC** → **Properties** → **Advanced System Settings** → **Environment Variables**
  * Under **System Variables**, find `Path`, click Edit, and add the `bin` directory (e.g., `C:\ffmpeg\bin`)
* Open Command Prompt or PowerShell and run the following command to verify the installation:

```bash
ffmpeg -version
```

If the version info appears, installation is successful. Example output:

```bash
ffmpeg version 7.0.2-essentials_build-www.gyan.dev Copyright (c) 2000-2024 ...
...
libpostproc    58.  1.100 / 58.  1.100
```

> 💡
> For a detailed tutorial, refer to this guide (in Chinese): [Install ffmpeg on Windows](https://blog.csdn.net/Natsuago/article/details/143231558)

---

### 2) Install `yt-dlp`

You can install `yt-dlp` **globally** or **within your project directory**. Differences:

* **Global Installation**:

  * `yt-dlp` is installed in a global path (e.g., `Python\Scripts`)
  * You can run `yt-dlp` from any directory via terminal
  * Useful if you want to share `yt-dlp` across multiple projects

* **Local Installation**:

  * Executable files and dependencies are only available to the current project
  * Suitable for isolated or portable setups

For convenience, this tutorial uses **global installation**.

Run the following in Command Prompt or PowerShell:

```bash
pip install yt-dlp
```

Check if the installation was successful:

```bash
yt-dlp --version
```

Sample output:

```bash
2024.12.06
```

---

### 3) Install the **Get cookies.txt LOCALLY** Chrome Extension

* Open Chrome
* Go to the Chrome Web Store
* Search for and install **Get cookies.txt LOCALLY**

Download this plugin in Chrome: [get-cookiestxt-locally](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc?pli=1)

This plugin is essential for extracting cookies from YouTube pages.

> ⚠️ When downloading age-restricted content, YouTube relies on cookies to verify your identity. Without valid cookies, you **cannot** access restricted videos.
> If you're under 18, unfortunately, there's no workaround.


---

## **Main Program Usage**

* Clone this project to your local IDE
* Configure a Python interpreter (Python 3.12 or above) in your IDE
* Open `main.py` — you can run the program directly from this file

---

### Feature Explanation

#### Set Download Quality

This part sets max resolution:

```python
-f "bestvideo[height<=1080]+bestaudio/best[height<=1080]"
```

You can modify the `height<=1080` part to values like `720` or `2160` (2K) based on your preferences.

#### Cookie Expiry Timer

YouTube login cookies usually expire in **about 20 minutes**. If you're downloading age-restricted videos, you'll need to refresh cookies periodically.

This script has a **built-in countdown timer** with a warning 3 minutes before cookies expire. You can customize the duration in:

```python
monitor_cookie_file(cookie_file, reset_event, warn_event, interval=18*60)
```

Here, `18*60` means 18 minutes. Modify it to suit your needs.

When you update and save the `cookies.txt` file, the countdown resets automatically.

---

## Step-by-Step Video Download Instructions

1. Clear Chrome’s **browsing data**, especially cookies.
2. Open YouTube — you should now be signed out.
3. **Log back in** to your YouTube account.
4. Click the Get cookies.txt LOCALLY plugin icon → click **Export All Cookies**
5. A `.txt` file will be downloaded. **Copy all its contents** and paste them into your `cookies.txt` file in the Python project folder.
6. Save the file.
7. Run the Python program. In the terminal:

   * Paste your video or playlist link
   * Answer whether it's a playlist (`y/n`)
   * If it's a playlist, input the **starting video number**
8. Videos will be downloaded to a `downloads` folder in your project directory.

> ✅ **Tips for Playlist Downloads**:
>
> * Downloaded files are named with the corresponding video index in the playlist.
> * To avoid restarting from the beginning if interrupted, you can specify the **starting index**.
> * Keep updating cookies every \~20 minutes if downloading age-restricted videos.

---

Last updated: **2024.12.12**

**NON-COMMERCIAL USE ONLY**

<a href="https://github.com/Marguerite68/YouTube_Video_Downloader_WithCookies"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">YouTube_Video Downloader WithCookies</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> © 2024 by </font></font><a href="https://github.com/Marguerite68"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Marguerite</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">已获得</font></font><a href="https://creativecommons.org/licenses/by-nc/4.0/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Creative Commons Attribution-NonCommercial 4.0 International许可</font></font></a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" style="max-width: 1em;max-height:1em;margin-left: .2em;">


For questions, email: [sekaibest@outlook.com](mailto:sekaibest@outlook.com)

Follow me on X: [https://linktr.ee/marguerite68](https://linktr.ee/marguerite68)

对于中文版操作指引，请详见：[利用Python批量下载Youtube中含有年龄限制视频的播放列表全指北](https://recondite-citron-f48.notion.site/Python-Youtube-15a9545f48c7806cb025f9a97f825b1d)
> ⚠️ **Note**: 中文版指引可能与此Readme内容不完全相同。遇到内容不同时，请以此英文版Readme为准
