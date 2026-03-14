from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

#Question1
'''driver.get("https://www.facebook.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"#_R_1h6kqsqppb6amH1_").send_keys("ABC@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#_R_1hmkqsqppb6amH1_").send_keys("1234567")
sleep(2)
driver.find_element(By.CSS_SELECTOR,".html-div.xdj266r.xat24cr.xexx8yu.xyri2b.x18d9i69.x1c1uobl.x6s0dn4.x78zum5.xl56j7k.x1e0frkt.xf0ucvx.xx2axb6").click()
sleep(2)
driver.close()'''

# Question2
'''driver.get("https://www.youtube.com")
driver.maximize_window()
sleep(2)
driver.find_element(By.NAME,"search_query").send_keys("melody hits")
driver.close()'''

# Question3
'''driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,"name").send_keys("Kakul")
sleep(2)
driver.find_element(By.ID,"email").send_keys("ABC@gmail.com")
sleep(2)
driver.find_element(By.ID,"password").send_keys("1234567")
sleep(2)
driver.close()'''

# Question4
'''driver.get("https://www.myntra.com")
driver.maximize_window()
sleep(2)
driver.find_element(By.CLASS_NAME,"desktop-searchBar").send_keys("shoes")
driver.close()'''