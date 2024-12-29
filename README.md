# TikTok Video Scraper

This project is a Python-based web scraper designed to download videos from TikTok using Selenium, BeautifulSoup, and Requests. It fetches video URLs, processes the webpage to retrieve the video title and download link, and saves the videos locally with sanitized filenames.

## Features
- Scrapes video details from TikTok profiles or specific video URLs.
- Utilizes Selenium for dynamic content loading.
- Processes the page with BeautifulSoup for structured parsing.
- Downloads videos with sanitized file names for compatibility.

## Requirements
The following Python libraries and tools are required:
- `re`
- `requests`
- `urllib`
- `bs4` (BeautifulSoup)
- `selenium`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ghdbashen/tiktok-video-scraper.git
   cd tiktok-video-scraper
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download and set up the [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) compatible with your Chrome version.

4. Create a `videos/` directory to save downloaded videos:
   ```bash
   mkdir videos
   ```

## Usage

1. Replace the TikTok profile or video URL in the script:
   ```python
   driver.get("https://www.tiktok.com/@romania")
   data = {
       'id': 'https://www.tiktok.com/@romania/video/7410452584588250401',
       'locale': 'en',
       'tt': 'WEp5bXY3',
   }
   ```

2. Run the script:
   ```bash
   python tiktok_scraper.py
   ```

3. The downloaded video will be saved in the `videos/` directory with a sanitized file name.

## Important Notes
- This script includes cookies and headers for bypassing protections, but TikTok may block repeated or aggressive scraping. Use responsibly.
- Ensure compliance with TikTok's Terms of Service and local regulations.
- Adjust `driver.implicitly_wait()` for varying page load times.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer
This project is for educational purposes only. The author does not endorse illegal use of the scraper and is not responsible for any misuse.

