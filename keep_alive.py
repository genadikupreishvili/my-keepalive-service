import requests
import time
import os

# თქვენი ძირითადი აპლიკაციის URL
MAIN_APP_URL = os.environ.get('MAIN_APP_URL', 'https://genhub-kskx.onrender.com/')

# Keep-Alive სერვისის პერიოდულობა წუთებში
INTERVAL_MINUTES = 15

def keep_alive():
    while True:
        try:
            response = requests.get(MAIN_APP_URL)
            response.raise_for_status()
            print(f'Keep-Alive request sent to {MAIN_APP_URL}. Status code: {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'Error sending Keep-Alive request: {e}')

        time.sleep(INTERVAL_MINUTES * 60)  # დაცადება შემდეგი მოთხოვნის გასაგზავნად

if __name__ == '__main__':
    keep_alive()