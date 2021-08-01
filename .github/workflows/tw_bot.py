from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path="ruta del webdriver")
driver.get("https://twitter.com/login")
sleep(4)

driver.find_element_by_name('session[username_or_emai]').send_keys("nombre de usuario")
driver.find_element_by_name('session[password]').send_keys("contrasennia")
driver.find_element_by_name('session[username]').send_keys(Keys.RETURN)
sleep(4)

f = open("Sherk.txt", 'r')

for Tweets in f:
    if Tweets == "\n":
        continue
    driver.find_element_xpath("//a[@data-testid'SideNav_NewTweet_Button']").click()
    sleep(2)
    driver.find_element_class_name("notranslate").click()
    driver.find_element_class_name("notranslate").send_keys(Tweets)
    driver.find_element_xpath("//div[@data-testid='tweetButton']").click()
    sleep(23)

f.close()
