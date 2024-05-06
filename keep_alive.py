import requests
import time
import os


MAIN_APP_URL = os.environ.get('MAIN_APP_URL', 'https://genhub-kskx.onrender.com/')


INTERVAL_MINUTES = 15

def keep_alive():
    while True:
        try:
            response = requests.get(MAIN_APP_URL)
            response.raise_for_status()
            print(f'Keep-Alive request sent to {MAIN_APP_URL}. Status code: {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'Error sending Keep-Alive request: {e}')
        
        time.sleep(INTERVAL_MINUTES * 60)

def send_keep_alive(host):
    try:
        url = f"http://{host}/"
        response = requests.get(url)
        print(f"Keep-alive ping sent to {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending keep-alive ping: {e}")
        
if __name__ == '__main__':
    keep_alive()
    host = os.environ.get("RENDER_INTERNAL_HOSTNAME")
    if host:
        send_keep_alive(host)
