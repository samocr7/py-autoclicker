import pyautogui
import sys
import time
from datetime import datetime, timedelta
import random

def click():
    print('clicked')
    pyautogui.click()


def main():
    # python autoclick.py 100 true 120
    # this will click every 100ms. double click. run for 120 minutes 
    start_time = datetime.now()
    interval = int(sys.argv[1])
    double_click = sys.argv[2]
    minutes = int(sys.argv[3])
    while True:
        sleep_interval = random.randint(interval-50, interval+50) / 1000
        print(f"sleeping for {sleep_interval} seconds")
        time.sleep(sleep_interval)
        if start_time + timedelta(minutes=minutes) <= datetime.now():
            print("Finished")
            break
        click()
        if double_click == 'true':
            time.sleep(random.randint(0,200) / 1000)
            click()
        


main()