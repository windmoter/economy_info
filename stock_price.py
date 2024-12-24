# ... 기존 코드 ...
import requests
from bs4 import BeautifulSoup

# TradingView에서 가격 가져오기
def get_price():
    response = requests.get('https://www.tradingview.com/')
    soup = BeautifulSoup(response.text, 'html.parser')
    price_element = soup.find('div', class_='tv-symbol-price-quote')  # 가격 요소의 클래스 이름
    if price_element:
        return price_element.text.strip()
    return None

# 가격 출력
current_price = get_price()
if current_price:
    print(f"현재 가격: {current_price}")
else:
    print("가격을 가져오는 데 실패했습니다.")
# ... 기존 코드 ...