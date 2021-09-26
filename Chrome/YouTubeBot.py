from selenium import webdriver
import time
#-------------------------------- FUNCTIONS --------------------------------#
def duration_split(duration):

    hour = 0
    min = 0
    sec = 0

    list = duration.split(":")

    if len(list) == 3:
        hour = int(list[0])
        min = int(list[1])
        sec = int(list[2])
    else:
        min = int(list[0])
        sec = int(list[1])
    
    return hour*3600 + min*60 + sec

#-------------------------------- MAIN EXECUTION --------------------------------#
while True:

    driver = webdriver.Chrome()

    # ---> Enter YouTube video URL below <--- #
    driver.get("https://www.youtube.com/watch?v=LmdhWsccv4w&lc=UgyW9iIVYCuCp8mK9CV4AaABAg")

    # ---> Enter duration below (format = "hour:min:sec" or "min:sec") <--- #
    duration = "4:57" 

    duration = duration_split(duration=duration)

    plybtn = driver.find_element_by_class_name("ytp-play-button")
    time.sleep(3)
    # ---> If the video doesnt start playing within three seconds of opening, then disable this  <--- #
    plybtn.click()                      

    time.sleep(duration)
    driver.close()
