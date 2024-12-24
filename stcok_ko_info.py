from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image
import time

# ChromeDriver 경로 설정 
chrome_driver_path = 'path/to/chromedriver'  # ChromeDriver 경로로 변경
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# TradingView 차트 URL
url = 'https://www.tradingview.com/chart/'  # 원하는 차트 URL로 변경
driver.get(url)

# 페이지 로딩 대기
time.sleep(10)  # 페이지가 완전히 로드될 때까지 대기

# 차트 캡처
chart_element = driver.find_element(By.CLASS_NAME, 'chart-container')  # 차트 요소의 클래스 이름
chart_element.screenshot('tradingview_chart.png')  # 차트 스크린샷 저장

# 브라우저 종료
driver.quit()

# 이미지 열기 (선택 사항)
image = Image.open('tradingview_chart.png')
image.show()