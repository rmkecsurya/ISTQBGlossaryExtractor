from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://glossary.istqb.org/')
driver.find_element(By.XPATH,'//*[@id="freeprivacypolicy-com---nb"]/div/div[3]/button[1]').click()
keywords = open("keywords.txt")
outputFile = open("output.txt",'w')
for i in keywords.read().split(','):
    searchKey = driver.find_element(By.XPATH,'//*[@id="search"]')
    searchKey.send_keys(i.strip())
    searchKey.send_keys(Keys.ENTER)
    definition = driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[3]/a/p').text
    searchKey.clear()
    outputFile.write(i.strip()+': '+definition+"\n")

outputFile.close()
keywords.close()
