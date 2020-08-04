# selenium 설치 후 import
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 초기화 --------------------------------------------
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("disable~~")

# 크롬드라이버 경로
path = '/home/sundoosdedu/다운로드/chromedriver'
# 선언
driver  = webdriver.Chrome(path)

# 딜레이
driver.implicitly_wait(3)
# 크롤링 대상 사이트
driver.get('site_url')
# 크롤링 대상 elements
test = driver.find_element_by_xpath('요소 xpath copy').text