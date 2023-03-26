# Google Classrom Automation by cop6567 on github

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
# Replace with the path to your Chromedriver executable

# Replace with your email and password
email = 'EMAIL HERE'
password = 'PASSWORD HERE'

# Create a new Chromedriver instance. Safari() can also be used if you're on Mac. Just make sure to enable automation in Safari
driver = webdriver.Chrome()

# Go to the Google login page
driver.get('PRIVATE LINK HERE') # check out README.md on how to get your kwn private link

# Find the email input field and enter your email
email_field = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email_field.send_keys(email)
email_field.send_keys(Keys.RETURN)

# Wait for the password input field to load and enter your password
time.sleep(2)
password_field = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# Wait for the page to load and go to the Google Classroom page
time.sleep(5)
driver.get('https://classroom.google.com/u/0/a/not-turned-in/all')


# Wait for the page to load and get the list of assignments
print('Analysing')
time.sleep(5)
assignments = driver.find_elements(By.CLASS_NAME, 'I2pI')

# Saving output to a list
assignments_list = []
for assignment in assignments:
    content = assignment.text
    assignments_list.append(content)

# Accesing the assignments with list index
if int(assignments_list[0]) == 0:
    print('It appears you have no assignments with no due date')
else:
    print(f'It appears you have {assignments_list[0]} assignments with no due date')
    print(f'No due date. {assignments_list[0]}')


if int(assignments_list[1]) == 0:
    print(f'You have no Assignments due this week. {assignments_list[1]}')
else:
    print(f'You have {assignments_list[1]} Assignments due this week.')
    print(f'This week. {assignments_list[1]}')


if int(assignments_list[2]) == 0:
    print('You have no Assignments due Next Week')
else:
    print(f'You have {assignments_list[2]} Assignments due Next Week')
    print(f'Next Week. {assignments_list[2]}')


if int(assignments_list[3]) == 0:
    print('You have no assignments due later')
else:
     print(f'You have {assignments_list[3]} assignments due later')
     print(f'Later. {assignments_list[3]}')

