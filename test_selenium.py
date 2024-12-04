from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a webpage
driver.get("https://www.google.com")

# Print the title of the page
print("Page Title:", driver.title)

# Optionally, you can perform more actions, like searching for a term
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.submit()

# Wait for a few seconds to see the result
driver.implicitly_wait(5)

# Print the title of the search results page
print("Search Results Page Title:", driver.title)

# Close the browser
driver.quit()