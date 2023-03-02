from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set the login credentials
username = 'example@gmail.com'
password = 'password123'

# Set the Airbnb page URL to fetch
airbnb_url = 'https://www.airbnb.it/rooms/27461318??preview_for_ml=true&source_impression_id=p3_1673300668_qRW6xsJUnunFVqdP'

# Launch a Chrome browser
driver = webdriver.Chrome()

# Login to the Google account
driver.get('https://accounts.google.com/')
email_field = driver.find_element_by_id('identifierId')
email_field.send_keys(username)
email_field.send_keys(Keys.RETURN)
driver.implicitly_wait(10)
password_field = driver.find_element_by_name('password')
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# Signup to Airbnb using the Google credentials
driver.get('https://www.airbnb.com/')
continue_with_google_button = driver.find_element_by_xpath('//button[@data-testid="social-auth-button-google"]')
continue_with_google_button.click()

# Fetch the Airbnb page and save to a text file
driver.get(airbnb_url)
with open('airbnb_page.txt', 'w') as f:
    f.write(driver.page_source)

# Close the browser
driver.quit()
