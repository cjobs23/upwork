from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set the URL of the form
url = 'https://example.com/contact'

# Set the form data
name = 'John Doe'
email = 'johndoe@example.com'
message = 'This is a test message.'
address = '123 Main St'
file1_path = '/path/to/file1'
file2_path = '/path/to/file2'
file3_path = '/path/to/file3'
file4_path = '/path/to/file4'

# Launch a Chrome browser
driver = webdriver.Chrome()

# Navigate to the form URL
driver.get(url)

# Fill in the form fields
name_field = driver.find_element_by_name('name')
name_field.send_keys(name)

email_field = driver.find_element_by_name('email')
email_field.send_keys(email)

message_field = driver.find_element_by_name('message')
message_field.send_keys(message)

address_field = driver.find_element_by_name('address')
address_field.send_keys(address)

# Upload files
file1_input = driver.find_element_by_name('file1')
file1_input.send_keys(file1_path)

file2_input = driver.find_element_by_name('file2')
file2_input.send_keys(file2_path)

file3_input = driver.find_element_by_name('file3')
file3_input.send_keys(file3_path)

file4_input = driver.find_element_by_name('file4')
file4_input.send_keys(file4_path)

# Agree to terms and conditions
agree_checkbox = driver.find_element_by_name('agree')
agree_checkbox.click()

# Submit the form
submit_button = driver.find_element_by_css_selector('button[type="submit"]')
submit_button.click()

# Wait for the form to submit
time.sleep(5)

# Verify that the form submission was successful
success_message = driver.find_element_by_css_selector('.success-message')
assert success_message.is_displayed()

# Close the browser
driver.quit()
#In this code, we added the address, file1_path, file2_path, file3_path, and file4_path variables to represent the additional form fields and files to upload. We then found the corresponding elements on the page using their names and used the send_keys() method to enter text and the send_keys(file_path) method to upload files.

After that, we found the agree checkbox and clicked on it. Finally, we submitted the form and waited for it to complete using time.sleep(), and then verified that the success message was displayed.
