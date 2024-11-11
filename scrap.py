from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from urllib.request import urlopen

def downloadVideo(link, id):
    print(f"Downloading video {id} from: {link}")
    cookies = {
    'cf_clearance': 'P06jsxmcAOm5RE667Liyy8JqAqmtK.yxk37RcFoR4jE-1731336275-1.2.1.1-YQUdbxr83VgvzpaPhbY9lFxNchdPD0NlHXsJd_X8dBhVMMMh8dd9Hjjtb7AsKgxxsNaUi52qfl7o3SWLVAWVM06cYIQzVKqhO2Z8GxSFDXcEwNuIoQlyZZLQj5LFvPYWgetdCfZX.mULyAYeUTfAQXv.nEq1LhScbzteV0NlNknlwGtChz_YiFJVg_7f.XMhHNzsv1o2aJce3b8JMnrj_u7VNY22y.M_DQ.AD_h4itfhOmm4ngHGMGxtbbMEHCJ9VMhB2xujoUxLNGhzPlF6LwiY0eZZ9ZNxKKDVt_PDMoHUUMdr5YfpSNVZuzQjqhj_i4qn5WKPEFx9ORltwzrw1Ls6TRpKSgQPOajeUpC.G4nSTz56wJnWBPF1fLV5NaMab1Y6tJS8oZXJjIEzGdE8C8UirGQCeZnr1Gn6Bfow4NzkV_.PA5CyfPCml2BlF7Tn',
    '_ga': 'GA1.1.1880707367.1731336266',
    '__gads': 'ID=2f68e49bf6b21a33:T=1731336288:RT=1731342655:S=ALNI_MaKBxBiySHqf5pMHNnAtgySAzwyaw',
    '__gpi': 'UID=00000f6623e3aafe:T=1731336288:RT=1731342655:S=ALNI_MZddt_64JSmTFK48dpPU6WRKhlxlQ',
    '__eoi': 'ID=8b626cf14807e69d:T=1731336288:RT=1731342655:S=AA-AfjYCn9Z2Y6Gy6oDS5SXbMm97',
    'FCNEC': '%5B%5B%22AKsRol8cwbIVpxcZa-5tLvug3-gQh6FIL1bnB_CmSxWN4ouzMM3YTDekvCl9DeLwC9r3rFnKW0OZ3WUmLz4S8F8JWX1EjHI6n6Y-g7v3A2WYAi4imffEEIsnwWnAfEEDAay4PdQeiqL0EO9jglwttdSVJwjNk7fTtg%3D%3D%22%5D%5D',
    '_ga_ZSF3D6YSLC': 'GS1.1.1731342639.2.1.1731342681.18.0.0',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'cf_clearance=P06jsxmcAOm5RE667Liyy8JqAqmtK.yxk37RcFoR4jE-1731336275-1.2.1.1-YQUdbxr83VgvzpaPhbY9lFxNchdPD0NlHXsJd_X8dBhVMMMh8dd9Hjjtb7AsKgxxsNaUi52qfl7o3SWLVAWVM06cYIQzVKqhO2Z8GxSFDXcEwNuIoQlyZZLQj5LFvPYWgetdCfZX.mULyAYeUTfAQXv.nEq1LhScbzteV0NlNknlwGtChz_YiFJVg_7f.XMhHNzsv1o2aJce3b8JMnrj_u7VNY22y.M_DQ.AD_h4itfhOmm4ngHGMGxtbbMEHCJ9VMhB2xujoUxLNGhzPlF6LwiY0eZZ9ZNxKKDVt_PDMoHUUMdr5YfpSNVZuzQjqhj_i4qn5WKPEFx9ORltwzrw1Ls6TRpKSgQPOajeUpC.G4nSTz56wJnWBPF1fLV5NaMab1Y6tJS8oZXJjIEzGdE8C8UirGQCeZnr1Gn6Bfow4NzkV_.PA5CyfPCml2BlF7Tn; _ga=GA1.1.1880707367.1731336266; __gads=ID=2f68e49bf6b21a33:T=1731336288:RT=1731342655:S=ALNI_MaKBxBiySHqf5pMHNnAtgySAzwyaw; __gpi=UID=00000f6623e3aafe:T=1731336288:RT=1731342655:S=ALNI_MZddt_64JSmTFK48dpPU6WRKhlxlQ; __eoi=ID=8b626cf14807e69d:T=1731336288:RT=1731342655:S=AA-AfjYCn9Z2Y6Gy6oDS5SXbMm97; FCNEC=%5B%5B%22AKsRol8cwbIVpxcZa-5tLvug3-gQh6FIL1bnB_CmSxWN4ouzMM3YTDekvCl9DeLwC9r3rFnKW0OZ3WUmLz4S8F8JWX1EjHI6n6Y-g7v3A2WYAi4imffEEIsnwWnAfEEDAay4PdQeiqL0EO9jglwttdSVJwjNk7fTtg%3D%3D%22%5D%5D; _ga_ZSF3D6YSLC=GS1.1.1731342639.2.1.1731342681.18.0.0',
        'hx-current-url': 'https://ssstik.io/',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'priority': 'u=1, i',
        'referer': 'https://ssstik.io/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"130.0.6723.117"',
        'sec-ch-ua-full-version-list': '"Chromium";v="130.0.6723.117", "Google Chrome";v="130.0.6723.117", "Not?A_Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': 'https://www.tiktok.com/@romania/video/7410452584588250401',
        'locale': 'en',
        'tt': 'WEp5bXY3',
    }
    
    print("STEP 4: Getting the download link")
    print("If this step fails, PLEASE read the steps above")
    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)

    downloadSoup = BeautifulSoup(response.text, "html.parser")

    downloadLink = downloadSoup.a["href"]
    videoTitle = downloadSoup.p.getText().strip()

    print("STEP 5: Saving the video :)")
    mp4File = urlopen(downloadLink)
    # Feel free to change the download directory
    with open(f"videos/{id}-{videoTitle}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break

print("STEP 1: Open Chrome browser")
options = Options()
options.add_argument("start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)
# Change the tiktok link
driver.get("https://www.tiktok.com/@romania")

# IF YOU GET A TIKTOK CAPTCHA, CHANGE THE TIMEOUT HERE
# to 60 seconds, just enough time for you to complete the captcha yourself.
time.sleep(1)

scroll_pause_time = 1
screen_height = driver.execute_script("return window.screen.height;")
i = 1

print("STEP 2: Scrolling page")
while True:
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    if (screen_height) * i > scroll_height:
        break 

# this class may change, so make sure to inspect the page and find the correct class
className = "css-1uqux2o-DivItemContainerV2"

script  = "let l = [];"
script += "document.getElementsByClassName(\""
script += className
script += "\").forEach(item => { l.push(item.querySelector('a').href)});"
script += "return l;"

urlsToDownload = driver.execute_script(script)


print(f"STEP 3: Time to download {len(urlsToDownload)} videos")
for index, url in enumerate(urlsToDownload):
    print(f"Downloading video: {index}")
    downloadVideo(url, index)
    time.sleep(10)



