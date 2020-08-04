# 인덱스 버튼 클릭
from selenium import webdriver

for page in range(1,17):                     [1] 
    if page == 1:                            [2]
        pass
    
    else :                                   [3]
        elements = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[1]/div/button[{page}]') # target elements xpath
        driver.execute_script("arguments[0].click();", elements)

# 무한 스크롤
import time

    SCROLL_PAUSE_TIME = 2

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")         [1]

    while True:
        # Scroll down to bottom                                                      [2]
          driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)                                                [3]
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")  [4]
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height            [5]
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:                                                [6]
            break

        last_height = new_height