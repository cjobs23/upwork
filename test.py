import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Replace with your own Instagram username and password
username = "your_username"
password = "your_password"

# Replace with the path to your Chrome driver executable
chromedriver_path = "path/to/chromedriver"

# Read profile URLs from text file
with open("profiles.txt", "r") as f:
    profile_urls = f.read().splitlines()

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
##In this version, the script reads profile URLs from a text file named "profiles.txt" and uses the splitlines() method to convert the file contents into a list of strings, with each string representing a profile URL. You can modify the text file as necessary to add or remove profile URLs.
