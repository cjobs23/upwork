import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Replace with your own Instagram username and password
username = "your_username"
password = "your_password"

# Replace with the path to your Chrome driver executable
chromedriver_path = "path/to/chromedriver"

# List of profile URLs to check
profile_urls = [
    "https://www.instagram.com/profile1/",
    "https://www.instagram.com/profile2/",
    "https://www.instagram.com/profile3/",
    # Add more profile URLs as necessary
]

# Open Chrome browser and log in to Instagram
driver = webdriver.Chrome(chromedriver_path)
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(2)
username_input = driver.find_element_by_name("username")
username_input.send_keys(username)
password_input = driver.find_element_by_name("password")
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)
time.sleep(2)

# Check if each profile is following you back
for profile_url in profile_urls:
    driver.get(f"{profile_url}following/")
    time.sleep(2)
    following_list = driver.find_elements_by_xpath("//ul[@class='jSC57  _6xe7A']/div/li")
    for following in following_list:
        if following.find_element_by_xpath(".//div/div[1]/a").get_attribute("href") == f"https://www.instagram.com/{username}/":
            print(f"{profile_url} is following you back.")
            break
    time.sleep(10)

# Close the browser
driver.quit()

##This script uses the Selenium library to automate the process of logging in to Instagram, navigating to each profile's following list, and checking if your profile is in the list. It also includes a time.sleep() function to slow down the script's execution and avoid being detected as a bot.
