from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# keep chrome browser open after program finish
chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

# crete and configure web driver
driver=webdriver.Chrome(options=chrome_option)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

cookie=driver.find_element(By.ID,value="cookie")

items=driver.find_elements(By.CSS_SELECTOR,value="#store div")
items_ids=[item.get_attribute("id") for item in items]
# items_ids.pop()
print(items_ids)
items_value=[value.text for value in items]
# print(items_value)
item_price=[]
for i in items_value[0:8]:
    x=i.split()
    if i==items_value[5] or i==items_value[7]:
        item_price.append(int(x[3].replace(",", "")))
    else:
       item_price.append(int(x[2].replace(",", "")))
print(item_price)

dict=dict(zip(item_price[::-1],items_ids[::-1]))

print(dict)



# Set the time limit in seconds
time_limit = 6
timeout= time.time()+time_limit
five_min = time.time() + 60*5 # 5 minutes

while True:
    # Your loop code here
    cookie.click()
    if time.time() > five_min:
        break
    # Check if the time limit has been exceeded
    if time.time() > timeout:
        money = int(driver.find_element(By.CSS_SELECTOR, value="#money").text)
        for key in dict:
            if key <= money:
                element=driver.find_element(By.ID,value=f"{dict[key]}")
                element.click()
cookies_per_sec=driver.find_element(By.ID,value="cps").text
print(cookies_per_sec)

# driver.quit()
