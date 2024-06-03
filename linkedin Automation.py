"""terminal comandas to get the requirments 
pip install selenium
pip install webdriver-manager
# to see the versin of installed pakages 
pip show selenium  webdriver-manager """

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time 


options = Options()
options.add_experimental_option('detach' , True)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()

# time.sleep(2)

driver.get("https://www.linkedin.com/")





