import requests as r
import time
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import threading

# pre requisites for binding firefox with selenium

def spam(video_duration):
	options = Options()
	options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
	driver = webdriver.Firefox(executable_path=r'C:\Users\PRANAV U\Desktop\Hacking\MyReports\RLB_ON_PAYPAL\geckodriver.exe', options=options)
	driver.get("https://www.youtube.com/watch?v=qyLwLOnhGw4&t=32s")
	youtube_play = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/button")
	youtube_play.click()
	time.sleep(video_duration)
	driver.close()

while True:
	spam(240)
