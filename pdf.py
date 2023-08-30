# selenium 4
import base64
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')

# download_dir = "/home/gmyou/dev/src/test/react-crawler-by-python"
# profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
#                "download.default_directory": download_dir , "download.extensions_to_open": "applications/pdf"}
# chrome_options.add_experimental_option("prefs", profile)

from selenium.webdriver.common.print_page_options import PrintOptions
print_options = PrintOptions()
print_options.page_ranges = ['1-2']




driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=KR&q=kt.com&search_type=keyword_unordered&media_type=all')
# driver.get('https://www.naver.com/')

time.sleep(5)

driver.maximize_window()

height = driver.execute_script('return document.documentElement.scrollHeight')
width  = driver.execute_script('return document.documentElement.scrollWidth')
driver.set_window_size(width, height)  # the trick

time.sleep(5)

print(driver.title)

# screenshot after etire load
if (driver.execute_script('return document.readyState') == 'complete'):
    print('complete')
    # driver.save_screenshot('screenshot.png')
    base64code = driver.print_page(print_options)
    # decode base64code
    with open('pdf.pdf', 'wb') as file:
        decoded = base64.b64decode(base64code)
        file.write(decoded)

driver.quit()