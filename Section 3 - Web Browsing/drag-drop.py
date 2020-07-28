from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximise_window()

source = driver.find_element_by_xpath('//*[@id="box5"]')
destination = driver.find_element_by_xpath('//*[@id="box106"]')

actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()