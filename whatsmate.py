from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://web.whatsapp.com')
input('press anything to start.')
fhandle = open('names.txt')
data = fhandle.read()
lines = data.split('\n')
for line in lines:
    namemsg = line.split(",")
    search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search.send_keys(namemsg[0])
    time.sleep(5)
    name = driver.find_element_by_class_name('_3j7s9')
    name.click()
    time.sleep(5)
    msg = driver.find_element_by_class_name('_1Plpp')
    msg.send_keys(namemsg[1])
    time.sleep(5)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
    time.sleep(5)



#search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
#search.send_keys('sanju')
#time.sleep(5)
#name = driver.find_element_by_class_name('_3j7s9')
#name.click()
#time.sleep(5)
#msg = driver.find_element_by_class_name('_1Plpp')
#msg.send_keys('HI,DEAR HOW ARE YOU')
#time.sleep(5)
#button = driver.find_element_by_class_name('_35EW6')
#button.click()
#time.sleep(5)