import re
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Function to sanitize the video title for a valid file name
def sanitize_filename(title):
    return re.sub(r'[<>:"/\\|?*]', '_', title)  # Replace invalid characters with '_'

# Set up Selenium WebDriver
options = Options()
options.add_argument("start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)
driver.get("https://www.tiktok.com/@romania")  # Replace with the TikTok video URL

# Wait for the page to load
driver.implicitly_wait(5)

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# Define cookies and headers for requests (These are likely to be needed in a real scraping context)
cookies = {
    'cf_clearance': 'P06jsxmcAOm5RE667Liyy8JqAqmtK.yxk37RcFoR4jE-1731336275-1.2.1.1-YQUdbxr83VgvzpaPhbY9lFxNchdPD0NlHXsJd_X8dBhVMMMh8dd9Hjjtb7AsKgxxsNaUi52qfl7o3SWLVAWVM06cYIQzVKqhO2Z8GxSFDXcEwNuIoQlyZZLQj5LFvPYWgetdCfZX.mULyAYeUTfAQXv.nEq1LhScbzteV0NlNknlwGtChz_YiFJVg_7f.XMhHNzsv1o2aJce3b8JMnrj_u7VNY22y.M_DQ.AD_h4itfhOmm4ngHGMGxtbbMEHCJ9VMhB2xujoUxLNGhzPlF6LwiY0eZZ9ZNxKKDVt_PDMoHUUMdr5YfpSNVZuzQjqhj_i4qn5WKPEFx9ORltwzrw1Ls6TRpKSgQPOajeUpC.G4nSTz56wJnWBPF1fLV5NaMab1Y6tJS8oZXJjIEzGdE8C8UirGQCeZnr1Gn6Bfow4NzkV_.PA5CyfPCml2BlF7Tn',
    '_ga': 'GA1.1.1880707367.1731336266',
    '__gads': 'ID=2f68e49bf6b21a33:T=1731336288:RT=1731336631:S=ALNI_MaKBxBiySHqf5pMHNnAtgySAzwyaw',
    '__gpi': 'UID=00000f6623e3aafe:T=1731336288:RT=1731336631:S=ALNI_MZddt_64JSmTFK48dpPU6WRKhlxlQ',
    '__eoi': 'ID=8b626cf14807e69d:T=1731336288:RT=1731336631:S=AA-AfjYCn9Z2Y6Gy6oDS5SXbMm97',
    'FCNEC': '%5B%5B%22AKsRol_2rX1R8dxkNmB5MENtZQjtyC2C_oBHggEm6kdxe22BTE_oZ8-jWrPvoQqIaHrfdHBXWVwtrvNeSCNPy4W7AoqyLNS1lsEs1A4g611l7HvjKUO7-I9RXMnhi4205oahWXMZ2Fp3EuJxPkFmP0oTzT3jxOCOZg%3D%3D%22%5D%5D',
    '_ga_ZSF3D6YSLC': 'GS1.1.1731336265.1.1.1731336629.46.0.0',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'hx-current-url': 'https://ssstik.io/',
    'hx-request': 'true',
    'hx-target': 'target',
    'hx-trigger': '_gcaptcha_pt',
    'origin': 'https://ssstik.io',
    'priority': 'u=1, i',
    'referer': 'https://ssstik.io/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.117 Safari/537.36',
}

params = {
    'url': 'dl',
}

data = {
    'id': 'https://www.tiktok.com/@romania/video/7410452584588250401',  # Replace with the actual video URL
    'locale': 'en',
    'tt': 'WEp5bXY3',
}

# Make the request to get the download link
response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)

# Parse the response to get the download link
downloadSoup = BeautifulSoup(response.text, "html.parser")

downloadLink = downloadSoup.a["href"]
videoTitle = downloadSoup.p.getText().strip()

# Sanitize the video title for a valid file name
safe_video_title = sanitize_filename(videoTitle)

# Download the video
mp4File = urlopen(downloadLink)
with open(f"videos/{safe_video_title}.mp4", "wb") as output:
    while True:
        data = mp4File.read(4096)
        if data:
            output.write(data)
        else:
            break

print(f"Video {safe_video_title} downloaded successfully.")

# Close the WebDriver
driver.quit()
