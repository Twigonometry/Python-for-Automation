from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
message_field = driver.find_element_by_xpath('//*[@id="user-message"]')
message_field.send_keys("hello world")
button = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')
button.click()