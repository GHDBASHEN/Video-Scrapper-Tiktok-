from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

def downloadVideo(link, id):
    try:
        print(f"Downloading video {id} from: {link}")
        cookies = {
            # Replace with actual cookie data from browser session
        }

        headers = {
            # Replace with actual header data from browser session
        }

        params = {
            'url': 'dl',
        }

        data = {
            'id': link,
            'locale': 'en',
            'tt': '',  # Use the actual 'tt' value from the network request
        }
        
        response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
        downloadSoup = BeautifulSoup(response.text, "html.parser")

        # Extract download link safely
        downloadLink = downloadSoup.a["href"] if downloadSoup.a else None
        if not downloadLink:
            print("Failed to find download link.")
            return

        videoTitle = downloadSoup.p.getText().strip() if downloadSoup.p else f"video_{id}"

        # Ensure the download directory exists
        os.makedirs("videos", exist_ok=True)

        print("Saving the video...")
        mp4File = urlopen(downloadLink)
        with open(f"videos/{id}-{videoTitle}.mp4", "wb") as output:
            while True:
                data = mp4File.read(4096)
                if not data:
                    break
                output.write(data)

        print(f"Video {id} downloaded successfully.")
    except Exception as e:
        print(f"Error downloading video {id}: {e}")

print("Opening Chrome browser...")
options = Options()
options.add_argument("start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Set the path to chromedriver
chromedriver_path = "C:\Program Files\Google\Chrome\Application"  # Update with your actual path
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

try:
    # Navigate to the TikTok page
    driver.get("https://www.tiktok.com/@romania")
    time.sleep(1)  # Adjust as needed for CAPTCHA handling

    scroll_pause_time = 1
    screen_height = driver.execute_script("return window.screen.height;")
    i = 1

    print("Scrolling page...")
    while True:
        driver.execute_script(f"window.scrollTo(0, {screen_height}*{i});")
        i += 1
        time.sleep(scroll_pause_time)
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        if (screen_height) * i > scroll_height:
            break

    # Extract URLs for videos
    className = "tiktok-1s72ajp-DivWrapper"
    script = """
    let l = [];
    document.getElementsByClassName("tiktok-1s72ajp-DivWrapper").forEach(item => {
        let link = item.querySelector('a');
        if (link) l.push(link.href);
    });
    return l;
    """

    urlsToDownload = driver.execute_script(script)
    print(f"Found {len(urlsToDownload)} videos to download.")

    for index, url in enumerate(urlsToDownload):
        print(f"Starting download for video {index + 1}/{len(urlsToDownload)}")
        downloadVideo(url, index)
        time.sleep(10)  # Adjust delay as necessary

finally:
    driver.quit()
    print("Browser closed.")
