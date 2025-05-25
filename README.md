Have you grown tired of wasting time on search engines trying to find a truly free YouTube video downloader? Frustrated with bugs in some high-star GitHub projects? Don’t want to pay, and don’t want to wait for authors to respond to issues? Encounter problems downloading age-restricted videos or bulk playlists? Don’t worry! This project and README.md will walk you through how to download **99.99% of YouTube videos**, free from restrictions on resolution, quantity, or limitations.

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


### Customizable Features

* **Set Download Quality**:

  The download quality is controlled via the format string:
  `"bestvideo[height<=1080]+bestaudio/best[height<=1080]"`.
  The `1080` in `bestvideo[height<=1080]` indicates that the script will download 1080p video if available; otherwise, it will download the next best resolution.
  You can change it to `720`, `2160`, etc., to download up to 720p or 2K quality.
  The `bestaudio/best[height<=1080]` part works similarly: change `1080` to match your desired video resolution for audio pairing (generally, no need to modify this).

* **Cookie Expiration Timer**:

  As is widely known, browser cookies—especially those storing login credentials—tend to expire quickly. Based on practical testing, YouTube login cookies typically expire in about **20 minutes**.
  This means if you want to continuously download **age-restricted videos**, you'll need to regularly refresh your cookies.

  For videos **without age restrictions**, cookie refresh is not required.

  This script includes a **cookie expiration timer** to remind users to update cookies in time.
  Located in the function:
  `monitor_cookie_file(cookie_file, reset_event, warn_event, interval=18*60):`
  The `18*60` means the timer runs for 18 minutes per cycle. You can modify this value to customize the countdown interval.
  A warning will be printed at **3 minutes before expiry** and **at expiration**.
  When the script detects changes saved to the `cookies.txt` file (e.g., using `Ctrl+S`), the timer will reset automatically.

---

### How to Download Videos

1. **Clear your Chrome browser history**, especially **Cookies**.

2. After clearing, go to [YouTube](https://www.youtube.com/) — you should now be logged out.

3. **Log back into your YouTube account**.

4. Once logged in, your cookies are freshly generated—and the expiration countdown starts immediately, so continue the following steps quickly.

5. On the YouTube homepage, click the **Get cookies.txt LOCALLY** browser extension icon in the toolbar, then click **Export All Cookies**. A `.txt` file will be downloaded.

6. Open the downloaded `.txt` file, **copy all its content without modifications**, and paste it into the `cookies.txt` file located in the root directory of the Python project. Save the file.

7. Run the program from your IDE and monitor the output in the Terminal.

8. The script will prompt you to input a video URL (either a single video or a playlist).

9. Paste the desired YouTube link and press Enter.

10. The program will ask if it's a **single video**:

    * If yes: it will download the video immediately.
    * If no: it switches to **playlist mode**, and will ask which video index to start downloading from.

      * In playlist mode, downloaded videos are **prefixed with an index number** corresponding to their order in the playlist.
      * Since the script **checks videos from the beginning** on every run, this may waste valuable cookie time. Specifying the **start index** helps skip already downloaded videos and save time.
      * To continue downloading restricted content, **manually refresh your cookies at least once every 20 minutes**: repeat the “Clear → Login → Export → Copy → Paste → Save” process.
      * Unrestricted videos can still be downloaded without updating cookies.

11. Wait for the downloads to complete. All downloaded files will be saved in the `downloads` folder in the project root.

---

Last updated: **2025.5.25**

**NON-COMMERCIAL USE ONLY**

<a href="https://github.com/Marguerite68/YouTube_Video_Downloader_WithCookies"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">YouTube_Video Downloader WithCookies</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> © 2024 by </font></font><a href="https://github.com/Marguerite68"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Marguerite</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">已获得</font></font><a href="https://creativecommons.org/licenses/by-nc/4.0/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Creative Commons Attribution-NonCommercial 4.0 International许可</font></font></a>

<img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" style="max-width: 50px;max-height:50px;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" style="max-width: 50px;max-height:50px;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" style="max-width: 50px;max-height:50px;margin-left: .2em;">


For questions, email: [sekaibest@outlook.com](mailto:sekaibest@outlook.com)

对于中文版操作指引，请详见：[利用Python批量下载Youtube中含有年龄限制视频的播放列表全指北](https://recondite-citron-f48.notion.site/Python-Youtube-15a9545f48c7806cb025f9a97f825b1d)
> ⚠️ **Note**: 中文版指引可能与此README内容不完全相同。遇到内容不同时，请以此英文版README为准
